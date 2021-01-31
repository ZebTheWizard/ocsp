from app.cert import Cert
from app.helpers import *


class Ocsp():

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def getConnectionString(self):
        return "%s:%s" % (self.host, self.port)

    def getRootServerCert(self):
        result = cli(
            "openssl", "s_client", "-connect", self.getConnectionString())
        return Cert.parseCerts(result[0])[0]

    def getChain(self):
        result = cli("openssl", "s_client", "-showcerts",
                     "-connect", self.getConnectionString())
        return Cert.parseCerts(result[0])[1:]

    def getChainAsString(self):
        return "\n".join(list(map(str, self.getChain())))

    def getResponderUrl(self):
        serverCert = makeTempFile(
            "ocsp_getRootServerCert", self.getRootServerCert())
        result = cli("openssl", "x509", "-noout",
                     "-ocsp_uri", "-in", serverCert)
        return result[0].strip()
