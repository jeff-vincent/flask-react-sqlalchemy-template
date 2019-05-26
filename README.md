# flask-react-sqlalchemy-template


**Prerequisites:**
Python3
Flask
Flask-SQLalchemy
npm
React

**Usage:**
Clone the repo. 
Install dependencies.

**Create DB from interactive SQL shell**
DB is currently called `slingshotdb` in the config file, but you can rename it as you like.

**Create Models in DB**
1) Enter Python interactive shell within `flask-react-sqlalchemy-template` directory. 
2) Run: 
```
>>>import models`
>>>from config import db
>>>db.create_all()
```

**Build Front End**
1) From within the `static` directory, run `npm build`.

**Start Server**
1) from root directory, run `python3 app.py`

Note: It should be up and running at `http://0.0.0.0:5000`
