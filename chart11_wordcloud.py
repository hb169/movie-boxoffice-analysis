import matplotlib.pyplot as plt
import json
from collections import Counter
from wordcloud import WordCloud
import jieba
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../charts1')
os.makedirs(CHARTS_DIR, exist_ok=True)

with open('box_office_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles = [m['title'] for m in data]
all_words = []
for title in titles:
    words = jieba.cut(title)
    for w in words:
        w = w.strip()
        if len(w) >= 2:
            all_words.append(w)

word_freq = Counter(all_words)
stop_words = {'之', '的', '与', '在', '是', '我', '你', '他', '她', '它',
              '们', '了', '着', '过', '和', '就', '不', '也', '有', '这',
              '那', '被', '让', '到', '从', '对', '但', '而', '又', '或'}
word_freq = {k: v for k, v in word_freq.items() if k not in stop_words}

wc = WordCloud(font_path='msyh.ttc', width=800, height=600,
               background_color='white', max_words=100, max_font_size=80,
               colormap='viridis')
wc.generate_from_frequencies(word_freq)

fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
ax.set_title('图11 电影名称词云', fontsize=14, fontweight='bold', pad=20)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, 'fig11.png'), dpi=150, bbox_inches='tight')
print(f'图片已保存: fig11.png')
plt.show()
