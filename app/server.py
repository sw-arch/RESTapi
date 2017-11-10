#! /bin/python
from flask import Flask, jsonify, abort
from app.data_objects.Event import Event

app = Flask(__name__)
app.json_encoder.default = lambda self, o: o.to_json()

# key: eventName  value: Event()
events = {}


def get_event(name):
    if name in events:
        return events[name]
    else:
        abort(jsonify(status="err",
                      message="No event by this name"))


@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(status="ok",
                   events=events)


@app.route('/events/<name>', methods=['GET'])
def get_event_by_name(name):
    return jsonify(status="ok",
                   event=get_event(name))


@app.route('/events/<name>/description', methods=['GET'])
def get_description_by_event_name(name):
    return jsonify(status="ok",
                   description=get_event(name).description)


@app.route('/events/<name>/tickets_available', methods=['GET'])
def get_ticket_count_by_event_name(name=None):
    return jsonify(status="ok",
                   tickets_available=len(get_event(name).ticketsAvailable))


@app.route(
    '/create/<name>/<description>/<int:numberOfSeats>/<float:ticketPrice>',
    methods=['POST'])
def create_event(name, description, numberOfSeats, ticketPrice):
    if name in events:
        return jsonify(status="err",
                       message="An event already exists by that name")
    else:
        event = Event(name, description, numberOfSeats, ticketPrice)
        events[name] = event
        return jsonify(status="ok",
                       event=event.to_json())


@app.route('/events/<name>', methods=['DELETE'])
def remove_event(name):
    if name in events:
        del events[name]
        return jsonify(status="ok")
    else:
        return jsonify(status="err",
                       message="No event by this name")


@app.route('/purchase/<eventName>', methods=['POST'])
def purchase_ticket(eventName):
    ticket = get_event(eventName).reserve_ticket()
    if ticket is not None:
        return jsonify(status="ok",
                       ticket=ticket)
    else:
        return jsonify(status="err",
                       message="There are no available tickets for this event")


@app.route('/refund/<eventName>/<int:ticketNumber>', methods=['POST'])
def refund_ticket(eventName, ticketNumber):
    if get_event(eventName).refund_ticket(ticketNumber):
        return jsonify(True)
    else:
        return jsonify(status="err",
                       message=f"No ticket number {ticketNumber} found for "
                               "this event")


if __name__ == '__main__':
    app.run("0.0.0.0", 80)
