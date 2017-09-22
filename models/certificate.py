import xml.etree.ElementTree as ET


class Certificate:
    def __init__(self, xmldata):
        root = ET.fromstring(xmldata)
        command_response = root.find('{http://api.namecheap.com/xml.response}CommandResponse')
        ssl_create_result = command_response.find('{http://api.namecheap.com/xml.response}SSLCreateResult')
        ssl_certificate = ssl_create_result.find('{http://api.namecheap.com/xml.response}SSLCertificate')
        self.id = ssl_certificate.get('CertificateID')