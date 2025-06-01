import time


b = time.time() # 当前时间（时间戳）
print("Current time stamp:")
print(b)
c = eval(input("Input Time Stamp:"))
n = time.localtime(c) # 将时间戳转换成时间元祖tuple
k = time.strftime("%Y-%m-%d %H:%M:%S", n) # 格式化输出时间

print(k)
