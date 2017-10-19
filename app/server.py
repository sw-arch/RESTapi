#! /bin/python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/events', method='GET')
def get_events():
    pass


@app.route('/events/<name>', method='GET')
def get_event_by_name(name=None):
    pass


@app.route('/events/<name>/description', method='GET')
def get_description_by_event_name(name=None):
    pass


@app.route('/events/<name>/ticket_count', method='GET')
def get_ticket_count_by_event_name(name=None):
    pass


@app.route('/events', method='POST')
def create_event():
    pass

@app.route('/events', method='UPDATE')
def update_event():
    pass


@app.route('/events/<name>', method='DELETE')
def remove_event(name=None):
    pass


@app.route('/tickets', method='GET')
def get_tickets():
    pass


@app.route('/tickets/<event_name>', method='GET')
def get_event_ticket(event_name):
    pass


@app.route('/tickets/<event_name>', method='POST')
def purchase_ticket(event_name):
    pass



if __name__ == '__main__':
    app.run(debug=True)
