# Revoke Detection

The goal of this library is to write a cross-platform revoke detection command

# How to Install

1. Create a virtual environment `python3 -m venv venv`
1. Activate venv `source venv/bin/activate`
1. Install pip packages inside venv `pip install -r requirements.txt`

# Usage

- Get ocsp root cert (ex. apple) `python main.py root-cert --host=ocsp.apple.com --port=443`
- Get ocsp cert chain `python main.py chain --host=ocsp.apple.com --port=443`
- Get ocsp responder url `python main.py responder --host=ocsp.apple.com --port=443`
