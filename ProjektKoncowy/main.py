from flask import Flask, render_template, request, redirect, url_for, jsonify
import random

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/przyczyna1")
def przyczyna1():
    return render_template("przyczyna1.html")

@app.route("/rozwiązanie1")
def rozwiązanie1():
    return render_template("rozwiązanie1.html")

@app.route("/przyczyna2")
def przyczyna2():
    return render_template("przyczyna2.html")

@app.route("/rozwiazanie2")
def rozwiazanie2():
    return render_template("rozwiazanie2.html")

@app.route("/twójpomysł")
def twójpomysł():
    return render_template("twójpomysł.html")


dobrawiadomość_lista = ["Kraje na całym świecie inwestują w energię słoneczną i wiatrową",
"W wielu miejscach prąd jest już tańszy niż z węgla, Prowadzone są akcje sadzenia miliardów drzew",
"Niektóre kraje np. Chiny zwiększyły powierzchnię lasów",
"Coraz więcej terenów jest chronionych",
"Sprzedaż aut elektrycznych szybko rośnie",
"Kraje zobowiązują się ograniczać emisję CO₂",
"Ludzie częściej segregują śmieci i oszczędzają energię",
"Popularne stają się style życia eko"]


@app.route("/losuj") 
def losuj():
    return jsonify({"DobraWiad": random.choice(dobrawiadomość_lista)})  

PLIK = "pomysly.txt"

def wczytaj_pomysly():
    try:
        with open(PLIK, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def zapisz_pomysl(pomysl):
    with open(PLIK, "a", encoding="utf-8") as f:
        f.write(pomysl + "\n")

@app.route("/twójpomysł", methods=["GET", "POST"])
def twójpomysł_post():
    if request.method == "POST":
        pomysl = request.form.get("pomysl")
        if pomysl:
            zapisz_pomysl(pomysl)

    pomysly = wczytaj_pomysly()
    return render_template("twójpomysł.html", pomysly=pomysly)


app.run(debug=True)