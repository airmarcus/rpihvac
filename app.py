from flask import Flask, render_template, jsonify, request, redirect
import os
import fileinterface

app = Flask(__name__)
import movedampers

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/open_game_room")
def open_game_room():
    movedampers.move('gameroom', 100)

@app.route("/close_game_room")
def close_game_room():
    movedampers.move('gameroom', 0)

@app.route("/open_master")
def open_master():
    movedampers.move('master', 100)

@app.route("/close_master")
def close_master():
    movedampers.move('master', 0)

@app.route("/refresh_positions")
def refresh_positions():
    print(jsonify(positions = fileinterface.getallpositions()))
    return jsonify(positions = fileinterface.getallpositions())

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5002)
