import tkinter as tk

window = tk.Tk()

def set_values(diff, hin, mis):
    if diff == "Easy":
        diff = 1
    if diff == "Medium":
        diff = 2
    if diff == "Hard":
        diff = 3
    if diff == "Impossible":
        diff = 4
    return diff, hin, mis


diff = hin = mis = 0
difficulty = ["Easy", "Medium", "Hard", "Impossible"]
hints = [i for i in range(1, 11)]
mistakes = [i for i in range(1, 11)]

difficute = tk.StringVar(window)
difficute.set(difficulty[1])

hint = tk.StringVar(window)
hint.set(hints[2])

mistake = tk.StringVar(window)
mistake.set(mistakes[2])

diff_lbl = tk.Label(window, text="Difficulty")
diff_lbl.pack()
difficulty_dropdown = tk.OptionMenu(window, difficute, *difficulty)
difficulty_dropdown.pack()
hint_lbl = tk.Label(window, text="Hints")
hint_lbl.pack()
hints_dropdown = tk.OptionMenu(window, hint, *hints)
hints_dropdown.pack()
mis_lbl = tk.Label(window, text="Mistakes Allowed")
mis_lbl.pack()
mistakes_dropdown = tk.OptionMenu(window, mistake, *mistakes)
mistakes_dropdown.pack()


def ok():
    global diff, hin, mis
    diff, hin, mis = set_values(difficute.get(), mistake.get(), hint.get())
    window.destroy()
    window.quit()


button = tk.Button(window, text="OK", command=ok)
button.pack()

window.mainloop()
