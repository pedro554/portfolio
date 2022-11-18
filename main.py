from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
tecnologias = 'Python, Delphi'
facebook = 'https://www.facebook.com/profile.php?id=100002337424265'
linkedin = 'https://www.linkedin.com/in/pedro-henrique-canterle-viero-8278771b0/'
github = 'https://github.com/pedro554'
nome = 'Pedro Henrique Canterle Viero'

@app.route('/')
def index():
    return render_template('index.html', 
                            tecnologias=tecnologias,
                            facebook=facebook,
                            linkedin=linkedin, 
                            github=github,
                            nome=nome)

@app.route('/resumo')
def resumo():
    return render_template('resumo.html')

@app.route('/portfolio')
def portfolio(): 
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)