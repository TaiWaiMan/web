from flask import Flask, render_template
# from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.rote("/")
    
# app.debug = True

# if __name__ == '__main__':
app.run(debug=True)
app.run() 