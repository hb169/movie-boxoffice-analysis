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

labels = ['票房(亿)', '年份', '平均票价', '场均人数', '评分']
box_vals = [m['box_office_yi'] for m in data]
year_vals = [m['year'] for m in data]
price_vals = [m['avg_ticket_price'] for m in data]
aud_vals = [m['avg_audience_per_screen'] for m in data]
rate_vals = [m.get('rate', 0) or 0 for m in data]

matrix = np.array([box_vals, year_vals, price_vals, aud_vals, rate_vals])
corr = np.corrcoef(matrix)

fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(corr, cmap='RdYlBu_r', vmin=-1, vmax=1, aspect='auto')
ax.set_xticks(range(len(labels)))
ax.set_yticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=10, rotation=45, ha='right')
ax.set_yticklabels(labels, fontsize=10)

for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f'{corr[i,j]:.2f}', ha='center', va='center', fontsize=10,
                color='white' if abs(corr[i,j]) > 0.5 else 'black')

fig.colorbar(im, ax=ax, shrink=0.8)
ax.set_title('图12 多因素相关性热力图', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig12.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig12.png')
plt.show()
