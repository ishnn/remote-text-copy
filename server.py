from flask import Flask, request, render_template
import pyperclip

app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      user = request.form['nm']
      pyperclip.copy(str(user))
      return render_template('index.html')
   else:
      return render_template('index.html')
if __name__ == '__main__':
   app.run(host = '<Your IP address>', port=5000)
