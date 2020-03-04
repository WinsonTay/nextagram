import requests
import os
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox14a64d8d03af4c9badd9c1f2ee2a0d0a.mailgun.org/messages",
		auth=("api", os.getenv("MG_API_KEY")),
		data={"from": "Excited User sandbox14a64d8d03af4c9badd9c1f2ee2a0d0a.mailgun.org",
			"to": ["weeshen90@gmail.com"],
			"subject": "Hello",
			"text": "Hi, I just donated to your Picture"})