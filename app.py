import os    # 乱数を設定するためインポート
from flask import Flask, render_template, session, redirect, url_for
from forms import LoginForm, RegisterForm

app = Flask(__name__)

# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)

# [index] index.htmlへのリンク
@app.route("/")
def index():
    return render_template("index.html")

    """
    ！！！以下ログイン関連ルーティング記述！！！
    ！！！フォルダ場所指定後、パス変更必須！！！
    ！！！おわったらけしてね！！！
    """
#ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    form2 = LoginForm()      #ファイルforms.pyのLoginFormクラスからオブジェクトを作る
    # POST
    if form2.validate_on_submit():    #validatorsの内容が表示されないなら、  
        return redirect(url_for('top'))     #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。
    # GETリクエストで、ifが通らなかった場合。form2オブジェクトを引数としてformにわたす。
    return render_template('login.html', form=form2)    #ログイン画面へ

# 登録
@app.route('/touroku', methods=['GET', 'POST'])
def touroku():
    form = RegisterForm()     #ファイルforms.pyのRegisterFormクラスからオブジェクトを作る
        #ファイルforms.pyのRegisterFormクラスからオブジェクトを作る
    # POST
    if form.validate_on_submit():    #validatorsの内容が表示されないなら、
        session['name'] = form.name.data           #セッションとして保存。登録完了ページで使う。
        session['password'] = form.password.data     
        
        return redirect(url_for('tourokuOK'))   #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。PRGパターンのR。
    
    # GETリクエストで、ifが通らなかった場合。formオブジェクトを引数としてformにわたす。
    return render_template('touroku.html', form=form)

# 登録完了画面
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('tourokuOK.html')

    """
    ！！！ログイン関連ここまで！！！
    ！！！おわったらけしてね！！！
    """
 
# top.htmlへのリンク
@app.route('/top')
def top():
    return render_template('top.html')    

# 以下game
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

# 直接実行された場合に、Flaskアプリケーションを実行し、サーバーを起動する記述
if __name__ == '__main__':
    app.run()