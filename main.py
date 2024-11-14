from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained models and dataset
random_forest_model = pickle.load(open("RandomForestModel.pkl", "rb"))
linear_regression_model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
decision_tree_model = pickle.load(open("DecisionTreeModel.pkl", "rb"))  # Load Decision Tree model
car = pd.read_csv("CleanedCar.csv")

@app.route('/')
def index():
    # Extract unique values for dropdowns from the cleaned car dataset
    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    # Render the HTML template and pass the variables
    return render_template('index.html', companies=companies, car_model=car_model, year=year, fuel_type=fuel_type)

@app.route('/final_data', methods=['POST'])
def final_data():
    company = request.form.get('company')
    car_model = request.form.get('car')
    year = int(request.form.get('year'))
    fuel = request.form.get('fuel')
    kms = int(request.form.get('kms'))
    model_type = request.form.get('model')  # The model selected by the user

    # Prepare the data to feed into the selected model
    input_data = pd.DataFrame([[car_model, company, year, kms, fuel]], 
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    # Choose the model based on user input
    if model_type == 'Random Forest':
        predict_output = random_forest_model.predict(input_data)
    elif model_type == 'Decision Tree':  # Decision Tree model option
        predict_output = decision_tree_model.predict(input_data)
    else:
        predict_output = linear_regression_model.predict(input_data)
    
    # Return the predicted price
    return str(np.round(predict_output[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
