from amadeus import Flights
import pprint

API_KEY = 'z0XEZUMglDdrJRyLOlSLP9La59xvhaK8'

# def getCheapestFlights(current, to, leaves, returns=None):
# 	flights = Flights(API_KEY)
# 	return flights.inspiration_search(
# 	    origin = current,
# 	    destination = to,
# 	    departure_date = leaves + "" if returns is None else "--{}".format(returns)
# 	    )

def getInspirationFlights(current, leaves, price, duration = None):
	flights = Flights(API_KEY)
	return flights.inspiration_search(
	    origin = current,
	    departure_date = leaves,
	    duration = duration,
	    max_price = price
	    )

# pprint.pprint(getCheapestFlights(current, to, leaves))

# pprint.pprint(resp)


# import amadeus

# API_KEY = keys['amadeus']['private']

# def getCheapestFlights(from, to, leaves, returns=None):
#     flight = amadeus.Flights(API_KEY)
#     return flight.low_fare_search(
#         origin = from,
#         destination = to,
#         departure_date=leaves + "" if returns is None else "--{}".format(returns)
#     )


# departure_date = "2016-11-25"