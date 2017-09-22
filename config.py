api_url = 'https://api.namecheap.com/xml.response'
api_url_sandbox = 'https://api.sandbox.namecheap.com/xml.response'

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

global_params = {
    'ApiUser': 'internalssl',
    'UserName': 'internalssl',
    #'ApiKey': 'af6d9e7b40cb40e7ac689e94ad9efea7',
    'ClientIp': '193.111.60.4'
}

global_params_sandbox = {
    'ApiUser': 'internalssl',
    'UserName': 'internalssl',
    'ApiKey': 'af6d9e7b40cb40e7ac689e94ad9efea7',
    'ClientIp': '193.111.60.4'
}

create_params = {
    'Command': 'namecheap.ssl.create',
    'Years': 1,
    'Type': 'PositiveSSL'
}

activate_params = {
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

subject = "/C=US/ST=Arizona/L=Phoenix/O=Namecheap, Inc./CN={}"
