from tkinter import *
from tkinter import messagebox, filedialog
import cv2
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
import time
import cc as cc_farm

from PIL import ImageTk,Image

whatsapp_btn = "Scan QR"

def scanned():

    whatsapp.destroy()

    # ------------------- Intialising Web Driver and Open Whatsapp ---------------------------
    driver = webdriver.Chrome(executable_path="webdrivers/chromedriver.exe")
    driver.get('https://web.whatsapp.com/')
    # ----------------------------------------------------------------------------------------

    gui = Tk()
    gui.geometry('1000x500+430+250')

    def search_con():
        try:
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contactName.get()))
            cname=contactName.get()
            user.click()
            messagebox.showinfo("Success", "Successfully Contact found in your Whatsapp - "+contactName.get(), parent=gui)
            gui.destroy()

            ###############################

            def open_img():
                # Select the Image name  from a folder
                x = openfilename()

                # opens the image
                img = Image.open(x)

                # resize the image and apply a high-quality down sampling filter
                img = img.resize((450, 250), Image.ANTIALIAS)

                # PhotoImage class is used to add image to widgets, icons etc
                img = ImageTk.PhotoImage(img)

                # create a label
                panel = Label(detect_animal, image=img)

                # set the image as img
                panel.image = img
                panel.place(x=250, y=150)

            def openfilename():
                filename = filedialog.askopenfilename(title='"pen')
                return filename

            def video_play():
                cc_farm.cc_farm()

            def run_program():

                ###############################################

                vidcap = cv2.VideoCapture("test3.avi")
                success, image = vidcap.read()
                calc_count = 0
                count = 0
                while success:
                    success, image = vidcap.read()
                    if (calc_count == 60):
                        calc_count = 0

                        reqpath = "frame" + str(count) + ".jpg"
                        cv2.imwrite("frame%d.jpg" % count, image)

                        name = cname
                        filepath = os.getcwd() + "\\" + reqpath

                        time.sleep(10)

                        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                        user.click()

                        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                        attachment_box.click()

                        image_box = driver.find_element_by_xpath(
                            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                        image_box.send_keys(filepath)

                        sleep(3)
                        try:
                            driver.find_element_by_xpath(
                                "/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]").send_keys(
                                Keys.ENTER)
                            count = 0
                        except:
                            print("Excepted")
                    print(calc_count)

                    calc_count = calc_count + 1
                count += 1

                ##################################################################
                messagebox.showinfo("Success", "Images sent to farmer successfully", parent=detect_animal)
                detect_animal.destroy()
                #################################### code for video plating

                ##################################################################




            ################################


            detect_animal = Tk()

            detect_animal.geometry('1000x500+430+250')

            # Allow Window to be resizable
            detect_animal.resizable(width=True, height=True)

            detect_animal.title("FARM PROTECTION")
            Label(detect_animal,text="FARM PROTECTION FROM ANIMAL INTRUSION", fg="black", font=('Comic Sans MS', 15)).place(x=200,
                                                                                                              y=1)

            Label(detect_animal,text="Select the intial image of the Farm", fg="black", font=('Comic Sans MS', 15)).place(x=300, y=60)

            # Create a button and place it into the window using grid layout
            Button(detect_animal, text='open image',command=open_img).place(x=450, y=100)

            Button(detect_animal, text="Visualise",command=video_play).place(x=600, y=450)
            Button(detect_animal, text="send Whats App Images", command=run_program).place(x=400, y=450)


            detect_animal.mainloop()

        except:
            messagebox.showerror("Error",f"Contact not Found - {str(contactName.get())}" ,parent=gui)
            print("Exception")



    gui.title("Farm Protection")
    Label(text="Farm Protection", fg="black", font=('Comic Sans MS', 15)).place(x=400, y=1)

    canvas = Canvas(gui, width=460, height=500)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("contact.jpeg"))
    canvas.create_image(50, 50, anchor=NW, image=img)

    # -------- Enter Whatsapp Contact   Name ------

    Label(text="Enter Contact Name --->  ", font=13).place(x=100, y=350)
    contactName = StringVar()
    Entry(gui, justify="center", textvariable=contactName).place(x=330, y=350)

    # --------------------------------

    # ---------------- Contact Search Button ---------------

    Button(gui, text="Search Contact",command=search_con).place(x=470, y=350)

    # ------------------------------------------------------

    gui.mainloop()



whatsapp = Tk()
canvas = Canvas(whatsapp, width = 460, height = 500)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("gen.jpeg"))
canvas.create_image(50, 50, anchor=NW, image=img)
Button(whatsapp,text=whatsapp_btn,command=scanned,width=20,height=2,bg="black",fg="white").place(x=170,y=400)

whatsapp.title("Scan QR")


whatsapp.mainloop()


# -------------------------------------------------------------------------------------------------------------------