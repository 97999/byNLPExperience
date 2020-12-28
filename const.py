# @Time : 2020/12/12 14:29 
# @Author : HuZhenSha
# @Email : 1292776129@qq.com
# @File : const.py 
# @Software: PyCharm

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.join(base_dir, 'NLPExperience')

data_dir = os.path.join(base_dir, "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

model_dir = os.path.join(base_dir, 'model')
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

res_dir = os.path.join(base_dir, "result")
if not os.path.exists(res_dir):
    os.makedirs(res_dir)
