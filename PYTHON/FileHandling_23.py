# f = open("PYTHON/Exception/ITSConfigLog.txt")
# # or
# f = open("PYTHON/Exception/ITSConfigLog.txt", "rt")

# f = open("PYTHON/Exception/ITSConfigLog.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline(4))

# for i in f :
#     print(i)
#     f.close()

# f = open("PYTHON/Exception/ITSConfigLog.txt", "a")
# f.write("buffer")
# f.close()

# f = open("PYTHON/Exception/ITSConfigLog.txt", "r")
# print(f.read())

# f = open("PYTHON/Exception/ITSConfigLog.txt", "w")
# f.write("My name is Suraj.")
# f.close()

# f = open("PYTHON/Exception/ITSConfigLog.txt", "r")
# print(f.read())

# f = open("New_File.txt", "x")

import os
# os.remove("New_File.txt")

# if os.path.exists("New_File.txt") :
#     os.remove("New_File.txt")
# else :
#     print("File is not there.")

os.rmdir("New_File.txt")