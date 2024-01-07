# İçeri aktarma
from flask import Flask, render_template,request, redirect
# Veri tabanı kütüphanesini içeri aktarma
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# SQLite'a bağlanma
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)

# Görev #1. Bir veri tabanı tablosu oluştur
class Card(db.Model):
    ### Alanları oluşturma ###
    # kimlik numarası (id)
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Alt başlık
    subtitle = db.Column(db.String(300), nullable=False)
    # Metin
    text = db.Column(db.Text, nullable=False)

    # Nesneyi ve id'sine göre yazdırma
    def __repr__(self):
        return f'<Card {self.id}>'


# Sayfa içeriğini çalıştırma
@app.route('/')
def index():
    ### DB objelerini göstermek ###
    # Görev #2. DB'deki objelerin index.html'de görüntülenmesi
    cards = Card.query.order_by(Card.id).all()
    
    return render_template('index.html', cards=cards)

# card sayfasını gösterme
@app.route('/card/<int:id>')
def card(id):
    # Görev #2. id'sine göre doğru kartı göster
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Sayfayı çalıştırma ve kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Görev #2. DB'de veri saklama yöntemi oluşturma
        card = Card(title=title, subtitle=subtitle, text=text)
        # db fonksiyonlarını kullanarak değişikleri kaydetmek
        db.session.add(card)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)