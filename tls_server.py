
'''
https://docs.python.org/3/library/ssl.html#server-side-operation
'''

import ssl, socket

key_pass = b'passphrase'
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain( certfile='certificate.pem'
                        ,keyfile='key.pem'
                        ,password=key_pass)
                        
bindsocket = socket.socket()
bindsocket.bind(('localhost', 10023))
bindsocket.listen(5)

def deal_with_client(connstream):
    try:
        # because our cert is self-signed, this step will freak out with an error:
        # ssl.SSLError: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (_ssl.c:2460)
        # so we just say "oh well" and send a response anyway. 
        # you'll need to play around with it to get it to actually read the data.
        # sometimes "it just works" is good enough for learning purposes :)
        connstream.recv(1024)
    except:
        pass
    connstream.send(
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/html\r\n"
        b"\r\n"
        b"<html> congratulations you did it </html>"
    )
    
print('serving on https://localhost:10023')
while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
