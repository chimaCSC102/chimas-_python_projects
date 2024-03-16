# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
#     symptoms = features.columns.values
#     print(features.columns.values)

#     # Creating a symptom index dictionary to encode the
#     # input symptoms into numerical form
#     symptom_index = {}
#     for index, value in enumerate(symptoms):
#     	symptom = " ".join([i.capitalize() for i in value.split("_")])
#     	symptom_index[symptom] = index
    
#     data_dict = {
#     	"symptom_index":symptom_index,
#     	"predictions_classes":le.classes_
#     }

#     # Defining the Function
#     # Input: string containing symptoms separated by commas
#     # Output: Generated predictions by models
#     def predictDisease(symptoms):
#     	symptoms = symptoms.split(",")
    	
#     	# creating input data for the models
#     	input_data = [0] * len(data_dict["symptom_index"])
#     	for symptom in symptoms: #for each symptom, it gets the index and update it's value to 1
#     		index = data_dict["symptom_index"][symptom]
#     		input_data[index] = 1
    		
#     	# reshaping the input data and converting it
#     	# into suitable format for model predictions
#     	input_data = np.array(input_data).reshape(1,-1)
    	
#     	# generating individual outputs
#     	# rf_prediction = data_dict["predictions_classes"][final_rfc_model.predict(input_data)[0]]
#     	# nb_prediction = data_dict["predictions_classes"][final_gaussian_model.predict(input_data)[0]]
#     	svm_prediction = data_dict["predictions_classes"][dumped_model.predict(input_data)[0]]
#         # lr_prediction = data_dict["predictions_classes"][final_lr_model.predict(input_data)[0]]

        
    	
#     	# making final prediction by taking mode of all predictions
#     	# final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
#     	predictions = {
#     		# "rf_model_prediction": rf_prediction,
#     		# "naive_bayes_prediction": nb_prediction,
#     		"svm_model_prediction": svm_prediction,
#     		# "final_prediction":final_prediction
#     	}
#     	return predictions

# # Testing the function
# # print(predictDisease("Fatigue,Obesity,Nausea"))
#     int_features = [eval(x) for x in request.form.values()]  
#     result = predictDisease(int_features)

#     return render_template('index.html', prediction_text="Disease prediction :{}".format(result))


# if __name__ == "__main__":
#     app.run(debug=True)


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
    symptoms = request.form['symptoms']
    
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)