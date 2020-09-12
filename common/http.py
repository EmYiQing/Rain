import ssl
from urllib import request
from urllib import parse

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive"}


def get_request(url):
    context = ssl._create_unverified_context()
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req, context=context)
    result = str(response.read().decode('utf-8'))
    return result


def post_request(url, data):
    context = ssl._create_unverified_context()
    data_string = parse.urlencode(data)
    last_data = bytes(data_string, encoding='utf-8')
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req, context=context, data=last_data)
    result = str(response.read().decode('utf-8'))
    return result

