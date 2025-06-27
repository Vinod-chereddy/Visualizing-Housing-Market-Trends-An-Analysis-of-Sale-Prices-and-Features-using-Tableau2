# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page which will display the embedded Tableau dashboard
@app.route('/')
def home():
    """
    Renders the main HTML page where the Tableau dashboard/story will be embedded.
    """
    # In a more complex application, you might pass dynamic data to the template here
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application
    # debug=True allows for automatic reloading on code changes and provides a debugger
    # Set debug=False for production environments
    app.run(debug=True)