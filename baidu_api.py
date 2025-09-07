import requests
import base64
import os

API_KEY = "your api key"
# 公有云 AIP 服务根地址
BASE_URL = "https://aip.baidubce.com"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def speech_to_text(audio_file):
    # 使用 API Key 鉴权调用语音识别
    url = "https://vop.baidu.com/server_api"
    with open(audio_file, "rb") as f:
        data = f.read()
    speech_base64 = base64.b64encode(data).decode("utf-8")
    payload = {
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "streamlit_demo",
        "len": len(data),
        "speech": speech_base64
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    return res.json().get("result", ["语音识别失败"])[0]

def analyze_image_emotion(image_file):
    # 使用 API Key 鉴权调用人脸表情分析
    url = f"{BASE_URL}/rest/2.0/face/v3/detect"
    with open(image_file, "rb") as f:
        data = f.read()
    img_base64 = base64.b64encode(data).decode("utf-8")
    payload = {
        "image": img_base64,
        "image_type": "BASE64",
        "face_field": "expression",
        "max_face_num": 1
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    d = res.json()
    try:
        exp = d["result"]["face_list"][0]["expression"]["type"]
        mapping = {"none": "无表情", "smile": "微笑 😊", "laugh": "大笑 😂"}
        return f"检测到表情：{mapping.get(exp, exp)}"
    except:
        return "未检测到有效人脸或表情。"
