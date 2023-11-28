# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Igor" 
    idade = "17" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai


# defina a rota para a página da mãe


# defina a rota para a página do amigo


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
