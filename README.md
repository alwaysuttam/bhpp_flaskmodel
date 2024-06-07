              #  Bengaluru House Price Prediction Web Application


This web application estimates the price of a house based on various parameters such as location, square footage (sqft), number of bedrooms (BHK), and number of bathrooms (bath). The model is pre-trained and the application serves predictions using this model.

                ##  **Project Structure**

app.py: The main Flask application script.

templates/: Directory containing HTML template(s) for the web pages.
          index.html: The main page where users input the data and view predictions.

data/: Directory containing necessary data files.
       columns.json: JSON file containing the data columns used by the model.
       bhpp.pickle: Pickle file containing the trained model.

              ## **Setup Instructions**
**Prerequisites**
Python 
Flask
Numpy
Scikit-learn (for loading the pickle model)


**Installation**

Clone the repository or download the project files.

Ensure you have Python installed on your machine.

Install the necessary Python packages using pip:


pip install flask numpy scikit-learn
Running the Application
Navigate to the project directory.

Run the Flask application:

python app.py
Open your web browser and go to http://127.0.0.1:5000/.

**screenshots from the project**

![alt text](<Screenshot (51).png>)
