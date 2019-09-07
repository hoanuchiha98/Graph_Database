from flask import render_template, redirect
from flask_marshmallow import Marshmallow

# app = Flask(__name__)

import connect  # personal config

# Get the application instance
connex_app = connect.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")



# Create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    @return@ auto redirect to swagger.ui
    """
    response = redirect("api/ui", code=302)
    headers = dict(response.headers)
    response.headers = headers
    return response


def startUp():
    print("Started App")

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    connex_app.run(port=5011, debug=True)
