tasks=[]

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

while True:
  choice=input("Choice option: \n 1. Add\n 2. View\n 3. Task completed\n 4. Exit\n")

  if choice=="1":
    task=input("Ënter your task: ")
    tasks.append(task)
    save()
  elif choice=="2":
    print("Your tasks: ")
    for i in range(len(tasks)):
      print(i+1, tasks[i])
  elif choice=="3":
    try:
      num=int(input("Enter task number which you have completed: "))
      tasks.pop(num-1)
      save()
      print("Task completed")
    except:
      print("Invalid task number")

    
  elif choice=="4":
    print("Exiting")
    break


  