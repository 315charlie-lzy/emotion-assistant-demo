import streamlit as st
from openai_api import chat_with_ernie
from baidu_api import speech_to_text, analyze_image_emotion
import tempfile
import os
import ffmpeg
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="情绪识别与学习引导", layout="centered")
st.title("🎓 情绪识别与学习引导 Demo ")

# 文本情绪识别
st.header("📝 文本情绪识别")
text_input = st.text_area("请输入你的学习感受：")
if st.button("分析文本情绪"):
    if not text_input.strip():
        st.warning("请输入内容后再发送。")
    else:
        prompt_text = f"请判断以下内容的情绪，并给予正向鼓励：\n“{text_input}”"
        reply = chat_with_ernie(prompt_text)
        st.success("模型建议：")
        st.write(reply)

# 图片表情识别
st.header("🖼️ 图片表情识别")
image_file = st.file_uploader("上传一张人脸图片（jpg/png）", type=["jpg", "jpeg", "png"])
if image_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
        tmp_img.write(image_file.read())
        img_path = tmp_img.name
    result = analyze_image_emotion(img_path)
    st.image(image_file, caption="上传图片预览", width=300)
    st.info(result)
    os.remove(img_path)

# 上传语音并识别
st.header("📤 上传语音文件（WAV）")
audio_file = st.file_uploader("上传一段语音（16kHz 单声道 WAV）", type=["wav"])
if audio_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
        tmp_audio.write(audio_file.read())
        audio_path = tmp_audio.name
    recognized_text = speech_to_text(audio_path)
    os.remove(audio_path)
    st.write(f"识别文本：{recognized_text}")
    prompt_audio = f"请判断以下一句话的情绪，并给予正向鼓励：\n“{recognized_text}”"
    reply = chat_with_ernie(prompt_audio)
    st.success("模型建议：")
    st.write(reply)

# 实时录音并识别
st.header("🎙️ 实时录音并识别")
audio_bytes = audio_recorder(text="点击录音 / 停止", icon_size="2x")
if audio_bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp_raw:
        tmp_raw.write(audio_bytes)
        raw_path = tmp_raw.name
    wav_path = raw_path.replace(".webm", ".wav")
    try:
        ffmpeg.input(raw_path).output(wav_path, ar=16000, ac=1).run(overwrite_output=True, quiet=True)
        recognized_text = speech_to_text(wav_path)
        st.audio(audio_bytes, format="audio/webm")
        st.write(f"识别文本：{recognized_text}")
        prompt_rec = f"请判断以下一句话的情绪，并给予正向鼓励：\n“{recognized_text}”"
        reply = chat_with_ernie(prompt_rec)
        st.success("模型建议：")
        st.write(reply)
    except Exception as e:
        st.error(f"录音转码或识别失败：{e}")
    finally:
        os.remove(raw_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
