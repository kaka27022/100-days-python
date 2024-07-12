from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)

# Miles entry

input = Entry(width=10)
input.insert(0, string="0")
input.place(x=200, y=50)

def convert():
    miles = input.get()
    km = int(miles) * 1.6
    return km

def button_clicked():
    result = round(convert(), 2)
    write_result.config(text=result)

# Coisas escritas
write_miles = Label(text="Miles")
write_miles.place(x=300, y=50)

write_is_equal_to = Label(text="is equal to")
write_is_equal_to.place(x=100, y=85)

write_result = Label(text="0", font=("Arial", 20, "bold"))
write_result.place(x=220, y=80)

write_km = Label(text="Km")
write_km.place(x=310, y=85)

button = Button(text="Calculate", command=button_clicked)
button.place(x=200, y=120)

window.mainloop()