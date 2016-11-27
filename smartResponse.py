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
    

# def cheapestFlightResponse(comingFrom, goingTo, date):

#     outOf = comingFrom
#     to = goingTo
#     leaves = convertDate.convertDate(date)

#     flightJson = getFlights.getCheapestFlights(outOf, to, leaves)
#     if "message" in flightJson.keys():
#         return [flightJson['message']]

#     outputList = []
#     for result in flightJson.get("results", [])[:3]: #This is fine
#         price = result.get("fare", {}).get("total_price", "Unknown")
#         for flights in result.get("itineraries", []):
#             connecting = flights.get("outbound", {}).get("flights", [])
#             isConnecting = "Connecting Flight" if len(connecting) > 1 else "Non Stop"
#             builtFlight = "Price: {}\n{}\n".format( price, isConnecting)
#             for flight in connecting:
#                 aircraftType  = flight.get("aircraft", "Unknown")
#                 leaves_at = toDate.toDate(flight.get("departs_at", "Unknown"))
#                 seatsRemaining = flight.get("booking_info", {}).get("seats_remaining", "Unknown")
#                 travel_class = flight.get("booking_info", {}).get("travel_class", "Unknown")
#                 destination = flight.get("destination", {}).get("airport", "Unknown")
#                 flightNumber = flight.get("flight_number", "Unknown")
#                 airline = flight.get("operating_airline", "Unknown")
#                 origin = flight.get("origin", {}).get("airport", "Unknown")
#                 terminal = flight.get("origin", {}).get("terminal", "Unknown")
#                 flightInfo = """
# Aircraft: {}
# Departing at: {}
# Seats Remaining: {}
# Class: {}
# Origin: {}
# Destinaton: {}
# Flight Number: {}
# Airline: {}
# Terminal: {}

#                 """.format(aircraftType, leaves_at, seatsRemaining, travel_class, origin, destination, flightNumber, airline, terminal)
#                 builtFlight += flightInfo
#             outputList.append(builtFlight)
#     return outputList




def inspirationFlightResponse(comingFrom, date, price, duration = None):

    outOf = comingFrom
    leaves = convertDate.convertDate(date)
    money = price

    if duration is not None:
        flightJson = getFlights.getInspirationFlights(outOf, leaves, price, duration)
    else:
        flightJson = getFlights.getInspirationFlights(outOf, leaves, price)

    if "message" in flightJson.keys():
        return [flightJson['message']]

    outputList = []
    listToSort = []
    currentPrice = 99999999.00

    for result in flightJson.get("results", [])[:3]: #This is fine
        price = result.get("price", "Unknown")
        airline = result.get("airline", "Unknown")
        leaves_at = toDate.toDate(result.get("departure_date", "Unknown"))
        to = result.get("destination", "Unknown")
        come_back = toDate.toDate(result.get("return_date", "Unknown"))

        flightInfo = """

    Price: {}
    Airline: {}
    Departing on: {}
    Origin: {}
    Destinaton: {}
    Return Date: {}

        """.format(price, airline, leaves_at, outOf, to, come_back)

        # For cheapesst flight out of all fo them
        # if float(price) < float(currentPrice):
        #     # print(price)
        #     currentPrice = price
        #     if len(outputList) != 0:
        #         outputList.pop()
        #     else:
        #         outputList.append(flightInfo)

    #For first x number of the list
        listToSort.append(price)

    listToSort.sort(); # Sort in greatest to least order
    listToSort[:3] # First 3 elements of the list of prices

    for num in listToSort:
        for element in flightJson.get("results", []):
            if num == element.get("price"):
                price = element.get("price", "Unknown")
                airline = element.get("airline", "Unknown")
                leaves_at = toDate.toDate(element.get("departure_date", "Unknown"))
                to = element.get("destination", "Unknown")
                come_back = toDate.toDate(element.get("return_date", "Unknown"))

                flightInfo = """

            Price: {}
            Airline: {}
            Departing on: {}
            Origin: {}
            Destinaton: {}
            Return Date: {}

                """.format(price, airline, leaves_at, outOf, to, come_back)

                outputList.append(flightInfo)

    return outputList











