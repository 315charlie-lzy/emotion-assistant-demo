# Emotion Assistant Demo

一个基于 **百度智能云千帆大模型** 和 **Streamlit** 的多模态情绪识别与学习引导演示系统。  
系统支持 **文本、音频、视觉（人脸表情）** 三种模态的情绪识别，并通过大模型生成个性化的学习鼓励建议。  

---

✨ 功能特性
- 📝 **文本情绪识别**：输入学习感受，模型自动判断情绪并给出鼓励建议  
- 🎙️ **语音情绪识别**：上传语音文件或实时录音 → 自动转写 → 模型分析情绪  
- 🖼️ **视觉情绪识别**：上传人脸照片 → 调用百度人脸识别 API → 模型输出情绪结果  
- 🤖 **大模型学习引导**：基于 ERNIE-Bot 的上下文理解与生成能力，提供学习激励  

---

🛠️ 环境依赖

请先安装以下依赖：
```bash
pip install -r requirements.txt
````

依赖内容：

* `streamlit`：前端界面
* `openai`：调用百度千帆 OpenAI 协议接口
* `requests`：API 请求
* `ffmpeg-python`：音频转码工具
* `streamlit-audio-recorder`：网页端录音插件

---

🚀 运行方法

1. **克隆仓库**

```bash
git clone https://github.com/你的用户名/emotion-assistant-demo.git
cd emotion-assistant-demo
```

2. **配置 API Key**
   在 `openai_api.py` 和 `baidu_api.py` 中，将 `你的API_KEY` 替换为在百度智能云控制台申请的 API Key。

3. **启动应用**

```bash
streamlit run app.py
```

4. **打开浏览器**
   访问 `http://localhost:8501` 即可使用。

