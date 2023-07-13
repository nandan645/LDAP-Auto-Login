import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': '',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://gateway.iitmandi.ac.in',
    'Connection': 'keep-alive',
    'Referer': 'http://gateway.iitmandi.ac.in/facstaff/login.php',
    'Upgrade-Insecure-Requests': '1',
}
success_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://gateway.iitmandi.ac.in/facstaff/login.php',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
data = {
    'url': '',
    'username': 'B22xxx',
    'password': 'yourPassword',
}

with requests.Session() as s:
    login_url = 'http://gateway.iitmandi.ac.in/facstaff/login.php'
    r = requests.get(login_url)
    c = r.cookies['PHPSESSID']
    cookies['PHPSESSID'] = c
    auth_url = 'http://gateway.iitmandi.ac.in/facstaff/authenticate.php'
    s.post(auth_url, cookies=cookies, headers=headers, data=data)
    s_r = requests.get('http://gateway.iitmandi.ac.in/facstaff/success.php', cookies=cookies, headers=success_headers)

    soup = BeautifulSoup(s_r.text, 'html.parser')
    data = soup.find('table', class_= 'table table-bordered')
    print("WELCOME TO IIT MANDI WEB BROWSING\n")
    for info in data.find_all('tr'):
        key = (info.find('th').text) + (" - ") + (info.find('td').text)
        print(key)
    