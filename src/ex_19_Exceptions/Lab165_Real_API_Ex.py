import requests # In case of request/response we need to import them

try:
    url = input("Enter the URL: ")
    # response = requests.get("https://google.com")
    response = requests.get(url, timeout = 3)
    print(response.status_code)

except requests.exceptions.ConnectionError:
    print("Connection Error due to wrong URL.")
except requests.exceptions.Timeout:
    print("Timeout Error. Cannot load the URL.")
except Exception as e:
    print(e)