from flask import Flask
import random

gercekler_listesi = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '<h1>Merhaba Dünya!</h1>'
@app.route("/")
def index():
    return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz! <br/> <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/rastgele_gercek")
def facts():
    return f'<p>{random.choice(gercekler_listesi)}</p>'

app.run(debug=True)