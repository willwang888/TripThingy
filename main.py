import smartResponse
import pprint

if __name__ == "__main__":
    outOf = input('Where are you coming from?')
    to = input('Where would you like to go?')
    date = input('Day to leave, in this format (yyyy-mm-dd):')

    pprint.pprint(smartResponse.cheapestFlightResponse(outOf, to, date))