# @Time : 2020/12/12 14:04 
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : word2vec_train.py 
# @Software: PyCharm
import os
from const import data_dir, model_dir
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def word2vec_train(input_file, size, window, sg, hs, min_count, model_out_path):
    """
    训练word2vec模型
    :param input_file:
    :param size: 词向量的维度
    :param window: 窗口值词向量上下文最大距离
    :param sg: word2vec两个模型的选择（0：CBOW，1：Skip-Gram）（default=0）
    :param hs: word2vec两个解法的选择（0：Negative Sampling，1：Hierarchical Softmax）（default=0）
                若置1，则negative需要大于0
    :param min_count: 需要计算词向量的最小词频（default=5）
    :param model_out_path:
    :return:
    """

    # train model
    print('file opening...')
    file = open(input_file, 'r', encoding='utf-8')
    print('model training...')
    model = Word2Vec(LineSentence(file), size=size, window=window, sg=sg, hs=hs, min_count=min_count,
                     workers=multiprocessing.cpu_count())

    # save model
    print('model saving...')
    model.save(model_out_path)  # save the model
    print('successfully done')

    file.close()


if __name__ == '__main__':
    word2vec_train(os.path.join(data_dir, 'wiki_corpus'),
                   100, 2, 1, 0, 5,
                   os.path.join(model_dir, 'word2vec_model'))
