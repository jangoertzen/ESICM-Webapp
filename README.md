# Title: ACID Model for Predicting Weaning Failure - Flask Webapp

## Description

This web application uses the ACID (Algorithm developers for Critical and Intensive care Datathon) model for predicting weaning failure in intensive care patients. The model takes into consideration various patient data like I:E ratio, P/F ratio, PetCO2/PaCO2 ratio, lowest Hb, Mechanical Power to Ideal Body Weight (MP/IBW) ratio, and Gender. The prediction results are displayed both in text and graphically as a pie chart.

The ACID model was trained using the Extra Trees Classifier algorithm on data from the AmsterdamUMCdb, a large medical database.

## Installation Guide

    Clone this repository.
    Make sure you have Python and the necessary dependencies installed. You can do this by running pip install -r requirements.txt.
    Run app.py to start the Flask server.


## Usage

The user interface includes fields for inputting the patient data mentioned above. After filling out the fields, click on "Predict Value!". The app will then display the prediction results.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


## Disclaimer

This project was created solely for demonstration purposes and was the result of participation in the 5th ESICM Datathon 2023. The data used is subject to change. The research has not yet been published or peer-reviewed, and the use of this model in patient care is strongly discouraged.


## Final Words

We hope this project serves as an inspiration for those interested in the development of AI models in medicine. For questions, comments, or suggestions, please feel free to contact us.