#pip install Flask==1.1.4
#pip install markupsafe==2.0.1

from flask import Flask
from produto import Produto

app = Flask(__name__)
lista = []
p1 = Produto('TV LG 50"', 2999, 10, id=1)
p2 = Produto('Smartphone LG', 1999, 20, id=2)
p3 = Produto('Computador i5', 5999, 5, id=3)

lista.append(p1)
lista.append(p2)
lista.append(p3)

@app.route('/')
def index():
    return '<h1>Olá Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)