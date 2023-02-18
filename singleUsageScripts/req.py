import requests

# PARAMS
url = "https://happi.yt/"
headers = {
    'Host': 'happi.yt',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://happi.yt/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}  # https://curlconverter.com/python/
cookies = {'perso': 'test'}

# MAIN THREAD
r = requests.get(url, headers=headers, cookies=cookies, verify=False)
print(r.status_code, r.text)
