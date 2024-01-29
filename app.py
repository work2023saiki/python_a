from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template('top.html')

@app.route('/puzzle') 
def puzzle():
    return render_template('15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('Dungeon.html')

@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('saturnvoyager.html')




if __name__ == '__main__':
    app.run()