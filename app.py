import original_py.dice as dice
import original_py.blackjack as blackjack
import original_py.poker as poker
import original_py.scratchers as scratchers
import original_py.roulette as roulette
import original_py.slot_machines as slot_machines
import original_py.horse_racing as horse_racing
import requests
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/blackjack")
def blackjack():
    return render_template("blackjack.html")


@app.route("/dice")
def dice():
    return render_template("dice.html")


@app.route("/poker")
def poker():
    return render_template("poker.html")


@app.route("/roulette")
def roulette():
    return render_template("roulette.html")


@app.route("/scratchers")
def scratchers():
    return render_template("scratchers.html")


if __name__ == "__main__":
    app.run(debug=True)
