import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置字体
plt.rcParams['font.family'] = ['SimHei']  # Windows下使用SimHei
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# 定义各模块框位置和大小
components = {
    "用户输入\n（Streamlit界面）": (0.05, 0.75, 0.25, 0.15),
    "文本输入": (0.05, 0.55, 0.2, 0.1),
    "图片上传": (0.05, 0.4, 0.2, 0.1),
    "音频上传": (0.05, 0.25, 0.2, 0.1),
    "实时录音": (0.05, 0.1, 0.2, 0.1),
    "百度智能云服务\n（API Key认证）": (0.4, 0.55, 0.3, 0.35),
    "ERNIE-Bot\n大模型": (0.75, 0.65, 0.2, 0.2),
    "情绪识别与学习建议\n（模型输出）": (0.75, 0.35, 0.2, 0.2)
}

# 绘制组件
for comp, (x, y, w, h) in components.items():
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                        linewidth=1, edgecolor='black', facecolor='lightblue'))
    plt.text(x + w/2, y + h/2, comp, ha='center', va='center', fontsize=12)

# 绘制箭头表示数据流动
arrows = [
    ((0.25, 0.6), (0.4, 0.725)),
    ((0.25, 0.45), (0.4, 0.65)),
    ((0.25, 0.3), (0.4, 0.575)),
    ((0.25, 0.15), (0.4, 0.5)),
    ((0.7, 0.725), (0.75, 0.75)),
    ((0.7, 0.725), (0.75, 0.5)),
    ((0.85, 0.65), (0.85, 0.55))
]

for start, end in arrows:
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2))

# 设置图标题
plt.title("融合视觉、音频和文本的多模态情绪识别与学习引导系统架构图", fontsize=16)

plt.show()
