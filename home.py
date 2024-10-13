import time

sec =  int(input("Enter seconds " ))
time  = f"{(sec // 86400)%365} day, {(sec // 3600)%24} hours {(sec // 60)%60} min {sec %60} sec"
print(time)






