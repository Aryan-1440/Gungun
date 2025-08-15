from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    love_quote = """GunGun,<br>
    Last day, when we were on our first date, it was one of the most unforgettable moments of my life.<br>
    I was so nervous… but then, you held my arms in your hands, and in that instant, it felt like my soul had left my body.<br>
    I can’t even explain it—it was like a dream.<br><br>

    The first time I held your hand in mine, it felt surreal… almost delusional. Every second we spent together that day, I loved it beyond words.<br>
    I believe in you… I believe in us. And I still remember the words I once told you—<br>
    I don’t know if this is love or not… but if I ever want to find love, I know I will find it in you, as a person.<br><br>

    And the only thing I wanted to say to you in my shayrana andaaz in that moment was—<br><br>

    <em>"Jab bhi kahin baadal garajte hain,<br>
    to samajh leta hoon tumne unse kuch kaha hoga,<br>
    Sanam… hamari is mulaqat ko,<br>
    shayad is qaynaat ne har boond mein likha hoga."</em>
    """
    return render_template("index.html", love_quote=love_quote)

if __name__ == "__main__":
    app.run(debug=True)
