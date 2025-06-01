import requests
import json

API_KEY = "C2dtGONW1YTH6BtvXR4ou8uI"
SECRET_KEY = "EGQzZQCa8Fh1lGWVWOQANlIGCTGefGtF"

def get_summary(body):

    try:
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": body
                }
            ],
            "system": "以下是一则大学校园内的通知，请简要概括其内容，并使用纯文本格式输出。"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, timeout=5000)
        return json.loads(response.text)["result"]
    except Exception as e:
        print(e)
        return None


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials",
              "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
