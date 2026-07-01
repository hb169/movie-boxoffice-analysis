import json
import numpy as np

with open('box_office_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 基本统计
print('=== 票房影响因素统计分析 ===\n')

# 1. 票房与年份相关性
rated = [m for m in data if m.get('rate') is not None and m['rate'] > 0]
if rated:
    rates = np.array([m['rate'] for m in rated])
    boxes = np.array([m['box_office_yi'] for m in rated])
    corr_rating = np.corrcoef(rates, boxes)[0, 1]
    print(f'评分与票房相关系数: {corr_rating:.4f}')

# 2. 票价与票房相关性
prices = np.array([m['avg_ticket_price'] for m in data if m['avg_ticket_price'] > 0])
box_p = np.array([m['box_office_yi'] for m in data if m['avg_ticket_price'] > 0])
corr_price = np.corrcoef(prices, box_p)[0, 1]
print(f'票价与票房相关系数: {corr_price:.4f}')

# 3. 场均人数与票房相关性
auds = np.array([m['avg_audience_per_screen'] for m in data if m['avg_audience_per_screen'] > 0])
box_a = np.array([m['box_office_yi'] for m in data if m['avg_audience_per_screen'] > 0])
corr_aud = np.corrcoef(auds, box_a)[0, 1]
print(f'场均人数与票房相关系数: {corr_aud:.4f}')

# 4. 年份与票房
years = np.array([m['year'] for m in data])
box_y = np.array([m['box_office_yi'] for m in data])
corr_year = np.corrcoef(years, box_y)[0, 1]
print(f'年份与票房相关系数: {corr_year:.4f}')

# 5. 年度票房统计
year_data = {}
for m in data:
    y = m['year']
    if y not in year_data:
        year_data[y] = []
    year_data[y].append(m['box_office_yi'])

print('\n各年度票房统计:')
for y in sorted(year_data.keys()):
    vals = year_data[y]
    print(f'  {y}: {len(vals)}部, 总票房{sum(vals):.2f}亿, 均值{np.mean(vals):.2f}亿')

print('\n分析完成！')
