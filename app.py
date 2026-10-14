from flask import Flask, request, redirect, render_template

app=Flask(__name__)

tasks = []

def save():
  f=open("tasks.txt","w")
  f.write("\n".join(tasks))
  f.close()

try:
  f=open("tasks.txt")
  tasks=f.read().splitlines()
  f.close()

except:
  pass

@app.route("/")
def home():
  return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
  new_tasks = request.form["task"]
  tasks.append(new_tasks)
  save()
  return redirect("/")

@app.route("/done/<int:i>")
def done(i):
  tasks.pop(i)
  save()
  return redirect("/")

app.run(debug=True)