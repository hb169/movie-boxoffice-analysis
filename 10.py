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

audiences = [m['avg_audience_per_screen'] for m in data if m['avg_audience_per_screen'] > 0]
box_a = [m['box_office_yi'] for m in data if m['avg_audience_per_screen'] > 0]

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(audiences, box_a, c='#ED7D31', alpha=0.6, s=40, edgecolors='white', linewidth=0.5, zorder=3)
z3 = np.polyfit(audiences, box_a, 1)
p3 = np.poly1d(z3)
x_line3 = np.linspace(min(audiences), max(audiences), 100)
ax.plot(x_line3, p3(x_line3), '--', color='red', linewidth=1.5,
        label=f'趋势线 (y={z3[0]:.2f}x{z3[1]:+.2f})')
ax.set_xlabel('场均观影人数（人）', fontsize=12)
ax.set_ylabel('票房（亿元）', fontsize=12)
ax.legend(fontsize=10)
ax.grid(alpha=0.3, zorder=0)
ax.set_title('图8 场均观影人数与票房关系', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig8.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig8.png')
plt.show()
