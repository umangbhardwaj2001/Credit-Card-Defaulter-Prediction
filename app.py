from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    return render_template('index.html', prediction_text = 'In progress')
if __name__ == '__main__':
    app.run(debug=True)