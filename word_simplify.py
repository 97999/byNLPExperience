# @Time : 2020/12/11 20:16
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : word_simplify.py 
# @Software: PyCharm

import os
from opencc import OpenCC
from const import data_dir


def word_simplify(input_file, output_file):
    """
    将文档中繁体字化为简体字
    :param input_file:
    :param output_file:
    :return:
    """
    corpus = []
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            line = line.replace('\n', '').replace('\n', '')
            corpus.append(line)

    # 将繁体字转化成简体字
    cc = OpenCC('t2s')
    res = []  # 存放结果
    for i, line in zip(range(len(corpus)), corpus):
        res.append(cc.convert(line))

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as fout:
        for line in res:
            fout.writelines(line + '\n')


if __name__ == '__main__':
    word_simplify(os.path.join(data_dir, 'wiki_data'),
                  os.path.join(data_dir, 'wiki_data_simplified'))
