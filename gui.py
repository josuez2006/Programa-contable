from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from main import find_input_path, find_output_path, convert_file
from error_gui import start_error_gui


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Josue\Desktop\Learning Python\assets\elements")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def set_field_1():
    path = find_input_path()
    set_pdf_placeholder(path)

def set_field_2():
    path = find_output_path()
    set_excel_placeholder(path)

def send():
    window.destroy()

    try:
        convert_file()
    except:
        start_error_gui()

window = Tk()

# Properties
window.geometry("600x378")
window.configure(bg = "#F9FBFC")
window.resizable(False, False)
window.title('Programa contable')
photo = PhotoImage(file = 'assets/icon.png')
window.wm_iconphoto(False, photo)

# Centered in the screen
width = 600
height = 378
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y-30))



# CANVAS CREATION
canvas = Canvas(
    window,
    bg = "#F9FBFC",
    height = 378,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)



# TITLE
canvas.create_text(
    32.0,
    28.0,
    anchor="nw",
    text="Convierte y extrae de tu Pdf a un Excel",
    fill="#01111A",
    font=("Inter", 27 * -1, 'bold'),
    width=340
)


# INPUT FIELD #1

# LABEL #1
canvas.create_text(
    32.0,
    121.0,
    anchor="nw",
    text="Archivo Pdf",
    fill="#01111A",
    font=("Inter", 19 * -1, 'bold')
)

# FIELD #1
field_image_1 = PhotoImage(
    file=relative_to_assets("field_1.png"))
field_1 = Button(
    image=field_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= set_field_1,
    relief="flat"
)
field_1.place(
    x=32.0,
    y=148.0,
    width=382.0,
    height=40.0
)

#PLACEHOLDER #1
placeholder_1 = Label(window, text='', font=("Inter", 13 * -1), fg="#01111A", bg="#9FDAF5", anchor='nw')
placeholder_1.place(x=40.0, y=156.0, width=362.0, height=24.0)

def set_pdf_placeholder(text):
    placeholder_1["text"] = text


# BUTTON FIELD #1
button_field_image_1 = PhotoImage(
    file=relative_to_assets("field_button_1.png"))
button_field_1 = Button(
    image=button_field_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=set_field_1,
    relief="flat"
)
button_field_1.place(
    x=422.0,
    y=148.0,
    width=146.0,
    height=40.0
)




# INPUT FIELD #2

# LABEL #1
canvas.create_text(
    32.0,
    207.0,
    anchor="nw",
    text="Carpeta de archivo Excel resultante",
    fill="#01111A",
    font=("Inter", 19 * -1, 'bold')
)



# FIELD #2
field_image_2 = PhotoImage(
    file=relative_to_assets("field_2.png"))
field_2 = Button(
    image=field_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=set_field_2,
    relief="flat"
)
field_2.place(
    x=32.0,
    y=234.0,
    width=382.0,
    height=40.0
)

# PLACEHOLDER #2
placeholder_2 = Label(window, text="", font=("Inter", 13 * -1), fg="#01111A", bg="#9FDAF5", anchor='nw')
placeholder_2.place(x=40.0, y=242.0, width=362.0, height=24.0)

def set_excel_placeholder(text):
    placeholder_2["text"] = text

# BUTTON FIELD #2
button_field_image_2 = PhotoImage(
    file=relative_to_assets("field_button_2.png"))
button_field_2 = Button(
    image=button_field_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=set_field_2,
    relief="flat"
)
button_field_2.place(
    x=422.0,
    y=234.0,
    width=146.0,
    height=40.0
)



# SENT BUTTON
button_sent_image = PhotoImage(
    file=relative_to_assets("button.png"))
button_sent = Button(
    image=button_sent_image,
    borderwidth=0,
    highlightthickness=0,
    command=send,
    relief="flat"
)
button_sent.place(
    x=32.0,
    y=306.0,
    width=209.0,
    height=40.0
)



window.mainloop()