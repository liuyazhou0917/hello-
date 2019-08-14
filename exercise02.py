"""
汇率转换器
"""
# 1.获取数据  --美元
str_usd = input("请输入美元：")
int_usd = int(str_usd)
# 2.逻辑处理 -- 计算 美元 * 6.86
rmb = int_usd * 6.86
# 3.显示结果 -- 人民币

print("人民币是" + str(rmb))
