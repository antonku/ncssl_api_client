from requests import get


def myip():
    return get('http://checkip.amazonaws.com/').text.strip()
