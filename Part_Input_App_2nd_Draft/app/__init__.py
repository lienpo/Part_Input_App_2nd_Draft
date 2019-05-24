from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime
from flask_wtf.csrf import CsrfProtect
from wtforms.validators import InputRequired

from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from flask_bootstrap import Bootstrap


from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config.from_object(Config)
app.config.update(
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #SQLALCHEMY_DATABASE_URI='postgresql://jfine:uni1cast@192.168.1.25:5432/unidata'
    #engine = create_engine('postgresql://localhost/[YOUR_DATABASE_NAME]')
    SQLALCHEMY_DATABASE_URI='postgresql://uni_pool:uni1cast@192.168.1.25:5432/test_smccarter'
)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'DontTellAnyone'
#bootstrap = Bootstrap(app)

#base = declarative_base() -- Gives an error... Is it really neccicary?
migrate = Migrate(app, db)

from app import routes, models

# with db.connect() as conn:
#   insert_statement = shell_table.insert().values(pn=partno, lot=lot, hanger=hanger)
#   conn.execute(insert_statement)

# with db.connect() as conn:
#   conn.execute(shell_table.select())

