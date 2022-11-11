# Astralyx Pay python library

You can [get API token here](https://t.me/crypt_nick)!

```py
invoice = Invoices("YOUR_TOKEN_HERE").createInvoice(
    user_wallet="1NV01C3-2W4LL31-fjawifjhaf92fha2f", # Wallet address of the invoiced user
    amount=10.5,
    callback_url="https://example.com/callback"
)
print(invoice)

info = Invoices("YOUR_TOKEN_HERE").getInvoice(invoice['data']['invoice_id'])
print(info)
```
