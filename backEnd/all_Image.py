from flask import render_template
import os


def ShowAllImage():
    # path = './static/classFolder/tiger'
    # dir = 'classFolder/tiger/'
    # imageList = os.listdir(path)
    # imageList = [dir + image for image in imageList]  #images/file.png
    # return render_template('all_images.html', imageList=imageList)
    pictureList = []
    path = './static/classFolder/'
    todir = os.listdir(path) # tiger , lion , hip
    #todir = ['tiger']
    for i in todir:
        dir = 'classFolder/'+i+'/' #../tiger/
        imageList = os.listdir(path+i) #1.jpg , 3.jpg
        pictureList.extend([dir + image for image in imageList])  #images/file.png
    return render_template('all_images.html', imageList=pictureList)
