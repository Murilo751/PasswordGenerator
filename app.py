from flask import Flask, render_template
from pathlib import Path
from gerator import gerado, getpasswordBase

app = Flask(__name__)


@app.route('/')
def geratorInterface():
    # Gera a senha usando a função gerado
    importpasswordBase = getpasswordBase()
    password = gerado(importpasswordBase, )


    # Passa a senha para o template para ser exibida
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
