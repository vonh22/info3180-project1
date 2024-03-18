"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import flash, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from app.models import Properties
from app.forms import PropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties')
def properties():
    properties = Properties.query.all()  
    for property in properties:
        property.formattedprice = "{:,.0f}".format(float(property.price))
    return render_template('properties.html', properties=properties)

@app.route('/properties/create', methods=['GET', 'POST'])
def add_property():
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data 
        filename = secure_filename(photo.filename) 
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_property = Properties(
            title=form.title.data,
            num_bedrooms=form.num_bedrooms.data,
            num_bathrooms=form.num_bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            type=form.type.data,
            description=form.description.data,
            photo_filename=filename
        )
        
        db.session.add(new_property)
        db.session.commit()
        
        flash('Property added successfully!', 'success')
        return redirect(url_for('properties')) 
        
    return render_template('add_property.html', form=form)

@app.route('/properties/<propertyid>')
def property_details(propertyid):
    property = Properties.query.get_or_404(propertyid)  
    property.formattedprice = "{:,.0f}".format(float(property.price))
    return render_template('property_details.html', property=property)


@app.route('/uploads/<filename>')
def get_image(filename):
    upload_folder = os.path.join(os.getcwd(), 'uploads')  
    return send_from_directory(upload_folder, filename)


# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404