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

rated = [m for m in data if m.get('rate') is not None and m['rate'] > 0]
rates = [m['rate'] for m in rated]
boxes = [m['box_office_yi'] for m in rated]

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(rates, boxes, c='#4472C4', alpha=0.6, s=40, edgecolors='white', linewidth=0.5, zorder=3)
z = np.polyfit(rates, boxes, 1)
p = np.poly1d(z)
x_line = np.linspace(min(rates), max(rates), 100)
ax.plot(x_line, p(x_line), '--', color='red', linewidth=1.5,
        label=f'趋势线 (y={z[0]:.2f}x{z[1]:+.2f})')
ax.set_xlabel('豆瓣评分', fontsize=12)
ax.set_ylabel('票房（亿元）', fontsize=12)
ax.legend(fontsize=10)
ax.grid(alpha=0.3, zorder=0)
ax.set_title('图6 豆瓣评分与票房关系', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig6.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig6.png')
plt.show()
