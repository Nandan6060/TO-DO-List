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
  all_done = len(tasks) > 0 and all(t.startswith("[x] ") for t in tasks)
  return render_template("index.html", tasks=tasks, count=len(tasks), all_done=all_done)

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

@app.route("/clear")
def clear():
  tasks.clear()
  save()
  return redirect("/")

@app.route("/toggle/<int:i>")
def toggle(i):
    if tasks[i].startswith("[x] "):
      tasks[i] = tasks[i][4:]
    else:
      tasks[i] = "[x] " + tasks[i]
      save()
    return redirect("/")

@app.route("/edit/<int:i>")
def edit(i):
  return render_template("edit.html", name=tasks[i], i=i)

@app.route("/update/<int:i>", methods=["POST"])
def update(i):
  new_text = request.form["task"].strip()
  if new_text:
    tasks[i] = new_text
    save()
  return redirect("/")

app.run(debug=True)