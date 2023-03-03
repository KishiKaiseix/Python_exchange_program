Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
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


def converter_buy(rates, amounts):
    amounts = amounts * rates - 3.5
    return amounts


def converter_sell(rates, amounts):
    amounts = amounts * rates + 3.5
    return amounts


try:
    currency = str(input("Enter currency name: "))
    cad = 1
    if currency == "USD":
        rate = rate_usd(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "EUR":
        rate = rate_euro(cad, currency)
        buy_rate = rate - ((rate * 2.94) / 100)
        sell_rate = rate + ((rate * 3) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "CHF":
        rate = rate_swiss(cad, currency)
        buy_rate = rate - ((rate * 9) / 100)
        sell_rate = rate + ((rate * 5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "DOM":
        rate = rate_dom(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "MXN":
        rate = rate_mexican(cad, currency)
        buy_rate = rate - ((rate * 2.5) / 100)
        sell_rate = rate + ((rate * 3) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "GBP":
        rate = rate_sterling(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "CNY":
        rate = rate_china(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "JPY":
        rate = rate_japan(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "WON":
        rate = rate_south_korea(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "CRC":
        rate = rate_costa_rica(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    elif currency == "AUD":
        rate = rate_australia(cad, currency)
        buy_rate = rate - ((rate * 3) / 100)
        sell_rate = rate + ((rate * 3.5) / 100)
        print("Buy rate is ", "%.5f" % buy_rate)
        print("Sell rate is", "%.5f" % sell_rate)
    question_buy_or_sell = str(input("Buy or Sell (B or S please): "))
    amount = float(input("Enter amount: "))
    if question_buy_or_sell == "B":
        question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
        if question_view_rates == "Y":
            print("Better rates are", "%.5f" % better_rate_buy(buy_rate))
            print("Premium rates are", "%.5f" % premium_rate_buy(buy_rate))
            question_choose_rate = str(input("choose rate please(P, B, N): "))
            if question_choose_rate == "N":
                print("rate is", buy_rate)
                print("commission =", 3.5, "$")
                print("amount =", converter_buy(buy_rate, amount))
            elif question_choose_rate == "B":
                print("rate is", "%.5f" % better_rate_buy(buy_rate))
                print("commission =", 3.5, "$")
                print("amount =", converter_buy(better_rate_buy(buy_rate), amount))
            elif question_choose_rate == "P":
                print("rate is", "%.5f" % premium_rate_buy(buy_rate))
                print("commission =", 3.5, "$")
...                 print("amount =", converter_buy(premium_rate_buy(buy_rate), amount))
... 
...         if question_view_rates == "N":
...             print("rate is", buy_rate)
...             print("commission =", 3.5, "$")
...             print("amount =", converter_buy(buy_rate, amount))
... 
...     elif question_buy_or_sell == "S":
...         question_view_rates = str(input("do you want to view rates(Y for yes , N for no): "))
...         if question_view_rates == "Y":
...             print("Better rates are", "%.5f" % better_rate_sell(sell_rate))
...             print("Premium rates are", "%.5f" % premium_rate_sell(sell_rate))
...             question_choose_rate = str(input("choose rate please(P, B, N): "))
...             if question_choose_rate == "N":
...                 print("rate is", sell_rate)
...                 print("commission =", 3.5, "$")
...                 print("amount =", converter_sell(sell_rate, amount))
...             elif question_choose_rate == "B":
...                 print("rate is", "%.5f" % better_rate_buy(sell_rate))
...                 print("commission =", 3.5, "$")
...                 print("amount =", converter_sell(better_rate_sell(sell_rate), amount))
...             elif question_choose_rate == "P":
...                 print("rate is", "%.5f" % premium_rate_sell(sell_rate))
...                 print("commission =", 3.5, "$")
...                 print("amount =", converter_sell(premium_rate_sell(sell_rate), amount))
... 
...         if question_view_rates == "N":
...             print("rate is", sell_rate)
...             print("commission =", 3.5, "$")
...             print("amount =", converter_sell(sell_rate, amount))
...     else:
...         print("Aborting transaction")
... finally:
...     print("起死回生 ϟ - 2023")
... 
