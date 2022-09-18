import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL() # instancia
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root' # qual é o usuario padrão
app.config['MYSQL_DATABASE_PASSWORD'] = 'rgd596' # qual é a senha
app.config['MYSQL_DATABASE_DB'] = 'bdaluno' # qual é o nome do banco de dados
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2' # ip do banco de dados
mysql.init_app(app) # vinculação do bando de dados com a aplicação, sendo que o 'mysql' setou com os parametros passado

@app.route('/')
def abrindo_info_aluno():
    return render_template('infoaluno.html')

@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    if nome and email and senha: # verificação se nem uma das variaveis são nulas
        conn = mysql.connect() # estabelecendo uma conecção com o mysql
        cursor = conn.cursor() # criase uma seção de comunicação com o banco de dados
        cursor.execute('insert into tbl_user (user_name, user_email, user_senha) VALUES(%s, %s, %s)',(nome, email, senha))
        conn.commit() # execução do comando
    return render_template('infoaluno.html')

@app.route('/lista', methods = ['POST', 'GET'])
def lista():
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute('select user_name, user_email, user_senha from tbl_user')
     data = cursor.fetchall() # faz a recuperação de dados
     conn.commit()
     return render_template('infolista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)