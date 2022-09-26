import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rgd596'
app.config['MYSQL_DATABASE_DB'] = 'bdproduto'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def cadastro_produto():
    return render_template('cadproduto.html')

@app.route('/cdproduto', methods = ['POST', 'GET'])
def castro_pro():
    no_prod = request.form['NomeProd']
    pr_prod= request.form['PrecoProd']
    ca_prod = request.form['CateProd']
    if no_prod and pr_prod and ca_prod:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TB_PRODUTO (NOME_PRO, PRECO_PRO, CATEGORIA_PRO) VALUES(%s, %s, %s)',(no_prod, pr_prod, ca_prod))
        conn.commit()
    return render_template('cadproduto.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)