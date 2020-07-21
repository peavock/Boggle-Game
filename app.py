from flask import Flask, request, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = "emmadog1223"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

GAME_BOARD = "game_board"
# HIGH_SCORE=0


@app.route('/')
def welcome():
    """render welcome page with initial start button"""
    return render_template("welcome.html")

@app.route('/begin', methods=["POST"])
def load_board():
    """redirects but creates a new board game and gets a count of the session"""
    session[GAME_BOARD]=boggle_game.make_board()
    
    # Keep a count of how many times a new game is started
    session['count'] = session.get('count', 0) + 1

    return redirect ("/board-game")

@app.route('/board-game')
def load_game():
    """shows the board game and allows for user interaction"""
    board_game = session.get(GAME_BOARD)
   #get high score - if first time high score is 0
    session["HIGH_SCORE"]=session.get("HIGH_SCORE",0)
    high_score=session.get("HIGH_SCORE")
    return render_template("board_game.html", board_game = board_game, high_score=high_score)



# This route uses url notation for the word
@app.route('/api/check-word/<word>')
def check_word(word):
    """checks if a word is valid / on board and returns the result"""
    board_game = session.get(GAME_BOARD)
    result = Boggle().check_valid_word(board_game,word)

    return {"result":result}

@app.route('/api/check-score/<int:score>')
def check_score(score):
    """takes a parameter score, if a high score reassigns high score and returns high score"""

    high_score=max(score,session.get("HIGH_SCORE"))

    session["HIGH_SCORE"]=high_score

    return {"high-score": high_score}



#check high score and update session high score if score is higher
# @app.route('/api/high-score/<score>')
# # def check_high_score(score):
# #     high_score = 0
# #     if (score > high_score):
# #         session[HIGH_SCORE] = score
# #     return{"high-score": high_score}
# def return_high_score(score):
#     return {"high_score" : score}

    # if(score > high_score):
    #     # high_score=score
    #     high_score=score
    #     session["HIGH_SCORE"]=score

# This route accepts parameters
# @app.route("/api/check-word/")
# def check_word():
#     word = request.args.get("word")
#     board_game=session.get(GAME_BOARD)
#     result = Boggle().check_valid_word(board_game,word)

#     return {"result":result}    