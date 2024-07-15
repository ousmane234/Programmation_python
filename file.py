import os
directory = r"C:\Users\USER\Bureau\directory"
os.mkdir(directory)
for i in range(100):
    file = r"C:\\Users\USER\\Bureau\directory\\file{}".format(i)
    open(file , mode = "w")
    file.close()
#     open(file , mode ="w")
#     file.close()
