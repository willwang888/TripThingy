import smartResponse
import pprint

if __name__ == "__main__":
	outOf = input('Where are you coming from?: ')
	# to = input('Where would you like to go?: ')
	date = input('Day to leave, in this format (yyyy-mm-dd): ')
	duration = input('How long would you like to be away for?(#days--#days). Input "Any" for any duration: ')
	price = input('What is your flight budget?')

	if duration is "Any" or "any":
		pprint.pprint(smartResponse.inspirationFlightResponse(outOf, date, price))
	else:
		pprint.pprint(smartResponse.inspirationFlightResponse(outOf, date, price, duration))