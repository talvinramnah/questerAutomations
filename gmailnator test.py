import requests
url = "https://gmailnator.p.rapidapi.com/generate-email"

payload = { "options": [2] }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ca263c054amshf7a16421e4dd1eap1126cdjsn1de0f0140b58",
	"X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

if response.ok:
    # Extracting the email address from the response
    email_address = response.json().get('email', 'No email found')
    print(email_address)
else:
    print("Error:", response.status_code)
import requests

url = "https://gmailnator.p.rapidapi.com/inbox"

payload = {
	"email": 'jocktmp+uykcs@gmail.com',
	"limit": 1
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ca263c054amshf7a16421e4dd1eap1126cdjsn1de0f0140b58",
	"X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

response_json = response.json()
print(response_json)
message_id = response_json[0]['id']

url = "https://gmailnator.p.rapidapi.com/messageid"

querystring = {"id": message_id}

headers = {
	"X-RapidAPI-Key": "ca263c054amshf7a16421e4dd1eap1126cdjsn1de0f0140b58",
	"X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
print(response.json())