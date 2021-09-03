from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/gameplay.html')
def gameplay():
    return render_template('gameplay.html')

@app.route('/plot.html')
def plot():
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)