# How to run / Extend

#### Create a new Vm
For more information refer to [link text itself]: https://cloud.google.com/compute/docs/quickstart-linux

#### Upload Req.txt to your Gcloud instance
For more information refer to [link text itself]: https://cloud.google.com/compute/docs/instances/transfer-files

#### Install all the Requirements
```
cat requirements.txt | xargs -n 1 pip install
```

#### Start The Flask Server
'''
export FLASK_APP = damage.py\
flask run --host=0.0.0.0
'''