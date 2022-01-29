import tkinter as tk

window = tk.Tk()
window.title("TKinter")
window.geometry('1080x720')

def click_button():   
	la = tk.Label(text=txt.get()) 
	la.grid(column=2, row=3)
	

txt = tk.Entry(window)
obj = tk.Button(window, text="Нажми меня", font=("Comic Sans MS", 10), bg = "black", fg = "blue", command = click_button)
txt.grid(column=0, row=1)
obj.grid(column=1, row=2)


window.mainloop()
