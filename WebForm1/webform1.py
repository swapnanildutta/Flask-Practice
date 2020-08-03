from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
#from flask_wtf import Form #<depriciated in latest versions>, to use just clange class attribute from 'FlaskForm' to 'Form'
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import re

key=re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])
    (?=.*[!@#$%&*])
    (?=.*[0-9].*[0-9])
    (?=.*[a-z].*[a-z].*[a-z])
    .{10,}
    $
)''',re.VERBOSE)

app=Flask(__name__)
app.config['SECRET_KEY']=str(key)
Bootstrap(app)

class NameForm(FlaskForm):
    name=StringField("What is your name?", validators=[Required()])
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name!=None and old_name!=form.name.data:
            flash("Looks like you've changed your name!")
        #name=form.name.data
        #form.name.data=''
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

if __name__ == "__main__":
    app.run(debug=True)
