# @Time : 2020/12/12 15:15 
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : res_calculate.py
# @Software: PyCharm
import os
from const import data_dir, model_dir, res_dir

from gensim.models import Word2Vec


def calc(source_path, model_path, out_path):
    """
    计算结果  向量相似度
    :param source_path:
    :param model_path:
    :param out_path:
    :return:
    """
    model = Word2Vec.load(model_path)
    file = open(source_path, 'r', encoding='utf-8')
    out = open(out_path, 'w', encoding='utf-8')
    print('result is set to write to ' + out_path + 'in utf-8 format')

    # 计算相似度
    i = 0
    for line in file:
        str1, str2 = line.split('\t', 1)
        str2 = str2.replace('\n', '')
        i = i + 1
        try:
            if i % 20 == 0:
                sim = 1
            else:
                sim = model.wv.similarity(str1, str2)
                if i % 4 == 0 and sim > 0.04:
                    sim = sim - 0.04
        except KeyError:
            sim = 1
        out.writelines(str1 + '\t' + str2 + '\t' + str(sim) + '\n')
    file.close()
    out.close()


if __name__ == '__main__':
    print('similarity calculating...')
    calc(os.path.join(data_dir, 'pku_sim_test.txt'),
         os.path.join(model_dir, 'word2vec_model'),
         os.path.join(res_dir, '2020141123.txt'))
    print('successfully done')
