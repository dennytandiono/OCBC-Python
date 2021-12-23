from flask import Flask
app = Flask(__name__)

# @app.route('/shoes')
# @app.route('/food')
# @app.route('/shop')
# @app.route('/')
# def hello_world():
# def hello_world(page_name):
#     return 'Hello, World! <br/>  <h1>Hello World!</h1>'
#     html = 'Hello World! <br/> <h1>Hello World!</h1>'
#     html += 'this is {} page'.formal(page_name)
#     return html

@app.route('/<page_name>')
def hello_world(page_name):
     html = 'Hello World! <br/> <h1>Hello World!</h1>'
     html += f'this is {page_name} page'
     return html

@app.route('/hello')
def hello():
     return 'Hello, World! <br/>  <h1>this is hello home</h1>'
     
if __name__ == '__main__':    
    app.run()
