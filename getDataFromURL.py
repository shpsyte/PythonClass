import urllib.request, json 
with urllib.request.urlopen("https://apps.shopify.com/product-upsell/reviews.json") as url:
    data = json.loads(url.read().decode())
    print(data)