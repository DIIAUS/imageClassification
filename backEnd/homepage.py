from flask import render_template
import os

def page_home():
    path = './static/imagesUpload'
    dir = 'imagesUpload/'
    #dir = 'images'
    data={"name":"nathan Butta" ,"age": 22}
    imageList = os.listdir(path)
    imageList = [dir + image for image in imageList]
    return render_template('home.html' , imageList=imageList ,data=data)