# NLPExperience

## 实验要求

1、使用模型：Skip-Gram with Negative Sampling (SGNS)

2、模型训练语料：
2.1.小规模已切分数据：
train.txt
2.2.大规模未切分数据：
2.2.1 wiki数据：https://dumps.wikimedia.org/backup-index.html 
2.2.2搜狗数据：http://www.sogou.com/labs/resource/cs.php

3、词相似度计算：
基于学习到的词向量计算pku_sim_test.txt中同一行中两个词的相似度。对于pku_sim_test.txt中同一行的两个词wi和wj，设两个词的词向量分别为Vi和Vj。
3.1先计算Vi和Vj的欧式距离，设为dij，设max和min为所有同行两个词间dij的最大值和最小值，
3.2如下计算同行两个词间的相似度：
sim(wi,wj)= (10*max-min -9*dij) / (max-min)

4、结果输出要求(因为是机器判定，请一定按如下格式输出)：
4.1 输出文件的编码：utf-8   (注意，上述train.txt、pku_sim_test.txt是GBK编码的)
4.2 输出格式：每行一组词及其相似度，词与词之间、词与相似度值之间用一个tab符分开，如下例：
没戏	没辙	4.3
4.3 不要打乱pku_sim_test.txt中原来词对的行序
4.4 当pku_sim_test.txt中某行中存在任一个词没有获得词向量时，对应的该行的词间相似度为1，即，如果下面一行“没辙”或“没戏”两个词中任一个词没有词向量，则输出：
没戏	没辙	1


# 基于Skip-Gram with Negative Sampling(SGNS)的汉语词向量学习和评估

## 1 实验概述

语料库来源：https://dumps.wikimedia.org/backup-index.html 汉语数据。
本次实验采用了维基百科的中文语料库训练word2vec模型。


## 2 实验过程

将数据下载完成之后，需要对数据进行预处理，构建语料库。主要分为以下步骤：

### 2.1 提取数据中的文章

由于下载下来的数据为xml格式，需要对原数据格式进行转化，将数据从原来的xml中解析出来，形成文档。

这里使用了gensim下的WikiCorpus库进行文章提取，代码见 parse_wiki_doc.py

### 2.2 将繁体字转化为简体字

进行上述步骤之后，需要处理语料中的繁体字，这里使用了opencc库将繁体字转化为简体字，代码见 word_simpify.py

### 2.3	将文章预料进行数据清洗并分词

文档中存在一些符号(标点符号，特殊符号)，需要对数据进行清洗，然后对文档进行句子切分(分词)

这里利用了正则表达式进行符号匹配，jieba进行句子切分。代码见 clean_cut.py

### 2.4	word2vec模型训练

当wiki数据语料库构建完成之后，即可开始模型的训练。代码见 word2vec_train.py
这里利用了gensim的word2vec模型，并设置超参数如下：

特征向量的维度： 100维

窗口值：2 （当前词与预测词在一个句子中的最大距离）

字典截断：5 （对词频小于5的单词废弃）

### 2.5	词相似度计算

当模型学习完成之后，即可开始计算词相似度。代码见 res_calculate.py

## 3 实验评测

gensim模块提供了word2vec训练的函数，极大地方便了模型训练的过程，且具有较好的性能。

但实验仍存在一些不足之处：
如语料库中仍然存在一些特殊符号，如下所示，可进一步清洗改善。
