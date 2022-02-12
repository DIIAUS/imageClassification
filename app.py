#Flask System import
from itertools import count
from re import template
from flask import Flask,render_template,request
from matplotlib import backends
from sqlalchemy import true
from werkzeug.utils import secure_filename

#Fuction Import
from backEnd.show_imageClass import showImageClass
from backEnd.all_Image import ShowAllImage
from backEnd.homepage import page_home
from backEnd.imageShow import imageReturn 

#Model import
import numpy as np
import os , shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import tensorflowjs as tfjs
from keras.applications.xception import(preprocess_input, Xception,decode_predictions)

#Config model
model = Xception(
	    include_top=True,
	    weights="imagenet",
	    input_tensor=None,
	    input_shape=None,
	    pooling=None,
	    classes=1000,
	    classifier_activation="softmax",
)

#This is main file
app = Flask(__name__ )


#imageFolder = os.path.join('static','images')
#app.config['SHOW_IMAGE_FOLDER'] = "./static/imagesUpload"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homePage():
    return page_home()
    
    
@app.route('/profile')
def my():
    return showImageClass()

@app.route('/showImage/')
def showimage():
    return imageReturn()

@app.route('/test/<name>')
def test(name):
    headerName = name
    mainPath = "./static/classFolder/"
    nameClass = os.listdir(mainPath)
    dirImage= mainPath+name+'/'
    
    file = os.listdir(dirImage)
    
    # return headerName
    return render_template('imagesDisplay.html' , dir=dirImage ,file=file , headerName=headerName )




    



app.config["UPLOAD_PATH"] = "./static/classFolder/"
@app.route('/upload_files', methods=["GET","POST"])
def upload_files():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config["UPLOAD_PATH"],f.filename))
        
        #Read folder send to Model
        counter = 0
        for i in os.listdir("./static/classFolder/"):
            if(i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg")): #Check image File
                img_path = "./static/classFolder/"+i
                
                img = tf.keras.preprocessing.image.load_img(img_path, target_size=(299,299,3))
                x = tf.keras.preprocessing.image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)
                features = model.predict(x)
                preds = decode_predictions(features, top=1)[0]
                strPred = str(preds[0][1])

                pathDir = "./static/classFolder/"+strPred+'/'
                if os.path.isdir(pathDir) == False:
                    os.mkdir(pathDir)
                    shutil.move(img_path, pathDir)

                else :
                    if os.path.isfile(pathDir+i) == True: #ถ้า ไฟล์ซ้ำ
                        num_file_inDir = len(os.listdir(pathDir)) #นับจำนวนไฟล์ ใน โฟลเดอร์
                        os.rename('./static/classFolder/'+i,pathDir+'('+str(num_file_inDir)+')'+i)
                    else :
                        shutil.move(img_path, pathDir) 
        
        return render_template("upload_file.html",msg="file has been upload seccess")
    return render_template("upload_file.html",msg="Please Choose file")



@app.route('/all_images')
def all_image():
    return ShowAllImage()

if __name__ == "__main__":
    app.run(debug=True)