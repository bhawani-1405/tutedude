from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/')
def home():
    return 'This is home page for getting json data, to get data hit the /api path with data, e.g., /api?name=yourname&age=yourage'

@app.route('/api', methods=['GET', 'POST'])
def api():
    a = dict(request.args)

    # Define the backend file path
    backend_file = 'api_data.json'
    
    # Save only the latest data (overwrite old data)
    with open(backend_file, 'w') as file:
        json.dump(a, file)
    
    # Return the saved data to display on the page
    return a

if __name__ == '__main__':
    app.run()