from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for



app = Flask(__name__)
app.debug = True



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('profile'))
    else:
            return render_template('profile.html')





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')



    

    








    


if __name__=='__main__':
    app.run()