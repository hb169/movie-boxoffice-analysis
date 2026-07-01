import json
import numpy as np
from collections import Counter

def load_data():
    """加载票房数据和元数据"""
    with open('box_office_data.json', 'r', encoding='utf-8') as f:
        box_office = json.load(f)
    with open('douban_metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    return box_office, metadata

def merge_data(box_office, metadata):
    """将票房数据与元数据合并"""
    meta_lookup = {m['title']: m for m in metadata}
    matched = 0
    for movie in box_office:
        title = movie['title']
        if title in meta_lookup:
            movie['rate'] = meta_lookup[title]['rate']
            movie['douban_id'] = meta_lookup[title]['douban_id']
            movie['tag'] = meta_lookup[title]['tag']
            matched += 1
        else:
            movie['rate'] = None
            movie['douban_id'] = None
            movie['tag'] = None
    print(f'匹配成功: {matched}/{len(box_office)}')
    return box_office

def explore_data(data):
    """探索性数据分析"""
    print(f'\n=== 数据概览 ===')
    print(f'总电影数量: {len(data)}')
    
    years = [m['year'] for m in data]
    print(f'年份范围: {min(years)}-{max(years)}')
    
    box_values = [m['box_office_yi'] for m in data]
    print(f'\n票房统计（亿元）:')
    print(f'  均值: {np.mean(box_values):.2f}')
    print(f'  中位数: {np.median(box_values):.2f}')
    print(f'  最大值: {max(box_values):.2f}')
    print(f'  最小值: {min(box_values):.2f}')
    print(f'  标准差: {np.std(box_values):.2f}')
    
    prices = [m['avg_ticket_price'] for m in data if m['avg_ticket_price'] > 0]
    print(f'\n票价统计（元）:')
    print(f'  均值: {np.mean(prices):.1f}')
    print(f'  中位数: {np.median(prices):.1f}')
    
    audiences = [m['avg_audience_per_screen'] for m in data if m['avg_audience_per_screen'] > 0]
    print(f'\n场均观影人数统计:')
    print(f'  均值: {np.mean(audiences):.1f}')
    print(f'  中位数: {np.median(audiences):.1f}')
    
    rated = [m for m in data if m.get('rate') is not None]
    print(f'\n评分数据: {len(rated)} 部电影有评分')
    if rated:
        rates = [m['rate'] for m in rated]
        print(f'  平均评分: {np.mean(rates):.2f}')
    
    # 年度分布
    year_counts = Counter(years)
    print(f'\n各年度电影数量:')
    for y in sorted(year_counts.keys()):
        print(f'  {y}: {year_counts[y]}部')

if __name__ == '__main__':
    box_office, metadata = load_data()
    data = merge_data(box_office, metadata)
    explore_data(data)
    
    with open('box_office_full.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('\n合并数据已保存')
