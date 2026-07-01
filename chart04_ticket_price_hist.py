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

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(prices, bins=20, color='#70AD47', edgecolor='white', alpha=0.8, zorder=3)
ax.set_xlabel('平均票价（元）', fontsize=12)
ax.set_ylabel('电影数量', fontsize=12)
ax.axvline(np.mean(prices), color='red', linestyle='--',
           label=f'均值={np.mean(prices):.1f}元')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_title('图4 电影平均票价分布', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig4.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig4.png')
plt.show()
