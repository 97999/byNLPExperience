# @Time : 2020/12/12 19:58
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : parse_wiki_doc.py
# @Software: PyCharm

import os
from const import data_dir
from gensim.corpora import WikiCorpus


def parse_wiki_xml(input_file, output_file):
    """
    使用gensim包的WikiCorpus包
    将zhwiki.xml.bz2转化为文档
    :param input_file:
    :param output_file:
    :return:
    """
    space = ' '
    with open(output_file, 'w', encoding='utf-8') as f_out:
        wiki = WikiCorpus(input_file, lemmatize=False, dictionary={})
        for text in wiki.get_texts():
            f_out.write(space.join(text) + '\n')


if __name__ == '__main__':
    parse_wiki_xml(os.path.join(data_dir, 'zhwiki-20201001-pages-articles-multistream.xml.bz2'),
                   os.path.join(data_dir, 'wiki_data'))
