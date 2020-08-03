from flask import  Flask,render_template
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime

app=Flask(__name__)
moment=Moment(app)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())
'''
@app.route('/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
'''
if __name__ == "__main__":
    app.run(debug=True)