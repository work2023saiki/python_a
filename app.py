from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template('top.html')

@app.route('/puzzle') 
def puzzle():
    return render_template('game/15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('game/Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('game/FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('game/ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('game/Dungeon.html')


@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('game/FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('game/Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('game/CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('game/saturnvoyager.html')

@app.route('/EggCatch') 
def EggCatch():
    return render_template('game/EggCatch.html')


@app.route('/chase') 
def chase():
    return render_template('game/Chase.html')

@app.route('/Billiard') 
def Billiard():
    return render_template('game/Billiard.html')

@app.route('/yasai') 
def yasai():
    return render_template('game/yasai.html')

if __name__ == '__main__':
    app.run()