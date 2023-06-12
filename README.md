# Title: ACID Model for Predicting Weaning Failure - Flask Webapp

## Description

Welcome to our Flask web application that utilizes the ACID (Algorithm developers for Critical and Intensive care Datathon) model for predicting weaning failure in intensive care patients. The ACID model, a product of our participation in the 5th ESICM Datathon 2023, takes into consideration a range of vital patient data including the I:E ratio, P/F ratio, PetCO₂/PaCO₂ ratio, the lowest Hb, the ratio of Mechanical Power to Ideal Body Weight (MP/IBW), and the patient's gender. The application uses these inputs to generate prediction results, which are subsequently presented for an easy understanding of the predicted probability of weaning failure.

The ACID model employs the Extra Trees Classifier algorithm and has been trained on data sourced from the AmsterdamUMCdb, a comprehensive intensive care database.

## Installation Guide

  To get this web application running on your local machine, follow these steps:

    Clone this repository to your local machine.
    Make sure Python and all necessary dependencies are installed on your system. If not, install them by executing pip install -r requirements.txt in your command prompt or terminal.
    Run app.py to start the Flask server. Now, you can access the web application on your local host.


## Usage

The user interface of our web application is designed to be straightforward and easy to use. It includes fields for inputting the required patient data. After you have filled out these fields, click on the "Predict Weaning Failure" button. The application will process the input data and present the prediction results on the screen.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


## Disclaimer

This project was created as a part of our participation in the 5th ESICM Datathon 2023 and is intended solely for demonstration and educational purposes. The data used for the model is subject to change, and the research associated with this model has not yet been published or peer-reviewed. As such, the use of this model in patient care is strongly discouraged until further scientific validation is provided.


## Final Words

We have enjoyed every step of the journey in participating in the 5th ESICM datathon 2023. The process of creating this model was both challenging and enriching, allowing us to apply and further our knowledge in the field of AI and healthcare. We are pleased to share this model with the community.

Should you have any questions, comments, or suggestions, please do not hesitate to reach out to us.