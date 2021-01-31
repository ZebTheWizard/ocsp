import re


class Cert:

    BEGIN = "-----BEGIN CERTIFICATE-----"
    END = "-----END CERTIFICATE-----"

    def __init__(self, content):
        self.content = content

    @staticmethod
    def parseCerts(text):
        return list(
            map(lambda match: Cert(match.strip()),
                re.findall(rf'{Cert.BEGIN}([^-]+)', text)
                )
        )

    def __str__(self):
        return "%s\n%s\n%s" % (Cert.BEGIN, self.content, Cert.END)
