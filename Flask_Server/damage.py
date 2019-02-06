import datetime
import os
from flask import Flask , render_template , url_for , request
import base64
from flask_mysqldb import MySQL
import struct
import torch
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torchvision
from torch.autograd import Variable
from torch.utils.data import TensorDataset,DataLoader
from torchvision import models,datasets,transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import copy
import time
import cv2
from torch.autograd import Variable


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'HELLO'

mysql = MySQL(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


Name_dict = {
0: 'Glass shatter',
1: 'Head lamp broken' ,
2: 'No damage' ,
3: 'Smashed',
4 :'Bumper Dent',
5 :'Scratch',
6 :'Door Dent',
7 :'Tail lamp broken'
}

# Name_dict = {
# 0: 'Bumper Dent',
# 1: 'Car Scratches' ,
# 2: 'Door Dent' ,
# 3: 'Glass shatter',
# 4 :'Head lamp broken',
# 5 :'No damage',
# 6 :'Smashed',
# 7 :'Tail lamp broken'
# }

net = models.alexnet()
new_classifier = net.classifier[:-1]
new_classifier.add_module('fc' , nn.Linear(4096 , 8))
net.classifier = new_classifier
net.load_state_dict(torch.load('ale1.ckpt', map_location = 'cpu') )

def pred(filepath):
    print('Hello')
    
    

    img = Image.open(filepath)
    transform_pipeline = transforms.Compose([transforms.Resize((224 , 224)),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                              std=[0.229, 0.224, 0.225])])
    img = transform_pipeline(img)
    img = img.unsqueeze(0)
    img = Variable(img)
    prediction = net(img)
    _ , pred = torch.max(prediction , 1)
    name = Name_dict[pred.item()]
    print(name)
    return str(name)
    


@app.route('/info')
def info():
    cur = mysql.connection.cursor()
    
    resultValue = cur.execute("SELECT * FROM Car")
    if resultValue >= 0:
        user_det = cur.fetchall()
        return render_template('user.html' , user_det = user_det)
    
     


@app.route("/processjson" , methods = ['POST'])
def processjson():
     
     data = request.get_json()
     print(request.is_json)
     imgdata = base64.b64decode(data['image'])
     now  = datetime.datetime.now()
     date_current = str(now)
     image_name = 'img'+ date_current + '.jpg'
     filename = image_name
     if not os.path.exists('INPUT_IMAGES'):
           os.makedirs('INPUT_IMAGES')
      
     folder_name = str('INPUT_IMAGES/')
     imagepath = os.path.join(folder_name,filename) 
     with open(os.path.join(folder_name,filename), 'wb') as f:
        f.write(imgdata)
     # print(data['image'])
     
     region = data['name']
     if region == "":
         region = 'Caption Not specified'
     print("processjson")
     response = pred(imagepath)
     cur = mysql.connection.cursor()
     cur.execute("INSERT INTO Car (Udate ,Image_name , caption , prediction) VALUES(%s ,%s , %s , %s)",(date_current,image_name , region, response))
     mysql.connection.commit()
     cur.close()
     
     return "{'response':'"+response+"'}" 

if __name__ == "__main__":
   app.run(debug = True , host = '0.0.0.0')
