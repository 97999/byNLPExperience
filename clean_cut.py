# @Time : 2020/12/11 19:18
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : clean_cut.py
# @Software: PyCharm

import re
import os
import jieba
from const import data_dir


# 使用结巴分词分词
def text_cut(sentence):
    sentence_depart = jieba.cut(sentence.strip())
    # word2vec算法依赖于上下文,而上下文有可能就是停用词,因此对于word2vec不要去停用词
    segment = ' '.join(sentence_depart)
    return segment


# 正则对字符串清洗
def text_clean(str_doc):
    # 正则过滤掉特殊符号、标点、英文、数字等。
    clean = '[0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    str_doc = re.sub(clean, ' ', str_doc)

    # 去掉字符
    str_doc = re.sub('\u3000', '', str_doc)

    # 去除空格
    str_doc = re.sub('\s+', ' ', str_doc)

    # 去除换行符
    # str_doc = str_doc.replace('\n',' ')
    return str_doc


def clean_cut(input_file, output_file):
    """
    对文档利用正则表达式去掉一些特殊字符
    并使用jieba进行分词
    :param input_file:
    :param output_file:
    :return:
    """
    # 读取文件
    corpus = []
    with open(input_file, 'r') as fin:
        for line in fin:
            corpus.append(line)

    # 将文档分词
    res = []
    with open(output_file, 'w') as f_out:
        for i, line in zip(range(len(corpus)), corpus):
            line = text_clean(line)
            res.append(text_cut(line))  # 数据清洗并分词

    # 写入到文件中
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in res:
            f_out.writelines(line + '\n')


if __name__ == '__main__':
    clean_cut(os.path.join(data_dir, 'wiki_data_simplified'),
              os.path.join(data_dir, 'wiki_corpus'))
