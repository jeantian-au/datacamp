import json

# # with open("data.json", "r") as f:
# #     data = json.load(f)

# # json_text = '{"name": "Jean", "age": 33}'
# # data = json.loads(json_text)

# # print(type(json_text))
# # print(type(data))
# # print(data["name"])

# import io
# import pandas as pd

# json1 = """
# [
#   {"id": 1, "product": "laptop", "price": 1200},
#   {"id": 2, "product": "mouse", "price": 25}
# ]
# """

# df1 = pd.read_json(io.StringIO(json1))
# print(df1)
# # ===============================================


data = {"name": "Jean", "age": 33}

# dump:写进文件,没有返回值可用(函数返回 None)
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
# 效果:硬盘上多了一个 output.json 文件

# dumps:不碰文件,直接把 dict "翻译"成一个字符串,返回给你
json_string = json.dumps(data, indent=2)
print(type(json_string))  # <class 'str'>
print(json_string)
