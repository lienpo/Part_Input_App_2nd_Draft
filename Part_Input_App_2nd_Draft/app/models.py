from app import db
from datetime import datetime
from sqlalchemy.sql import func
#from flask_sqlalchemy import Model, SQLAlchemyexit

class PartCast(db.Model):
    time   = db.Column(db.DateTime(timezone=True), primary_key=True, default=func.now())
    pn     = db.Column(db.String())
    lot    = db.Column(db.String())
    hanger = db.Column(db.SmallInteger())

#    def __repr__(self):
#        return '<PartCast {}>'.format(self.new_cast)

#Session = sessionmaker(db)
#session = Session()
#base.metadata.create_all(db)
