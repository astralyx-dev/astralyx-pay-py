import requests

class Invoices:

    payment_domain = "https://pay.astralyx.dev"

    def __init__(self, token):
        self.token = token

    def make_request(self, method, parameters):
        parameters['token'] = self.token
        res = requests.get(f"{payment_domain}/api/{method}", params=parameters)
        if res.status_code == 200:
            return res.json()
        else:
            return False
    
    def createInvoice(self, user_wallet, amount, callback_url):
        return self.make_request("createInvoice", {
            "sender": user_wallet, 
            "amount": amount, 
            "callback_url": callback_url
        })

    def getInvoice(self, invoice_id):
        return self.make_request("getInvoice", {
            "id": invoice_id
        })
