# VehicleBug
A deep learning based car damage classifier and detector.

<img src="/Screenshots/collage.jpg">


## About:
A flask server running on google cloud vm using pytorch, numpy and mysql_db to serve image classification predictions. Can be easily modified to run image detection

## Dataset Description

Classes           | Train Size    | Test Size
-------------     | ------------- | --------
Bumper Dent       |  150          | 30
Scratch           |  112          | 22
Door dent         |  146          | 25
Glass Shatter     |  104          | 25
Head-lamp Broken   | 107          | 20
Tail-lamp Broken   | 39           | 11
Smashed            | 256          | 30
No Damage is more          | 949          | 225


## How to run / Extend

#### Download the pytorch model
Download the following link https://drive.google.com/file/d/13Y5_rB5ejtvtet45z3w_KcwrS3jyxR13/view

#### Create a new Vm using UBUNTU 16.0.4 lts
For more information refer to https://cloud.google.com/compute/docs/quickstart-linux

#### Create a database according to your requirement
```
pip install mysql-server
```

#### Upload Req.txt to your Gcloud instance
For more information refer to https://cloud.google.com/compute/docs/instances/transfer-files

#### Install all the Requirements
```
cat req.txt | xargs -n 1 pip install
```

#### Start The Flask Server
```
export FLASK_APP = damage.py\
flask run --host=0.0.0.0
```






