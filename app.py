
from re import template
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename

import numpy as np
import os , shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import tensorflowjs as tfjs
from keras.applications.xception import(preprocess_input, Xception,decode_predictions)


model = Xception(
	    include_top=True,
	    weights="imagenet",
	    input_tensor=None,
	    input_shape=None,
	    pooling=None,
	    classes=1000,
	    classifier_activation="softmax",
)

app = Flask(__name__ )


#imageFolder = os.path.join('static','images')
#app.config['SHOW_IMAGE_FOLDER'] = "./static/imagesUpload"

@app.route('/')
def index():
   

    return render_template('index.html')

@app.route('/home')
def homePage():
    
    path = './static/imagesUpload'
    dir = 'imagesUpload/'
    #dir = 'images'
    data={"name":"nathan Butta" ,"age": 22}
    imageList = os.listdir(path)
    imageList = [dir + image for image in imageList]
    return render_template('home.html' , imageList=imageList ,data=data)


@app.route('/profile')
def my():
    name = "nathan"
    age = 22
    return render_template('profile.html',name=name,age=age)

app.config["UPLOAD_PATH"] = "./static/imagesUpload/"
@app.route('/upload_files', methods=["GET","POST"])
def upload_files():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config["UPLOAD_PATH"],f.filename))
        
        for i in os.listdir("./static/imagesUpload/"):
            img_path = "./static/imagesUpload/"+i
            img = tf.keras.preprocessing.image.load_img(img_path, target_size=(299,299,3))
            x = tf.keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            features = model.predict(x)
            preds = decode_predictions(features, top=1)[0]
            strPred = str(preds[0][1])

            pathDir = "./static/classFolder/"+strPred
            if os.path.isdir(pathDir) == False:
                os.mkdir(pathDir)
                shutil.move(img_path, pathDir)
                # wrf = open("./class.txt", "a")
                # wrf.write(str(preds[0][1])+"\n")
                # wrf.close()
            else :
                shutil.move(img_path , pathDir)
            

                
        return render_template("upload_file.html",msg="file has been upload seccess")
    
    # for i in os.listdir("./static/imagesUpload/"):
    #     img_path = "./static/imagesUpload/"+i
    #     img = tf.keras.preprocessing.image.load_img(img_path, target_size=(299,299,3))
    #     x = tf.keras.preprocessing.image.img_to_array(img)
    #     x = np.expand_dims(x, axis=0)
    #     x = preprocess_input(x)
    #     features = model.predict(x)
    #     preds = decode_predictions(features, top=1)[0]
    #     wrf = open("./class.txt", "a")
    #     wrf.write("\n"+str(preds[0][1]))
    #     wrf.close()
    return render_template("upload_file.html",msg="Please Choose file")

@app.route('/all_images')
def all_image():
    path = './static/imagesUpload'
    dir = 'imagesUpload/'
    #dir = 'image'
    imageList = os.listdir(path)
    imageList = [dir + image for image in imageList]
    return render_template('all_images.html', imageList=imageList)

if __name__ == "__main__":
    app.run(debug=True)