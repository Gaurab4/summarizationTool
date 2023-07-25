from flask import Flask,render_template,request
from mainFile import summarizerWithURL
from mainFile import summarizerWithWord

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result' , methods=['GET' , 'POST'])
def result():
    if request.method == 'POST':
        URL = request.form['url']
        text  = summarizerWithURL(URL)
    return render_template('summary.html',summary = text)


@app.route('/resultText' , methods=['GET' , 'POST'])
def resultText():
    if request.method == 'POST':
        text = request.form['text']
        ans = summarizerWithWord(text)
    return render_template('summaryText.html' , summaryText = ans)


if __name__ == "__main__":
    app.run(port=8000, debug=True)