from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse

from django_daraja.mpesa.core import MpesaClient


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0748272022'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

    # conn = http.client.HTTPSConnection("sandbox.safaricom.co.ke")
    # payload = json.dumps({
    #     "BusinessShortCode": 174379,
    #     "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNzA1MTkxNzAx",
    #     "Timestamp": "20240705191701",
    #     "TransactionType": "CustomerPayBillOnline",
    #     "Amount": 2,
    #     "PartyA": 254748416480,
    #     "PartyB": 174379,
    #     "PhoneNumber": 254704936670,
    #     "CallBackURL": "https://mydomain.com/path",
    #     "AccountReference": "CompanyXLTD",
    #     "TransactionDesc": "Payment of X"
    # })
    # headers = {
    #     'Authorization': 'Bearer mDmo2ZZpNqdUeRaUDXNFHb8DdAVa',
    #     'Content-Type': 'application/json',
    #     'Cookie': 'incap_ses_1021_2742146=sMXnJxheHBF762aHLlIrDoUaiGYAAAAAxGv7wdZDpwZMZo/Zv/Bgnw==; visid_incap_2742146=cSWlQ7K0ShqGbCIxGoZzUMdYbGYAAAAAQUIPAAAAAAAjWLaaNGm0jpab2IcdPlcg'
    # }
    # conn.request("POST", "/mpesa/stkpush/v1/processrequest", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
    # final_response = data.decode("utf-8")
    # #print(data.decode("utf-8"))
    # return HttpResponse(final_response)


