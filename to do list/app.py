from flask import Flask, request, redirect

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
  page=""
  for i in range(len(tasks)):
    page+= "<p>" + tasks[i] +"<a href='/done/" + str(i) + "'>Done</a></p>"
  page += """ <form action="/add" method="post">
        <input name="task">
        <button>Add</button>
    </form>
    """
  return page

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