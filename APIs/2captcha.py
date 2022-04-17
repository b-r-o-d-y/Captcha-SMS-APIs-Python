import requests
from colorama import init, Fore, Back, Style
import time

starting = Fore.YELLOW
finished = Fore.CYAN
done = Fore.GREEN
failed = Fore.RED

resetc = Style.RESET_ALL
# colour legend

two_captcha_key = 'API KEY HERE'
sitekey = 'SITEKEY HERE'

endpoint = f"http://2captcha.com/in.php?key={two_captcha_key}&method=userrecaptcha&googlekey={sitekey}&pageurl=https://www.footlocker.ca/en/account/create"

response = requests.post(endpoint)
#print(response.text)
captcha_id_step1 = response.text
captcha_id = captcha_id_step1.split('|')[1]
#print(captcha_id)
print(finished + 'Got Captcha ID')

time.sleep(55)

print(starting + 'Solving Captcha...')
while True:

    endpoint1 = f"http://2captcha.com/res.php?key={two_captcha_key}&action=get&id={captcha_id}"

    response1 = requests.get(endpoint1)
    #print(response1.text)
    captcha_token_step1 = response1.text
    captcha_token = captcha_token_step1.split('|')[1]
    #print(captcha_token)

    if 'OK' in response1.text:
        #print(captcha_token)
        print(finished + 'Got 2Captcha Response Token')
        print(captcha_token)

    if 'ERROR' in response1.text:
        print('Error')
        time.sleep(5)