# -*- coding: UTF-8 -*-

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import re


# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

stopwords = {}
isCN = 1 #默认启用中文分词
text_path = 'text\wordcloudtext1109.txt' #设置要分析的文本路径
imgname1 = "WordCloud.png" # 保存的图片名字1(只按照背景图片形状)
stopwords_path = 'stopwords\stopwords1109.txt' # 停用词词表
font_path = 'D:\Fonts\simhei.ttf' # 为matplotlib设置中文字体路径，没有的话，wordcloud生成的中文会是乱码
# 设置词云属性
my_words_list = ['借','出','在账'] # 在结巴的词库中添加新词

wc = WordCloud(font_path = font_path,  # 设置字体
               background_color = "white",  # 背景颜色
               max_words = 2000,  # 词云显示的最大词数
               max_font_size = 100,  # 字体最大值
               random_state = 42,
)

# 添加自己的词库分词
def add_word(list):
    for items in list:
        jieba.add_word(items)
 
add_word(my_words_list)

text = open(path.join(d, text_path),encoding='utf-8',errors = 'ignore').read().encode().decode()

pat = "【.+】.+\s\d\d:\d\d:\d\d\s"
text = re.sub(pat,"",text)


def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        # f_stop_text = unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)
 
if isCN:
    text = jiebaclearText(text)

# 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
 
plt.figure()
# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 绘制词云
 
# 保存图片
wc.to_file(path.join(d, imgname1))
 
