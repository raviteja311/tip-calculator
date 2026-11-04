VERSION = "0.1.0"
def tip(amount, percent=15):
    return round(amount * percent / 100, 2)
def split(amount, people):
    return round(amount / people, 2)
