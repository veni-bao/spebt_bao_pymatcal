from tkinter import *
from PIL import ImageTk, Image

def forward(img_no, img_NO):
    
    global label
    global button_forward
    global button_back
    global button_exit

    label.pack_forget()

    label = label(image=List_images[img_no-1])
    label.pack(fill=BOTH, expand=True)
    button_forward = Button(root, text="forward", command=lambda: forward(img_no+1,img_NO))

    if img_no == img_NO:
        button_forward.config(state=DISABLED)

    button_back = Button(root, text="Back", command=lambda: back(img_no-1))

    button_back.pack(side=LEFT, fill=Y, expand=True)
    button_exit = Button(root, text="Exit", command=root.quit)
    button_exit.pack(side=RIGHT, fill=Y, expand=True)
    button_forward.pack(side=RIGHT, fill=Y, expand=True)

def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.pack_forget()

    label = label(image=List_images[img_no - 1])
    label.pack(fill=BOTH, expand=True)
    button_forward = Button(root, text="forward", command=lambda: forward(img_no+1,img_NO))
    button_back = Button(root, text="Back", command=lambda: back(img_no - 1))

    if img_no == 1:
        button_back.config(state=DISABLED)

    label.pack(fill=BOTH, expand=True)
    button_back.pack(side=LEFT, fill=Y, expand=True)
    button_exit.pack(side=RIGHT, fill=Y, expand=True)
    button_forward.pack(side=RIGHT, fill=Y, expand=True)

def Image_Viewer(img_NO):
    
    root = Tk()
    root.title("Image Viewer")
    root.geometry("700x700")
    List_images = [img_NO]
    image_no_1=ImageTk.PhotoImage(Image.open("test_20240722_182815_data_det_000.png"))
    
    for i in range(img_NO):
        
        image_no_temp = ImageTk.PhotoImage(Image.open("test_20240722_182815_data_det_000.png"))
        List_images.append(image_no_temp)
        label = Label(root, image=image_no_temp)
        label.image = image_no_temp  # 保持图像引用，以便在需要时更新
        
    label = label(image=image_no_1)
    label.pack(fill=BOTH, expand=True)

    button_back = Button(root, text="Back", command=back, state=DISABLED)
    button_exit = Button(root, text="Exit", command=root.quit)
    button_forward = Button(root, text="forward", command=lambda: forward(img_no+1,img_NO))

    button_back.pack(side=LEFT, fill=Y, expand=True)
    button_exit.pack(side=RIGHT, fill=Y, expand=True)
    button_forward.pack(side=RIGHT, fill=Y, expand=True)

    root.mainloop()
