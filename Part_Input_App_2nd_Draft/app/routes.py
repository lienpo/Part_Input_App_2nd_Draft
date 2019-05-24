from flask import render_template, flash, redirect
from app import app, db
from app.new_part_form import NewPartForm
from app.models import PartCast
from datetime import datetime

# from sqlalchemy import create_engine
# from sqlalchemy import Table, MetaData, Column, String, DateTime, SmallInteger

# meta = MetaData(db)  
# shell_table = Table('part_cast', meta,  
#                         Column('pn',     String),
#                         Column('lot',    String),
#                         Column('hanger', SmallInteger))

@app.route('/', methods = ['GET', 'POST'])
def new():
    form = NewPartForm()
    if form.validate_on_submit():
        p = form.partno.data
        l = form.lot.data
        h = form.hanger.data

        new_entry = PartCast(pn=p, lot=l, hanger=h)
        db.session.add(new_entry)
        db.session.commit()
        return render_template('/list.html', title='New Part Entered', parts=PartCast.query.all())

    return render_template('new.html', title='New Part', form=form)

def csrf_error(reason):
    return render_template('csrf_error.html', reason=reason), 400

@app.route('/test')
def test():
    
    return render_template('test.html', parts=PartCast.query.all())

@app.route('/list')
def list_all():
    return render_template('list.html', parts=PartCast.query.all())
'''
Belongs in new() function after form declaration but is difficult to keep	
    if request.method == 'POST':
        p = request.form['partno']
        l    = request.form['lot']
        h = request.form['hanger']
        meta = MetaData(db)
'''
