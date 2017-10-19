#! /bin/python
from flask import Flask, jsonify, abort, make_response
from .data_objects.Event import Event


app = Flask(__name__)


# key: eventName  value: Event()
events = {}


def get_event(name):
    if name in events:
        return events[name]
    else:
        abort(make_response("No event by this name", 403))


@app.route('/events', method='GET')
def get_events():
    return jsonify(events)


@app.route('/events/<name>', method='GET')
def get_event_by_name(name):
    return jsonify(get_event(name))


@app.route('/events/<name>/description', method='GET')
def get_description_by_event_name(name):
    return jsonify(get_event(name).description)


@app.route('/events/<name>/ticket_count', method='GET')
def get_ticket_count_by_event_name(name=None):
    return jsonify(get_event(name).get_tickets_remaining())


@app.route('/events/new/<name>/<description>/<numberOfSeats>/<ticketPrice>',
           method='POST')
def create_event(name, description, numberOfSeats, ticketPrice):
    if name in events:
        abort(make_response("An event already exists by that name", 403))
    else:
        events[name] = Event(name, description, numberOfSeats, ticketPrice)


@app.route('/events/<name>', method='DELETE')
def remove_event(name):
    if name in events:
        del events[name]
    else:
        abort(make_response("No event by this name", 403))


@app.route('/purchase/<eventName>', method='POST')
def purchase_ticket(eventName):
    ticket = get_event(eventName).reserve_ticket()
    if ticket is not None:
        return jsonify(ticket)
    else:
        abort(make_response(
            "There are no available tickets for this event", 403
        ))


@app.route('/refund/<eventName>/<ticketNumber>', method='POST')
def refund_ticket(eventName, ticketNumber):
    if get_event(eventName).refund_ticket(ticketNumber):
        return jsonify(True)
    else:
        abort(make_response(
            f"No ticket number {ticketNumber} found for this event", 403
        ))


if __name__ == '__main__':
    app.run(debug=True)
