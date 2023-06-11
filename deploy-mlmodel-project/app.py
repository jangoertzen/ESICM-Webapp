from flask import Flask, request, render_template
import pickle
import joblib

# Load the model from the file
model = joblib.load('dein_modell.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    mechanical_power = float(request.form["mechanical_power"])
    body_height = float(request.form["body_height"])
    ibw = (body_height - 100) - 0.10 * (body_height - 100)
    mpibw = mechanical_power / ibw
    ie = float(request.form["ie"]) if request.form["ie"] else None
    pfratio = float(request.form["pfratio"]) if request.form["pfratio"] else None
    petco2paco2 = float(request.form["petco2paco2"]) if request.form["petco2paco2"] else None
    hbmin = float(request.form["hbmin"]) if request.form["hbmin"] else None
    gender = int(request.form["gender"]) if request.form["gender"] else None
    
    # Construct list of inputs
    inputs = [ie, pfratio, petco2paco2, hbmin, mpibw, gender]
    
    # Fill missing values
    inputs = [0 if value is None else value for value in inputs]

    prediction_proba = model.predict_proba([inputs])  # this returns a list of probabilities e.g. [0.94, 0.06]
    class0_prob = round(prediction_proba[0][0] * 100, 2)  # get the first class probability and convert to percentage
    class1_prob = round(prediction_proba[0][1] * 100, 2)  # get the second class probability and convert to percentage

    # Add conditional logic to assign CSS classes based on class0_prob
    if class0_prob > 90:
        result_class = 'success'
    elif 60 <= class0_prob <= 90:
        result_class = 'warning'
    else:
        result_class = 'danger'

    output = f"This model predicts with {class0_prob}% probability that the patient will be successfully weaned. The probability for weaning failure is {class1_prob}%."
    # Pass the result_class variable to your template
    return render_template('index.html', prediction_text=output, ie=ie, pfratio=pfratio, petco2paco2=petco2paco2, hbmin=hbmin, mpibw=mpibw, gender=gender, result_class=result_class)



if __name__ == "__main__":
    app.run()