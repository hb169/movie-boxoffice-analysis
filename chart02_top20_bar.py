import matplotlib.pyplot as plt
import json
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../charts1')
os.makedirs(CHARTS_DIR, exist_ok=True)

with open('box_office_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

top20 = sorted(data, key=lambda x: x['box_office_yi'], reverse=True)[:20]
top20.reverse()
titles = [m['title'] for m in top20]
values = [m['box_office_yi'] for m in top20]
colors = ['#C00000' if i >= 17 else '#ED7D31' if i >= 14 else '#4472C4' for i in range(20)]

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(range(len(titles)), values, color=colors, height=0.7, zorder=3)
ax.set_yticks(range(len(titles)))
ax.set_yticklabels(titles, fontsize=9)
ax.set_xlabel('票房（亿元）', fontsize=12)
for bar, v in zip(bars, values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{v:.2f}', va='center', fontsize=8)
ax.grid(axis='x', alpha=0.3, zorder=0)
ax.set_title('图2 中国影史票房Top20电影', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig2.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig2.png')
plt.show()
