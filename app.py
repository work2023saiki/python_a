from flask import Flask, render_template, session, redirect, url_for
from forms import InputForm, InputForm2 

app = Flask(__name__)

import os    # 乱数を設定するためインポート
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)


#ログイン
@app.route('/', methods=['GET', 'POST'])
def login():
    form2 = InputForm2()      #ファイルforms.pyのInputForm2クラスからオブジェクトを作る
    # POST
    if form2.validate_on_submit():    #InputForm2クラス、validatorsの内容が表示されないなら、
        
        return redirect(url_for('top'))     #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。
    # GETリクエストで、ifが通らなかった場合。form2オブジェクトを引数としてformにわたす。
    return render_template('login.html', form=form2)    #ログイン画面へ

# 登録
@app.route('/touroku', methods=['GET', 'POST'])
def touroku():
    form = InputForm()     #ファイルforms.pyのInputFormクラスからオブジェクトを作る
    # POST
    if form.validate_on_submit():    #InputFormクラス、validatorsの内容が表示されないなら、
        session['name'] = form.name.data           #セッションとして保存。他のページに移動してもsession['name']の中身はそのまま。
        session['password'] = form.password.data     
        session['confirm_password'] = form.confirm_password.data
        
        return redirect(url_for('tourokuOK'))   #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。PRGパターンのR。
    
    # GETリクエストで、ifが通らなかった場合。formオブジェクトを引数としてformにわたす。
    return render_template('touroku.html', form=form)

# 登録完了画面
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('tourokuOK.html')


@app.route('/top')
def top():
    return render_template('top.html')    





@app.route('/puzzle') 
def puzzle():
    return render_template('login/templates/game/15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('login/templates/game/Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('login/templates/game/FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('login/templates/game/ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('login/templates/game/Dungeon.html')


@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('login/templates/game/FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('login/templates/game/Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('login/templates/game/CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('login/templates/game/saturnvoyager.html')

@app.route('/EggCatch') 
def EggCatch():
    return render_template('login/templates/game/EggCatch.html')


@app.route('/chase') 
def chase():
    return render_template('login/templates/game/Chase.html')

@app.route('/Billiard') 
def Billiard():
    return render_template('login/templates/game/Billiard.html')

@app.route('/yasai') 
def yasai():
    return render_template('login/templates/game/yasai.html')

if __name__ == '__main__':
    app.run()