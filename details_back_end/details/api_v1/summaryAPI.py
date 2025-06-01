import openai

from flask import jsonify, request,g
from flask.views import MethodView

from details.errors import api_abort
from details.auth import Validate_uid,auth_required
from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.checker import ValidateAccount
from details.api_v1.tools import Decoder


class SummaryAPI(MethodView):
	decorators = [auth_required]
	def post(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		params = (('Text','STRING','NN'),)

		try: Text = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		db.crs.execute("INSERT INTO Summary (Text,Statu) VALUES (%s,0)",Text)
		db.crs.execute("SELECT LAST_INSERT_ID()")
		db.commit()
		summary_id = db.crs.fetchone()[0]
		return jsonify({'ID':summary_id})

class FetchSummaryAPI(MethodView):
	decorators = [auth_required]
	def get(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		params = (('ID','INT','NN'),)

		try: ID = Decoder(request.args,params)
		except: return api_abort(400,"invalid form")
		
		db.crs.execute("SELECT Text,Statu FROM Summary WHERE ID=%s",ID)
		res = db.crs.fetchall()
		text = res[0][0]
		statu = res[0][1]
		if statu == 0:
			return api_abort(400,"Summary not ready")
		else:
			return jsonify({'Text':text})
prompt = "用大约40个字归纳这条通知的主要内容:"
openai.api_key = "<KEY HERE>"
class CalcSummaryAPI(MethodView):
	def get(self):
		db = DataBase()
		db.crs.execute("SELECT ID,Text FROM Summary WHERE STATU = 0")
		data = db.crs.fetchall()
		for l in data:
			print(l[1])
			response = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				messages=[
					{"role": "system", "content": prompt},
					{"role": "user", "content": l[1]}
				],
				temperature=0.4,
				max_tokens=200,
				top_p=1.0,
				frequency_penalty=0.0,
				presence_penalty=0.0
			)
			# response = openai.ChatCompletion.create(
			# model="text-davinci-003",
			# prompt="归纳这条消息的摘要:\n%s"%l[1],
			# temperature=0.3,
			# max_tokens=100,
			# top_p=1.0,
			# frequency_penalty=0.0,
			# presence_penalty=0.0
			# )
			res = response['choices'][0]['message']['content']
			print(res)
			#db.crs.execute("UPDATE Summary SET Statu = 1,Text = %s WHERE ID = %s",(res,l[0]))
			#db.commit()
		return api_abort(204)

api_v1.add_url_rule('/summary/post_text', view_func=SummaryAPI.as_view('SummaryAPI'), methods=['POST'])
api_v1.add_url_rule('/summary/fetch_text', view_func=FetchSummaryAPI.as_view('FetchSummaryAPI'), methods=['GET'])
api_v1.add_url_rule('/summary/calc_summary', view_func=CalcSummaryAPI.as_view('CalcSummaryAPI'), methods=['GET'])