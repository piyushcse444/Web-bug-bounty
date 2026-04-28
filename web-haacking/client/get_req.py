import requests

class HttpRequest:
    def __init__(self):
        self.session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        }
        self.session.headers.update(headers)

    def get_req(self, url):
        return self.session.get(url, verify=True)


if __name__ == "__main__":
    url = "http://192.168.166.246:8000"
    response = HttpRequest().get_req(url)
    print(response.text)