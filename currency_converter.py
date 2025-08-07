# SuperSnake members: Sahand, Akam, Mustafa
# Final Project: Currency Converter
# Description: User inputs a dollar amount, then the base currecny and target currency and this program will give you the converted rate

import requests
from tabulate import tabulate

def get_rates(base):
    url = "https://v6.exchangerate-api.com/v6/a9b20580f614b33e955d245a/latest/" + base
    try:
        response = requests.get(url)
        data = response.json()
        return data["conversion_rates"]
    except:
        print("error getting rates")
        return {}

def main():
    print("SuperSnake Currency Converter")
    print()

    keep_going = True
    while keep_going:
        amount = input("Please type the amount (numbers only): ").replace(",", "")
        try:
            amt = float(amount)
        except:
            print("invalid amount")
            continue

        from_curr = input("Enter base currency (e.g., USD): ").upper()

        rates = get_rates(from_curr)
        if not rates:
            print("Error getting rates for that currency.")
            continue

        while True:
            to_curr = input("Enter target currency (e.g., EUR): ").upper()
            if to_curr in rates:
                break
            else:
                print("Currency not found. Try again.")

        result = amt * rates[to_curr]

        amt_fmt = f"{amt:,.2f}"
        result_fmt = f"{result:,.2f}"

        headers = ["FROM", "TO", "AMOUNT", "RESULT"]
        row = [from_curr, to_curr, amt_fmt, result_fmt]
        print()
        print(tabulate([row], headers=headers, tablefmt="pipe"))
        print()

        again = input("Would you like to convert another amount and/or currency: ")
        if again.lower() not in ("y", "yes", "Yes"):
            keep_going = False

    print("done")

main()
