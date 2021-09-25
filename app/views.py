import http.client
import urllib.parse
import json
from django.http import HttpResponse

def get_data(request):
	address_data = urllib.parse.quote_plus(request.POST['address']);

	conn = http.client.HTTPSConnection("nhf.finance")
	payload = 'address='+address_data
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}
	conn.request("POST", "/data", payload, headers)
	res = conn.getresponse()

	status = res.status
	data = res.read()
	decod_res = json.loads(data)
	data = json.dumps(decod_res)

	return HttpResponse(data, status=status, content_type="text/json")

def get_api(request):
	value_data = urllib.parse.quote_plus(request.POST['value']);
	type_data = urllib.parse.quote_plus(request.POST['type']);

	conn = http.client.HTTPSConnection("nhf.finance")
	payload = 'value='+value_data+'&type='+type_data
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}

	conn.request("POST", "/api", payload, headers)
	res = conn.getresponse()

	status = res.status;
	data = res.read()
	decod_res = json.loads(data)
	data = json.dumps(decod_res)

	return HttpResponse(data, status=status, content_type="text/json")