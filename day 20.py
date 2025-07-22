from urllib.request import urlopen

url = 'https://example.com'  # You can replace this with any URL
response = urlopen(url)
html = response.read().decode('utf-8')

print("Webpage Content:\n")
print(html)
