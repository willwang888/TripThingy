import getFlights
# import getHotels
# import getCarRentals
import toDate
import pprint
import json
import convertDate
import pprint

# def codeToFullName(originAirport):
#     return originAirport
#     airportsJsonData = json.load(open("utils/airportsJson.json"))

#     for state in airportsJsonData: # Turn origin airport into real name rather than code
# 	for airportKey, airportValue in airportsJsonData[state].items():
# 	    if airportValue == originAirport:
# 		originAirport = airportKey + "(" + airportValue + ")"
#                 return originAirport
#     return originAirport
    

def cheapestFlightResponse(comingFrom, goingTo, date):

    outOf = comingFrom
    to = goingTo
    leaves = convertDate.convertDate(date)

    flightJson = getFlights.getCheapestFlights(outOf, to, leaves)
    if "message" in flightJson.keys():
        return [flightJson['message']]

    outputList = []
    for result in flightJson.get("results", [])[:3]:
        price = result.get("fare", {}).get("total_price", "Unknown")
        for flights in result.get("itineraries", []):
            connecting = flights.get("outbound", {}).get("flights", [])
            isConnecting = "Connecting Flight" if len(connecting) > 1 else "Non Stop"
            builtFlight = "Price: {}\n{}\n".format( price, isConnecting)
            for flight in connecting:
                aircraftType  = flight.get("aircraft", "Unknown")
                leaves_at = toDate.toDate(flight.get("departs_at", "Unknown"))
                seatsRemaining = flight.get("booking_info", {}).get("seats_remaining", "Unknown")
                travel_class = flight.get("booking_info", {}).get("travel_class", "Unknown")
                destination = flight.get("destination", {}).get("airport", "Unknown")
                flightNumber = flight.get("flight_number", "Unknown")
                airline = flight.get("operating_airline", "Unknown")
                origin = flight.get("origin", {}).get("airport", "Unknown")
                terminal = flight.get("origin", {}).get("terminal", "Unknown")
                flightInfo = """
Aircraft: {}
Departing at: {}
Seats Remaining: {}
Class: {}
Origin: {}
Destinaton: {}
Flight Number: {}
Airline: {}
Terminal: {}

                """.format(aircraftType, leaves_at, seatsRemaining, travel_class, origin, destination, flightNumber, airline, terminal)
                builtFlight += flightInfo
            outputList.append(builtFlight)
    return outputList











