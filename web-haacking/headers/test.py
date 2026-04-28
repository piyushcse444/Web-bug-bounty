import requests

print("start")
session = requests.Session()
url = "http://10.48.162.228/RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret@12345.txt"
headers ={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}

response = session.get(url,verify=False,timeout=5)
print(response.text)