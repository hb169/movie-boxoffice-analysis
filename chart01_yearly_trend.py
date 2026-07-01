import matplotlib.pyplot as plt
import json
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../charts1')
os.makedirs(CHARTS_DIR, exist_ok=True)

with open('box_office_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

year_data = {}
for m in data:
    y = m['year']
    if y not in year_data:
        year_data[y] = {'count': 0, 'total_box': 0}
    year_data[y]['count'] += 1
    year_data[y]['total_box'] += m['box_office_yi']

years = sorted(year_data.keys())
counts = [year_data[y]['count'] for y in years]
total_boxes = [year_data[y]['total_box'] for y in years]

fig, ax1 = plt.subplots(figsize=(10, 6))
x = np.arange(len(years))
width = 0.4
bars = ax1.bar(x, counts, width, color='#4472C4', label='电影数量', zorder=3)
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('电影数量（部）', fontsize=12, color='#4472C4')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45, fontsize=9)
ax1.tick_params(axis='y', labelcolor='#4472C4')
ax1.grid(axis='y', alpha=0.3, zorder=0)
for bar, c in zip(bars, counts):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             str(c), ha='center', va='bottom', fontsize=8, color='#4472C4')

ax2 = ax1.twinx()
ax2.plot(x, total_boxes, 'o-', color='#ED7D31', linewidth=2, markersize=5, label='总票房（亿元）', zorder=4)
ax2.set_ylabel('总票房（亿元）', fontsize=12, color='#ED7D31')
ax2.tick_params(axis='y', labelcolor='#ED7D31')
for i, v in enumerate(total_boxes):
    ax2.annotate(f'{v:.1f}', (x[i], v), textcoords='offset points',
                 xytext=(0, 8), ha='center', fontsize=7, color='#ED7D31')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)
ax1.set_title('图1 各年度电影数量与总票房趋势', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig1.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig1.png')
plt.show()
