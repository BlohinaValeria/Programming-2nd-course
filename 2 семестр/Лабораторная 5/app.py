from flask import Flask, render_template, request
import controller

app = Flask(__name__,template_folder='views')

@app.route('/', methods=['GET', 'POST'])
def index():
    return controller.index()

if __name__ == '__main__':
    app.run(debug=True)