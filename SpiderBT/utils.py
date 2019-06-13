from django.conf import settings
import urllib, json, string, random

import markdown as md

def google_recaptcha(request):
	recaptcha_response = request.POST.get('g-recaptcha-response')
	google_url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
	}

	data = urllib.parse.urlencode(values).encode()
	req =  urllib.request.Request(google_url, data=data)
	response = urllib.request.urlopen(req)
	result = json.loads(response.read().decode())

	return result

# https://python-markdown.github.io/extensions/
def convert_to_markdown(value):
	return md.markdown(value, extensions=['markdown.extensions.fenced_code'])