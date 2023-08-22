import requests

def telegram_proxy_message(server_url, text):
    # Constructing the URL for the telegram_text endpoint
    url = f"{server_url}/message"

    # Parameters to be sent with the GET request
    params = {
        'text': text
    }

    # Sending the GET request
    response = requests.get(url, params=params)

    # Handling the response
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.text}")

# Usage Example
server_url = "http://10.2.4.87:2732"
message = "test 0"

telegram_proxy_message(server_url, message)
