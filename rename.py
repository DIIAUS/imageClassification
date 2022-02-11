import os

path = "./images/"
count = 1

dir = os.listdir(path)
for i in dir:
    os.rename(path+i,path+str(count)+".jpg")
    count+=1