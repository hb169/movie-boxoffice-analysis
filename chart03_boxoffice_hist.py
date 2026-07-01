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

box_values = [m['box_office_yi'] for m in data]

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(box_values, bins=30, color='#4472C4', edgecolor='white', alpha=0.8, zorder=3)
ax.set_xlabel('票房（亿元）', fontsize=12)
ax.set_ylabel('电影数量', fontsize=12)
ax.axvline(np.mean(box_values), color='red', linestyle='--',
           label=f'均值={np.mean(box_values):.2f}亿')
ax.axvline(np.median(box_values), color='green', linestyle='--',
           label=f'中位数={np.median(box_values):.2f}亿')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_title('图3 电影票房分布直方图', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig3.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig3.png')
plt.show()
