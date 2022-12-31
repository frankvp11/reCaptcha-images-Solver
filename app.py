from flask import Flask, request
from flask_cors import CORS, cross_origin
from solver import Solver
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/send', methods=['POST'])
@cross_origin()
def send_data():
    # Get the data from the request
    print("Recieving data!")
    data = request.get_json()
    url = data
    
    solver = Solver(url)
    value = solver.complete()
    
    return value
   

@app.route('/receive')
def receive_data():
    # Send some data back to the client
    return 'token: tokennsnsfeinwfwoh'

if __name__ == '__main__':
    app.run()
