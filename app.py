from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from waitress import serve
from src.utils import clean_message
from src.models.predictor import get_prediction


app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/make_prediction", methods=["POST"])
def make_prediction():
    """ Use the ML model to make a prediction using the form inputs. """
    # Get the data from the submitted form
    data = request.form['message']

    cleaned_message = clean_message(data)
    
    print('CLEANED MESSAGE: ', cleaned_message)
    # Send the values to the model to get a prediction
    prediction = get_prediction(cleaned_message)
    print('PREDICTION: ', prediction)
    # Tell the browser to fetch the results page, passing along the prediction
    return redirect(url_for("show_results", prediction=prediction))

@app.route("/show_results")
def show_results():
    """ Display the results page with the provided prediction """
    
    prediction = int(request.args.get('prediction'))
    
    # Round it for display purposes

    if prediction == 0:
        message = "This is not Spam"
    else: 
        message = "This is Spam"

    # Return the results pge
    return render_template("results.html", prediction = message)


#if __name__ == "__main__":
    #serve(app, host='0.0.0.0', port=5000)
