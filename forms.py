from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,DateField, IntegerField, FileField
from wtforms.validators import DataRequired

class Online_queue(FlaskForm):
    filial = SelectField(u'Filial',choices=[])
    xidmet= SelectField('Xidmət Növü',choices=[()])
    date= DateField(label='Tarix',format='%Y-%m-%d' , validators=[DataRequired()])
    number= IntegerField(label='Mobil nömrə',validators=[DataRequired()])

# 'Sürətli pul köçürmələri','Sürətli pul köçürmələri'),('Western Union','Western Union'), ('Barat','Barat'), ('Zolotoya Korona','Zolotoya Korona'

