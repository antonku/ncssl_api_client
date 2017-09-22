url = {
    'production': 'https://api.namecheap.com/xml.response',
    'sandbox': 'https://api.sandbox.namecheap.com/xml.response',
}

general = {
    'production': {
        'ApiUser': 'internalssl',
        'UserName': 'internalssl',
        'ApiKey': '',
        'ClientIp': '193.111.60.4'
    },
    'sandbox': {
        'ApiUser': 'ssltool',
        'UserName': 'ssltool',
        'ApiKey': '',
        'ClientIp': '193.111.60.4'
    }
}

activate = {
    'Command': 'namecheap.ssl.activate',
    'CertificateID': None,
    'ApproverEmail': None,
    'csr': None,
    'WebServerType': 'apachessl',
    'HTTPDCValidation': 'False',
    'DNSDCValidation': 'False',
    'AdminJobTitle': 'SSL Support',
    'AdminFirstName': 'Anton',
    'AdminLastName': 'Ku',
    'AdminAddress1': '4600 East Washington Street Suite 305',
    'AdminCity': 'Phoenix',
    'AdminStateProvince': 'AZ',
    'AdminPostalCode': '85034',
    'AdminCountry': 'US',
    'AdminPhone': '+1.6613102107',
    'AdminEmailAddress': 'ssl@namecheap.com',
    'TechJobTitle': 'SSL Support',
    'BillingJobTitle': 'SSL Support'
}

getinfo = {
    'Command': 'namecheap.ssl.getInfo',
    'CertificateID': None,
}

create = {
    'Command': 'namecheap.ssl.create',
    'Years': 1,
    'Type': 'PositiveSSL'
}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

