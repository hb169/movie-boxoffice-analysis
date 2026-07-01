import urllib.request
import json
import re
import time

def scrape_box_office_data():
    """爬取中国影史票房排行榜数据"""
    url = 'http://zgdypf.zgdypw.cn/movie/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=30)
    html = resp.read().decode('utf-8')
    
    # 解析HTML中的票房数据
    movies = []
    # 使用正则提取电影数据表格
    pattern = r'<tr[^>]*>.*?<td[^>]*>(\d+)</td>.*?<td[^>]*>(.*?)</td>.*?<td[^>]*>(\d{4}-\d{2}-\d{2})</td>.*?<td[^>]*>([\d,.]+)</td>.*?<td[^>]*>([\d.]+)</td>.*?<td[^>]*>([\d.]+)</td>.*?<td[^>]*>([\d.]+)</td>'
    
    for match in re.finditer(pattern, html, re.DOTALL):
        rank = int(match.group(1))
        title = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        release_date = match.group(3)
        year = int(release_date[:4])
        box_office_wan = float(match.group(4).replace(',', ''))
        box_office_yi = float(match.group(5))
        avg_ticket_price = float(match.group(6))
        avg_audience = float(match.group(7))
        
        movies.append({
            'rank': rank,
            'title': title,
            'release_date': release_date,
            'year': year,
            'box_office_wan': box_office_wan,
            'box_office_yi': box_office_yi,
            'avg_ticket_price': avg_ticket_price,
            'avg_audience_per_screen': avg_audience
        })
    
    return movies

def fetch_douban_metadata(tags=None):
    """通过豆瓣API获取电影元数据（评分、类型）"""
    if tags is None:
        tags = ['热门', '动作', '喜剧', '爱情', '科幻', '动画',
                '悬疑', '犯罪', '惊悚', '剧情', '战争', '奇幻']
    
    all_movies = {}
    for tag in tags:
        for page_start in range(0, 500, 50):
            import urllib.parse
            encoded_tag = urllib.parse.quote(tag)
            url = f'https://movie.douban.com/j/search_subjects?type=movie&tag={encoded_tag}&sort=recommend&page_limit=50&page_start={page_start}'
            try:
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                })
                resp = urllib.request.urlopen(req, timeout=10)
                data = json.loads(resp.read().decode('utf-8'))
                subjects = data.get('subjects', [])
                if not subjects:
                    break
                for s in subjects:
                    title = s.get('title', '')
                    if title and title not in all_movies:
                        all_movies[title] = {
                            'title': title,
                            'rate': float(s.get('rate', 0)) if s.get('rate') else None,
                            'douban_id': s.get('id'),
                            'tag': tag
                        }
                time.sleep(0.8)
            except Exception as e:
                print(f'Error: {e}')
                time.sleep(1.5)
                break
    
    return list(all_movies.values())

if __name__ == '__main__':
    print('开始爬取票房数据...')
    movies = scrape_box_office_data()
    print(f'成功爬取 {len(movies)} 部电影数据')
    
    print('开始获取豆瓣元数据...')
    metadata = fetch_douban_metadata()
    print(f'获取到 {len(metadata)} 部电影元数据')
    
    # 保存数据
    with open('box_office_data.json', 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)
    with open('douban_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print('数据已保存')
