# İçe aktarma
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


# Form sonuçları
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # seçilen resmi al
        selected_image = request.form.get("image-selector")

        # Görev #2. Metne ulaş
        selected_text_top = request.form.get("text-top")
        selected_text_bottom = request.form.get("text-bottom")
        # Görev #3. Metnin pozisyonuna ulaş
        selected_text_top_y = request.form.get("text-top-y")
        selected_text_bottom_y = request.form.get("text-bottom-y")
        # Görev #3. Metnin rengine ulaş
        color = request.form.get("color-selector")
        
        return render_template(
            "index.html",
            # Seçilen resmi göster
            selected_image = selected_image,
            # Görev #2. Metni göster
            selected_text_top = selected_text_top,
            selected_text_bottom = selected_text_bottom,
            # Görev #3. Rengi göster
            color = color,
            # Görev #3. Metnin posizyonunu göster
            selected_text_top_y = selected_text_top_y,
            selected_text_bottom_y = selected_text_bottom_y,
        )
    else:
        # İlk resmi varsayılan olarak ayarlamak
        return render_template("index.html", selected_image="logo.svg")


@app.route("/static/img/<path:path>")
def serve_images(path):
    return send_from_directory("static/img", path)


app.run(debug=True)
