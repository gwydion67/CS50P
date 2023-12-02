import requests
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        nb = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    bpi = response["bpi"]
    rateusd = float(bpi["USD"]["rate"].replace(",",""))
    amount = nb * rateusd
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("error")