from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    concavity_mean = float(request.form['concavity_mean'])
    concave_points_mean = float(request.form['concave_points_mean'])
    perimeter_worst = float(request.form['perimeter_worst'])
    area_worst = float(request.form['area_worst'])
    concave_points_worst = float(request.form['concave_points_worst'])
    result = model.predict([[concavity_mean, concave_points_mean, perimeter_worst, area_worst,concave_points_worst]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)