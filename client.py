

# this will query your fancy new python tls web server


import requests

r = requests.get('https://localhost:10023', verify=False)

print(r.content.decode())

# alternatively you can even use your WEB BROWSER!!!!!
# you'll have to add a security exception for the localhost though,
# because it's a self-signed certificate and all.

#import webbrowser
#webbrowser.open('https://localhost:10023')

# enjoy

input('press Enter to continue')

