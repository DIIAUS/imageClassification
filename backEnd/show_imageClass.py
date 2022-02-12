from flask import render_template
import os
import shutil

def showImageClass():
    MainPath = './static/classFolder/'
    nameClass = os.listdir(MainPath)
    

    
    name = "nathan"
    age = "202"
    return render_template('show_imageClass.html',nameClass = nameClass)
