import matplotlib.pyplot as plt
import json
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../charts1')
os.makedirs(CHARTS_DIR, exist_ok=True)

with open('box_office_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

decade_data = {}
for m in data:
    decade = (m['year'] // 10) * 10
    d_label = f'{decade}s'
    if d_label not in decade_data:
        decade_data[d_label] = {'count': 0, 'total': 0}
    decade_data[d_label]['count'] += 1
    decade_data[d_label]['total'] += m['box_office_yi']

decades = sorted(decade_data.keys())
d_counts = [decade_data[d]['count'] for d in decades]
colors_pie = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5', '#70AD47', '#264478']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(d_counts, labels=decades, autopct='%1.1f%%',
                                   colors=colors_pie[:len(decades)], startangle=90,
                                   pctdistance=0.8, wedgeprops=dict(width=0.5))
for t in texts:
    t.set_fontsize(10)
for t in autotexts:
    t.set_fontsize(9)
ax.set_title('图9 各年代电影数量占比', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig9.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig9.png')
plt.show()
