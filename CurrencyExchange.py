# Below are the functions to get the rate of each currency , we perfer repeating functions to manually change the rate
# We don't want to rely on internet connectivity
def rate_usd(usd, ca):
    return 1.36


def rate_euro(euro, ca):
    return 1.44


def rate_sterling(gbp, ca):
    return 1.63


def rate_mexican(mxn, ca):
    return 0.075


def rate_dom(dom, ca):
    return 0.025


def rate_swiss(chf, ca):
    return 1.45


def rate_japan(jpy, ca):
    return 0.0099


def rate_south_korea(won, ca):
    return 0.0010


def rate_china(cny, ca):
    return 0.20


def rate_costa_rica(crc, ca):
    return 0.0024


def rate_australia(aud, ca):
    return 0.91

# fucntions for different rates that depend on the amount given by the customer


def premium_rate_buy(premium_buy):
    premium_buy = rate - ((rate * 2) / 100)
    return premium_buy


def premium_rate_sell(premium_sell):
    premium_sell = rate + ((rate * 2) / 100)
    return premium_sell


def better_rate_buy(normal_buy):
    normal_buy = rate - ((rate * 2.7) / 100)
    return normal_buy


def better_rate_sell(normal_sell):
    normal_sell = rate + ((rate * 2.7) / 100)
    return normal_sell


# functions that calculate the buy or sell rate that depends on user input


def converter_buy(rates, amounts):
    amounts = amounts * rates - 3.5
    return amounts


def converter_sell(rates, amounts):
    amounts = amounts * rates + 3.5
    return amounts


# Start of program
print("Hello i will be your Currency Exchange corp assistant today")
print("let's start by choosing the currency you are interested in")
# We use major currencies only
available_currencies = ["EUR", "USD", "CNY", "CRC", "CHF", "JPY", "WON", "AUD", "GBP", "MXN", "DOM"]
print("So here is the list of available currencies")
print(available_currencies)
try:
    currency = str(input("Enter currency name: "))
    cad = 1  # Base currency is canadian Dollar
    # Viewing rates of the currency from the currency input
    if currency in available_currencies:
        if currency == "USD":
            rate = rate_usd(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "EUR":
            rate = rate_euro(cad, currency)
            buy_rate = rate - ((rate * 2.94) / 100)
            sell_rate = rate + ((rate * 3) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "CHF":
            rate = rate_swiss(cad, currency)
            buy_rate = rate - ((rate * 9) / 100)
            sell_rate = rate + ((rate * 5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "DOM":
            rate = rate_dom(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "MXN":
            rate = rate_mexican(cad, currency)
            buy_rate = rate - ((rate * 2.5) / 100)
            sell_rate = rate + ((rate * 3) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "GBP":
            rate = rate_sterling(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "CNY":
            rate = rate_china(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "JPY":
            rate = rate_japan(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "WON":
            rate = rate_south_korea(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "CRC":
            rate = rate_costa_rica(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
        elif currency == "AUD":
            rate = rate_australia(cad, currency)
            buy_rate = rate - ((rate * 3) / 100)
            sell_rate = rate + ((rate * 3.5) / 100)
            print("Sell rate is ", "%.5f" % buy_rate)
            print("Buy rate is", "%.5f" % sell_rate)
    if currency not in available_currencies:
        print("try again")
    # Now we will ask the user whether they want to buy or sell the currency
    print("So you are intersted in", currency)
    question_buy_or_sell = str(input("Would like to Buy or Sell (B or S please) in this currency: "))
    amount = float(input("Enter the amount please: "))
    if question_buy_or_sell == "S":
        if amount < 1500:
            print("rate is", buy_rate)
            print("commission =", 3.5, "$")
            print("amount =", converter_buy(buy_rate, amount))

        if amount > 1500:  # we offer better rates the bigger the amount
            print("We can offer better rates then the ones shown above exceptionnally for this amount of", amount)
            question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
            # the user has the capacity to choose to apply rate or not
            if question_view_rates == "Y":
                print("Better rates are", "%.5f" % better_rate_buy(buy_rate))
                print("Premium rates are", "%.5f" % premium_rate_buy(buy_rate))
                question_choose_rate = str(input("Do you want to apply new rates? (Y or N): "))
                if question_choose_rate == "N":
                    print("rate is", buy_rate)
                    print("commission =", 3.5, "$")
                    print("amount =", converter_buy(buy_rate, amount))
                elif question_choose_rate == "Y":
                    print("rate is", "%.5f" % better_rate_buy(buy_rate))
                    print("commission =", 3.5, "$")
                    print("amount =", converter_buy(better_rate_buy(buy_rate), amount))

                elif question_choose_rate == "P":
                    print("rate is", "%.5f" % premium_rate_buy(buy_rate))
                    print("commission =", 3.5, "$")
                    print("amount =", converter_buy(premium_rate_buy(buy_rate), amount))
            if amount > 2500:
                print("We can offer better rates then the ones shown above exceptionnally for this amount of", amount)
                question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
                if question_view_rates == "Y":
                    print("Premium rates are", "%.5f" % premium_rate_buy(buy_rate))
                question_choose_rate = str(input("Do you want to apply new rates? (Y or N): "))
                if question_choose_rate == "N":
                    print("rate is", buy_rate)
                    print("commission =", 3.5, "$")
                    print("amount =", converter_buy(buy_rate, amount))
                elif question_choose_rate == "Y":
                    print("rate is", "%.5f" % premium_rate_buy(buy_rate))
                    print("commission =", 3.5, "$")
                    print("amount =", converter_buy(premium_rate_buy(buy_rate), amount))

    elif question_buy_or_sell == "B":
        if amount <= 1500:
            print("rate is", sell_rate)
            print("commission =", 3.5, "$")
            print("amount =", converter_sell(sell_rate, amount))

        if amount > 1500:
            print("We can offer better rates then the ones shown above exceptionnally for this amount of", amount)
            question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
            if question_view_rates == "Y":
                print("Better rates are", "%.5f" % better_rate_sell(sell_rate))
            question_choose_rate = str(input("Do you want to apply special rate(Y or N): "))
            if question_choose_rate == "N":
                print("rate is", sell_rate)
                print("commission =", 3.5, "$")
                print("amount =", converter_sell(sell_rate, amount))
            elif question_choose_rate == "Y":
                print("rate is", "%.5f" % better_rate_buy(sell_rate))
                print("commission =", 3.5, "$")
                print("amount =", converter_sell(better_rate_sell(sell_rate), amount))
        if amount > 2500:
            print("We can offer better rates then the ones shown above exceptionnally for this amount of", amount)
            question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
            if question_view_rates == "Y":
                print("Premium rates are", "%.5f" % premium_rate_sell(sell_rate))
            question_choose_rate = str(input("Do you want to apply special rate(Y or N): "))
            if question_choose_rate == "N":
                print("rate is", sell_rate)
                print("commission =", 3.5, "$")
                print("amount =", converter_sell(sell_rate, amount))
            elif question_choose_rate == "Y":
                print("rate is", "%.5f" % premium_rate_sell(sell_rate))
                print("commission =", 3.5, "$")
                print("amount =", converter_sell(premium_rate_sell(sell_rate), amount))
    else:
        print("Aborting transaction")
        # finally to print the name of the developer
finally:
    print("Developed by Fares Majdoub ϟ - 2023")



# Comments of chatGpt for this program that i wrote 3 weeks into learning python :
# I would say that the code is at an intermediate level. The code includes functions for calculating exchange rates based on different currencies, as well as functions for calculating premium and better exchange rates based on user input. Additionally, there are functions for converting currency based on user input.
#the code is well-structured and easy to understand
