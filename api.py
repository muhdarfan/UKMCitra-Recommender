from app import app
from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)