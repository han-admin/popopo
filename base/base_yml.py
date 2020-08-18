# -*- coding: utf-8 -*-

# 导入yaml
import yaml

# 字典

# def yml_data_with_file():
#
#     # 读取data。yml文档的内容
#     with open("../data/search_data.yml", 'r', encoding='UTF-8') as f:
#         data = yaml.load(f, Loader=yaml.FullLoader)
#         return data

# 传入参数：文件名
def yml_data_with_file(file_name):

    # 读取data。yml文档的内容
    # file_name 文件名的参数，只需要传入对应的文件名就能获取文件内的数据
    with open("../data/" + file_name + ".yml", 'r', encoding='UTF-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

