import requests
import json


def get_some_data():
    url = 'https://api.dev.pumped.ai/graphql'

    data = {"operationName": "customerPaymentInfo",
           "variables": {},
           "query":
               "query customerPaymentInfo "
               "{\n  customerPaymentInfo "
               "{\n    paymentMethods "
               "{\n      id\n      cardType\n      expirationMonth\n      "
               "expirationYear\n      paymentMethodType\n      imageURL\n      "
               "last4\n      bin\n      accountHolderName\n      accountType\n      "
               "bankName\n      routingNumber\n    }\n    paymentClientToken\n  }\n}\n"}

    headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                              '.eyJvYmplY3RJZCI6IjVkNGQ0YzQwMDIwYWF'
                              'lMDAxMjg2OWRiZCIsIm9iamVjdFJvbGVJZCI'
                              '6IjVkNGQ0YzQwMDIwYWFlMDAxMjg2OWRiZSI'
                              'sInJvbGUiOiJjdXN0b21lciIsImlzRW1haWxD'
                              'b25maXJtZWQiOm51bGwsImlhdCI6MTU2NTM1M'
                              'zQzNCwiZXhwIjoxNTY1NDM5ODM0fQ.t-dzsNV'
                              'TAkbmiwXj37OQS2EaI1J_ZRn0q9xbuS34Iyw',
               'Content-Type': 'application/json',
               # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 1'
               #               '0_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
               #               'Chrome/50.0.2661.102 Safari/537.36'
               }

    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


print(get_some_data())
