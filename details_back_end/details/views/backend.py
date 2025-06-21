import re,psutil,os
from flask import session,render_template,jsonify,redirect,url_for, request

import requests
from io import BytesIO

from details import app
from details.api_v1.database import DataBase
from details.forms import *
from details.methods import *
from details.errors import api_abort

# 根页面
@app.route("/")
def index():
    if 'logged_in' in session:
        return redirect(url_for('overview'))
    else:
        return redirect(url_for('login'))
    
# 服务器日志页面
@app.route("/backend/log")
def log():
    if not 'id' in session:
        return redirect(url_for('login'))
    return render_template("logs.html",active_page = 'log')

# overview页面
@app.route("/backend/overview")
def overview():
    if not 'id' in session:
        return redirect(url_for('login'))
    return render_template("overview.html",active_page = 'overview')

# 管理页面
@app.route("/backend/manage")
def manage():
    if not 'id' in session:
        return redirect(url_for('login'))
    return render_template("manage.html",active_page = 'manage')

# 以下为AJAX请求的资源端点
@app.route("/ajax/logdata")
def  logdata():
    db = DataBase()
    f = open("DetailsLog.log","r")
    data = f.readlines()
    data.reverse()
    tot = 0
    res = [dict()]
    tit = ["User_Agent","Method","Args","Form","Authorization"]
    for i,line in enumerate(data):
        #print(line)
        if line.startswith("Quest"):
            key = line.split(":")[1]
            db.crs.execute("SELECT User_Agent,Method,Args,Form,Authorization FROM `Log` WHERE ID = %s",key)
            s = ''
            t = db.crs.fetchall()
            for j,w in enumerate(t[0]):
                if w == None: w = "None"
                s += '<b>' + tit[j] + '：' + '</b>' + w + '<br>'
            res[tot-1]['content'] = s
        else:
            if '/backend/' in line or '/ajax/' in line:
                continue
            line = re.sub(r'\?[^ ]+', '', line)
            res[tot]['title'] = line
            res.append(dict())
            tot += 1
        if tot >= 30:break
    res = res[:-1]
    return jsonify(res)

@app.route("/ajax/usagedata")
def  usagedata():
    # 获取 CPU 和内存占用信息
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    memory_total = round(psutil.virtual_memory().total/1000000000,2)
    memory_available = round(psutil.virtual_memory().available/1000000000,2)

    return jsonify(cpu_percent=cpu_percent, memory_percent=memory_percent, memory_total = memory_total, memory_available =  memory_available)

@app.route("/ajax/dbdata")
def dbdata():
    db = DataBase()

    db.crs.execute("SHOW GLOBAL STATUS LIKE 'Threads_connected';")
    Threads_connected = db.crs.fetchall()[0][1]
    db.crs.execute("SHOW GLOBAL STATUS LIKE 'Innodb_row_lock_time';")
    Innodb_row_lock_time = db.crs.fetchall()[0][1]

    db.crs.execute("SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_read_requests';")
    Innodb_buffer_pool_read_requests = db.crs.fetchall()[0][1]
    db.crs.execute("SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_reads';")
    Innodb_buffer_pool_reads = db.crs.fetchall()[0][1]
    cache_hit_rate = round((1 - (int(Innodb_buffer_pool_reads) / int(Innodb_buffer_pool_read_requests)))*100,2)

    db.crs.execute("SELECT COUNT(*) FROM `user`;")
    user_number = db.crs.fetchall()[0][0]
    db.crs.execute("SELECT COUNT(*) FROM message;")
    message_number = db.crs.fetchall()[0][0]
    
    redis_data = db.tgb.info()
    
    db.close()

    return jsonify(Threads_connected=Threads_connected, Innodb_row_lock_time=Innodb_row_lock_time, 
                   cache_hit_rate = cache_hit_rate, user_number = user_number, message_number = message_number,
                   connected_clients = redis_data['connected_clients'],
                   used_memory_human = redis_data['used_memory_human'],
                   total_connections_received = redis_data['total_connections_received'],
                   total_commands_processed = redis_data['total_commands_processed'],)

@app.route("/ajax/backupdata")
def backupdata():
    db = DataBase()
    
    db.crs.execute("SELECT COUNT(*) FROM `Summary` WHERE Statu = 0;")
    success_number = db.crs.fetchall()[0][0]

    l1 = os.listdir('/home/RedisBackup/')
    n1 = len(l1)
    l2 = os.listdir('/home/MySQLBackup/')
    n2 = len(l2)

    return jsonify(success_number=success_number, redis_backup_number = n1, mysql_backup_number = n2,
                   redis_backup_list = l1,mysql_backup_list = l2)


@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']
    data = file.stream.read()

    files = {'file': (file.filename, BytesIO(data), file.mimetype)}

    try:
        response = requests.post(
            'https://picui.cn/api/v1/upload',
            files=files,
            headers={
                "Authorization": "Bearer 1230|Wnq1A7RDHQBvgXSEAGLiGjnV7M9b28iWlCyuDmR2",
                "Accept": "application/json",
            }
        )
        
        return jsonify(response.json())
    except Exception as e:
        print(f"Error uploading image: {e}")
        return jsonify({'error': str(e)}), 500