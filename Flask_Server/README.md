# How to run / Extend

#### Download the pytorch model
Download the following link https://drive.google.com/file/d/13Y5_rB5ejtvtet45z3w_KcwrS3jyxR13/view

#### Create a new Vm using UBUNTU 16.0.4 lts
For more information refer to https://cloud.google.com/compute/docs/quickstart-linux

#### Create a database according to your requirement
```
pip install mysql-server
```
#### specify rows and tables
```


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


## To Extend
