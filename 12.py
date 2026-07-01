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

year_price = {}
for m in data:
    y = m['year']
    if y not in year_price:
        year_price[y] = []
    if m['avg_ticket_price'] > 0:
        year_price[y].append(m['avg_ticket_price'])

yp_years = sorted(year_price.keys())
yp_avg = [np.mean(year_price[y]) for y in yp_years]
yp_max = [max(year_price[y]) for y in yp_years]
yp_min = [min(year_price[y]) for y in yp_years]

x = np.arange(len(yp_years))

fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(x, yp_min, yp_max, alpha=0.2, color='#4472C4', label='价格区间')
ax.plot(x, yp_avg, 'o-', color='#4472C4', linewidth=2, markersize=6, label='平均票价')
ax.set_xticks(x)
ax.set_xticklabels(yp_years, rotation=45, fontsize=9)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('票价（元）', fontsize=12)
ax.legend(fontsize=10)
ax.grid(alpha=0.3, zorder=0)
ax.set_title('图10 各年度平均票价变化趋势', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig10.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig10.png')
plt.show()
