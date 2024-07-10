import sys
import requests

def main():
    total = 0
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
    try:
        # payload = {'key1': 'value1', 'key2': 'value2'}
        # r = requests.get('https://httpbin.org/get', params=payload)
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        J = response.json()
        price = J['bpi']['USD']['rate_float']
    except requests.RequestException:
        sys.exit('Request error')
    total = price * bitcoin_amount
    print(f'${total:,.4f}')


main()