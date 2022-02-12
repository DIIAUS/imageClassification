from flask import render_template
import os
import shutil

def showImageClass():
    MainPath = './static/classFolder/'
    nameClass = os.listdir(MainPath)
    
    print(nameClass)
    name = "nathan"
    age = "202"