from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    male = float(request.form['male'])
    age = float(request.form['age'])
    education = float(request.form['education'])
    smoker = float(request.form['smoker'])
    cigsPerDay = float(request.form['cigsPerDay'])
    bpm = float(request.form['bpm'])
    strokes = float(request.form['strokes'])
    hypertension = float(request.form['hypertension'])
    diabetes = float(request.form['diabetes'])
    chol = float(request.form['chol'])
    bp = float(request.form['bp'])
    dia = float(request.form['dia'])
    bmi = float(request.form['bmi'])
    heartRate = float(request.form['heartRate'])
    glucose = float(request.form['glucose'])
    result = model.predict([[male, age, education, smoker,cigsPerDay,bpm,strokes,hypertension,diabetes,chol,bp,dia,bmi,heartRate,glucose]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)