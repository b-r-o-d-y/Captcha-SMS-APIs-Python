import requests
from colorama import init, Fore, Back, Style
import time

starting = Fore.YELLOW
finished = Fore.CYAN
done = Fore.GREEN
failed = Fore.RED

resetc = Style.RESET_ALL
# colour legend

sms_api_key = 'API KEY HERE'

print(starting + 'Getting number...')
print(resetc)

endpoint0 = f"https://sms-activate.org/stubs/handler_api.php?api_key={sms_api_key}&action=getNumber&service=mm&ref=1996036&country=16"

response0 = requests.get(endpoint0)

if 'ACCESS_NUMBER' in response0.text:

    get_number = response0.text
    sms_number = get_number.split(':')[2]
    sms_number1 = sms_number[2:]
    sms_id = get_number.split(':')[1]
    print(finished + 'Got Number!')
    print(resetc)

while True:

    endpoint1 = f"https://api.sms-activate.org/stubs/handler_api.php?api_key={sms_api_key}&action=getStatus&id={sms_id}"

    response1 = requests.get(endpoint1)
    #print(response3.text)

    if 'STATUS_WAIT_CODE' in response1.text:
        print(starting + 'Waiting for code...')
        print(resetc)
        time.sleep(10)

    if 'STATUS_OK' in response1.text:
        print(finished + 'Got code!')
        print(resetc)
        get_code = response1.text
        received_code = get_code.split(':')[1]
        #print(received_code)
        break

    else:
        print(response1.text)
        time.sleep(10)