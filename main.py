from flask import Flask

app = Flask(__name__)
@app.route("/")
def hell_word():
  return "hello World"

if __name__ == "__main__":
  print('inside')
  app.run(host='0.0.0.0', debug=True)