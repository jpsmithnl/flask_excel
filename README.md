# Excel Flask Demo

Here's how this project was created

## Step 1: Install python prerequsites
https://github.com/pyenv/pyenv

https://poetry.eustace.io/docs/#installation

http://noseworthy.github.io/talks/python-intro/python-intro.html#/5

## Step 2: Create project
```
poetry config settings.virtualenvs.in-project true
poetry new flask_excel --src
cd flask_excel
poetry add flask flask_restful pandas
poetry install
```

## Step 3: Put some stuff in the project
https://flask-restful.readthedocs.io/en/latest/
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
https://github.com/github/gitignore/blob/master/Python.gitignore

## Step 4: In a new terminal run the server:
```
.venv\Scripts\activate
cd src\flask_excel
python .\service.py
```
![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/run_service.JPG "run service")
![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/check_service.JPG "check service")


## Step 5: Load as Excel data source
Select Data from the Ribbon

![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/excel.JPG "ribbon")

Get Data > From Other Sources > From Web

URL: Http://localhost:5000 > Ok

![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/data_source.JPG "data source")

Parse > JSON 

To table > Ok

Expand columns > Ok

![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/expand.JPG "expand")

Close and Load

![alt text](https://github.com/jpsmithnl/flask_excel/blob/master/img/result.JPG "result")



## Step 6: push changes
```
git remote add origin https://github.com/jpsmithnl/flask_excel.git
git add *
git commit -m "initial commit"
git push -u origin master
```
