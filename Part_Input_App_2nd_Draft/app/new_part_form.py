from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from wtforms import StringField, IntegerField, SubmitField

class NewPartForm(FlaskForm):
    partno = StringField('PartNo', validators=[DataRequired(), InputRequired()])
    lot = StringField('Lot', validators=[DataRequired(), InputRequired()])
    hanger = IntegerField('Hanger', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Input Part')
