# crypto-web-app

This web application can encrypt and decrypt the message.

![crypto_page](https://user-images.githubusercontent.com/69793689/128303477-9fa805ac-d419-4dcf-8226-192c79a47a23.PNG)

This web application consist of 2 pages:-
1) Encrypt Page :- To encrypt the message from textbox
2) Decrypt Page :- TO decrypt the encrypted message 

You can select which encryption or decryption to use from the dropdown box.

## How to setup locally?

### Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install the django and dependencies
```bash
pip3 install -r requirements.txt
```

### Run the web application at the local host http://127.0.0.1:8000/
```bash
python3 manage.py runserver
```
