
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


app_window = tk.Tk()
app_window.title("My Application")
app_window.geometry("500x500")


def open_file():
    filepath = askopenfilename(defaultextension=".txt",
                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "r") as input_file:
        text_editor.delete("1.0", tk.END)
        text_editor.insert("1.0", input_file.read())
    app_window.title(f"My Application - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt",
                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        output_file.write(text_editor.get("1.0", tk.END))
    app_window.title(f"My Application - {filepath}")

def exit_application():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app_window.destroy()


menu_bar = tk.Menu(app_window)
app_window.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Cut", command=lambda: app_window.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: app_window.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: app_window.focus_get().event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

text_editor = tk.Text(app_window, wrap="word")
text_editor.pack(expand=True, fill="both")

status_bar = ttk.Label(app_window, text="Ready", anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)


text_scroll = ttk.Scrollbar(text_editor, orient=tk.VERTICAL, command=text_editor.yview)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.config(yscrollcommand=text_scroll.set)


app_window.mainloop()
