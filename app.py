from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template('top.html')

@app.route('/puzzle') 
def puzzle():
    return render_template('login/templates/games/15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('login/templates/games/Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('login/templates/games/FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('login/templates/games/ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('login/templates/games/Dungeon.html')


@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('login/templates/games/FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('login/templates/games/Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('login/templates/games/CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('login/templates/games/saturnvoyager.html')

@app.route('/EggCatch') 
def EggCatch():
    return render_template('login/templates/games/EggCatch.html')


@app.route('/chase') 
def chase():
    return render_template('login/templates/games/Chase.html')

@app.route('/Billiard') 
def Billiard():
    return render_template('login/templates/games/Billiard.html')

@app.route('/yasai') 
def yasai():
    return render_template('login/templates/games/yasai.html')

if __name__ == '__main__':
    app.run()