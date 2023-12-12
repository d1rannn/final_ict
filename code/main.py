import tkinter
import tkinter.messagebox
import pickle

#root
root = tkinter.Tk()
root.title("Күнделікті Тапсырмалар")

root.resizable(height=False, width=False)

#Functions
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Тапсырма енгізгенің жөн!")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Тапсырма таңдағаның жөн!")


def delete_all_tasks():
    answer = tkinter.messagebox.askyesno(title="Warning!", message="Барлық тапсырмаларды кетіргің келе ме?")
    if answer == True:
        listbox_tasks.delete(0, tkinter.END)


def load_task():
    try:
        tasks = pickle.load(open("tasks.txt", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Тапсырмаларды сақтауға арналған файл жоқ секілді!")


def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.txt", "wb"))


def move_up():
    try:
        task_index = listbox_tasks.curselection()
        if not task_index:
            return
        for index in task_index:
            if index == 0:
                continue
            task = listbox_tasks.get(index)
            listbox_tasks.delete(index)
            listbox_tasks.insert(index - 1, task)
    except:
        pass

def move_down():
    try:
        task_index = listbox_tasks.curselection()
        if not task_index:
            return
        for index in task_index:
            task = listbox_tasks.get(index)
            listbox_tasks.delete(index)
            listbox_tasks.insert(index + 1, task)
    except:
        pass


# GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

frame_sort = tkinter.Frame(root)
frame_sort.pack()

entry_task = tkinter.Entry(frame_sort, width=25)
entry_task.pack(side=tkinter.LEFT)

frame_buttons1 = tkinter.Frame(root)
frame_buttons1.pack()

frame_buttons2 = tkinter.Frame(root)
frame_buttons2.pack()


scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=35)
listbox_tasks.pack()

listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

btn_move_up = tkinter.Button(frame_sort, text="▲", width=1, command=move_up)
btn_move_up.pack(side=tkinter.RIGHT)

btn_move_down = tkinter.Button(frame_sort, text="▼", width=1, command=move_down)
btn_move_down.pack(side=tkinter.RIGHT)

btn_add_task = tkinter.Button(frame_buttons1, text="Қосу", width=14, command=add_task)
btn_add_task.pack(side=tkinter.LEFT)

btn_delete_task = tkinter.Button(frame_buttons1, text="Кетіру", width=14, command=delete_task)
btn_delete_task.pack(side=tkinter.RIGHT)

btn_delete_all_tasks = tkinter.Button(frame_buttons2, text="Барлығын кетіру", width=14, command=delete_all_tasks)
btn_delete_all_tasks.pack(side=tkinter.LEFT)

btn_load_task = tkinter.Button(frame_buttons2, text="Жүктеу", width=14, command=load_task)
btn_load_task.pack(side=tkinter.RIGHT)

btn_save_task = tkinter.Button(root, text="Сақтау", width=32, command=save_task)
btn_save_task.pack()

#mainloop
root.mainloop()
