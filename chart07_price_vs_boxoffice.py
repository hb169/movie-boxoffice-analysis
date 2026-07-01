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

prices = [m['avg_ticket_price'] for m in data if m['avg_ticket_price'] > 0]
box_p = [m['box_office_yi'] for m in data if m['avg_ticket_price'] > 0]

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(prices, box_p, c='#70AD47', alpha=0.6, s=40, edgecolors='white', linewidth=0.5, zorder=3)
z2 = np.polyfit(prices, box_p, 1)
p2 = np.poly1d(z2)
x_line2 = np.linspace(min(prices), max(prices), 100)
ax.plot(x_line2, p2(x_line2), '--', color='red', linewidth=1.5,
        label=f'趋势线 (y={z2[0]:.2f}x{z2[1]:+.2f})')
ax.set_xlabel('平均票价（元）', fontsize=12)
ax.set_ylabel('票房（亿元）', fontsize=12)
ax.legend(fontsize=10)
ax.grid(alpha=0.3, zorder=0)
ax.set_title('图7 平均票价与票房关系', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig7.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig7.png')
plt.show()
