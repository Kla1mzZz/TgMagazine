import json
import paypalrestsdk

class Settings():
    def getAdminIds(self):
        with open('app/settings/settings.json') as f:
            template = json.load(f)

            for key, item in template.items():
                return item
    

paypalrestsdk.configure(
    {'mode': 'sandbox',  # sandbox или live
    'client_id': 'AYlZoB2sHZ2OjkzAlM3gGyUGGsbYrP-Nlf99YXKQGLEO66cNA-ECn6UnIp1CJCqSXKALY93ApmSZ076Y',
    'client_secret': 'EMRiyQOuiUjPm0iMZxadPKY871LtmftftinMTHooBjzpYABTK76jDodp5d2CgNiR_tcgHalgsS4DdPKO'})

def create_paypal_payment(item,price):
    payment = paypalrestsdk.Payment({
        'intent': 'sale',
        'payer': {
            'payment_method': 'paypal'
        },
        'redirect_urls': {
            'return_url': 'https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-7A6047684G5708708',
            'cancel_url': 'http://127.0.0.1:8000/payment/cancel'
        },
        'transactions': [{
            'item_list': {
                'items': [{
                    'name': item,
                    'sku': 'item',
                    'price': price,
                    'currency': 'USD',
                    'quantity': 1
                }]
            },
            'amount': {
                'total': price,
                'currency': 'USD'
            },
            'description': 'This is the payment transaction description.'
        }]
    })
    return payment