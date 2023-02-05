from pathlib import Path
from tkinter import Tk, Canvas, Label, PhotoImage


def start_error_gui():
    window = Tk()

    # Properties
    window.geometry("400x120")
    window.configure(bg = "#F9FBFC")
    window.resizable(False, False)
    window.title('Programa contable')
    photo = PhotoImage(file = 'assets/icon.png')
    window.wm_iconphoto(False, photo)

    # Centered in the screen
    width = 400
    height = 120
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y-30))

    title = Label(text="Oops, ocurrio un error", font=("Inter", 27 * -1, 'bold'), fg="#01111A", bg="#F9FBFC")
    title.place(x=44, y=28)

    description = Label(text="El archivo seleccionado es muy complejo", font=("Inter", 16 * -1, 'bold'), fg="#01111A", bg="#F9FBFC")
    description.place(x=32, y=64, width=328, height=32)

    # # CANVAS CREATION
    # canvas = Canvas(
    #     window,
    #     bg = "#F9FBFC",
    #     height = 400,
    #     width = 120,
    #     bd = 0,
    #     highlightthickness = 0,
    #     relief = "ridge"
    # )

    # canvas.place(x = 0, y = 0)



    window.mainloop()