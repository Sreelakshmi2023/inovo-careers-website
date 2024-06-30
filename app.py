from flask import Flask,render_template

app=Flask(__name__) #creatin a flask application . name---how particular script was invoked
@app.route("/")  # when a certain url is what should be written  
def hello_world():
  return render_template('home.html')


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)