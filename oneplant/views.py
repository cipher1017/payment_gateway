from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse

from django_daraja.mpesa.core import MpesaClient


def index(request):
    import http.client
    import json

    conn = http.client.HTTPSConnection("sandbox.safaricom.co.ke")
    payload = json.dumps({
        "BusinessShortCode": 174379,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNzA1MTkxNzAx",
        "Timestamp": "20240705191701",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 2,
        "PartyA": 254748416480,
        "PartyB": 174379,
        "PhoneNumber": 254704936670,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    })
    headers = {
        'Authorization': 'Bearer 6G5WcZ8dxvr3XhpQEAiGQoeiNDmH',
        'Content-Type': 'application/json',
        'Cookie': 'incap_ses_1021_2742146=emvDB+/pkm9xhF7JMFIrDnv6jGYAAAAAfMeBDsog0gT6c0wBATiFYg==; incap_ses_1040_2742146=sn4LO52azEFATMJ0ktJuDip1imYAAAAArAvD5EPpP9Kv60BvOUio+w==; visid_incap_2742146=cSWlQ7K0ShqGbCIxGoZzUMdYbGYAAAAAQUIPAAAAAAAjWLaaNGm0jpab2IcdPlcg'
    }
    conn.request("POST", "/mpesa/stkpush/v1/processrequest", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    final_response = data.decode("utf-8")
    #print(data.decode("utf-8"))
    return HttpResponse(final_response)


def donate(request):
    return render(request, 'oneplant/index.html')
