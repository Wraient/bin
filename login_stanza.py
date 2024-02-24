import requests

# First POST request
otp_url = 'http://wifiunify38.spectra.co/userportal/pages/usermedia/spectra3/stanza-disable-random-mac/otp.jsp'
otp_data = {
    'memberId': '23TSFBA023'
}
otp_cookies = {
    'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
}
otp_response = requests.post(otp_url, data=otp_data, cookies=otp_cookies)

# Second POST request
login_url = 'http://wifiunify38.spectra.co/userportal/newlogin.do'
login_data = {
    'username': 'STN-23TSFBA023',
    'password': '1981',
    'type': '2',
    'phone': '0',
    'jsonresponse': '1'
}
login_cookies = {
    'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
}
login_response = requests.post(login_url, data=login_data, cookies=login_cookies)

# Third POST request
magic_url = 'http://10.201.21.1/login'
magic_data = {
    'username': 'STN-23TSFBA023',
    'password': '1981',
    'magic': ''
}
magic_response = requests.post(magic_url, data=magic_data)

if all([response.status_code == 200 for response in [otp_response, login_response, magic_response]]):
    print("Login successful")
else:
    print("Login failed")

