from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('req.html')



@app.route('/ccc', methods=['POST'])
def eye():
    name=request.form['name']
    number=request.form['number']
    return render_template('reqqq.html',name=name,number=number)
   






if __name__ == '__main__':
    app.run(debug=True)