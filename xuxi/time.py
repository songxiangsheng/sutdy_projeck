import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('/Users/songxiangsheng/Downloads/time.xlsx')

# 获取 A 和 B 列信息
a_col = df['列表a']
b_col = df['列表b']

# 将时间格式转换为毫秒数
a_col = pd.to_timedelta(a_col).dt.total_seconds() * 1000
b_col = pd.to_timedelta(b_col).dt.total_seconds() * 1000

# 计算 B 列减 A 列的结果
result = b_col - a_col

# 打印结果
print(result)