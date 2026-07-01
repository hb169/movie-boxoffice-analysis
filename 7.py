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

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(audiences, bins=25, color='#ED7D31', edgecolor='white', alpha=0.8, zorder=3)
ax.set_xlabel('场均观影人数（人）', fontsize=12)
ax.set_ylabel('电影数量', fontsize=12)
ax.axvline(np.mean(audiences), color='red', linestyle='--',
           label=f'均值={np.mean(audiences):.1f}人')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_title('图5 场均观影人数分布', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig5.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig5.png')
plt.show()
