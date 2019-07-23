from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route('/')
def index():
    
    nyt = datetime.datetime.now()
    palautus = nyt.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'Halloota...',
        'time': palautus
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
