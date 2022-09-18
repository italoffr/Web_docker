import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rgd596'
app.config['MYSQL_DATABASE_DB'] = 'bdaluno'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def cadastrando_info_aluno():
    return render_template('cadastro.html')

@app.route('/salvar', methods = ['POST', 'GET'])
def salvando():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    if nome and cpf and endereco:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tb_aluno (us_nome, us_cpf, us_endereco) VALUES(%s, %s, %s)',(nome, cpf, endereco))
        conn.commit()
    return render_template('cadastro.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)