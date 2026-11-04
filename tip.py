VERSION = "1.0.1"
def tip(amount, percent=18):
    return round(amount * percent / 100, 2)
def split(amount, people):
    return round(amount / people, 2)
