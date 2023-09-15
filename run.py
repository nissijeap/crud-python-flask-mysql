from flask import Flask, render_template
from auth import auth_blueprint
from crud import crud_blueprint

app = Flask(__name__)
app.secret_key = 'many random bytes'

if __name__ == "__main__":
    # Run the auth app first
    auth_app.run(host='0.0.0.0', port=5001, debug=True)
    # Run the main app
    main_app.run(host='0.0.0.0', port=5000, debug=True) 
