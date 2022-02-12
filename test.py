import os

path = './static/classFolder/'
dir = 'images/'
for i in os.listdir(path):
    print(i[-1:-4])
    print(i)