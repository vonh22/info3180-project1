from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    num_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired(), NumberRange(min=0)])
    num_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=0)])
    location = StringField('Location', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired(), NumberRange(min=0)])
    type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    submit = SubmitField('Add Property')