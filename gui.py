import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Wireshark 2.0")
        #setting window size
        width=800
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_19=tk.Button(root)
        GButton_19["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_19["font"] = ft
        GButton_19["fg"] = "#000000"
        GButton_19["justify"] = "center"
        GButton_19["text"] = "START"
        GButton_19.place(x=10,y=10,width=112,height=41)
        GButton_19["command"] = self.GButton_19_command

        GButton_917=tk.Button(root)
        GButton_917["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_917["font"] = ft
        GButton_917["fg"] = "#000000"
        GButton_917["justify"] = "center"
        GButton_917["text"] = "STOP"
        GButton_917.place(x=10,y=70,width=112,height=41)
        GButton_917["command"] = self.GButton_917_command

        GLabel_889=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_889["font"] = ft
        GLabel_889["fg"] = "#333333"
        GLabel_889["justify"] = "left"
        GLabel_889["text"] = "Čas:"
        GLabel_889.place(x=10,y=120,width=54,height=41)

        GLabel_695=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "left"
        GLabel_695["text"] = "Zachyceno paketů:"
        GLabel_695.place(x=5,y=160,width=150,height=43)

        GLabel_895=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_895["font"] = ft
        GLabel_895["fg"] = "#333333"
        GLabel_895["justify"] = "left"
        GLabel_895["text"] = "0:2:36"
        GLabel_895.place(x=160,y=120,width=72,height=41)

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "left"
        GLabel_551["text"] = "5640"
        GLabel_551.place(x=160,y=160,width=70,height=41)

        GButton_278=tk.Button(root)
        GButton_278["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_278["font"] = ft
        GButton_278["fg"] = "#000000"
        GButton_278["justify"] = "center"
        GButton_278["text"] = "Výsledky"
        GButton_278.place(x=10,y=210,width=112,height=41)
        GButton_278["command"] = self.GButton_278_command

        GLabel_104=tk.Label(root)
        ft = tkFont.Font(family='Times',size=26)
        GLabel_104["font"] = ft
        GLabel_104["fg"] = "#333333"
        GLabel_104["justify"] = "center"
        GLabel_104["text"] = "Výsledky"
        GLabel_104.place(x=290,y=9,width=500,height=40)

        GLabel_754=tk.Label(root)
        GLabel_754["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_754["font"] = ft
        GLabel_754["fg"] = "#333333"
        GLabel_754["justify"] = "left"
        GLabel_754["text"] = "Poměr šifrovaných dat v síti [%]:"
        GLabel_754["relief"] = "flat"
        GLabel_754.place(x=290,y=70,width=260,height=42)

        GLabel_631=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_631["font"] = ft
        GLabel_631["fg"] = "#333333"
        GLabel_631["justify"] = "left"
        GLabel_631["text"] = "86"
        GLabel_631.place(x=570,y=70,width=57,height=42)

        GButton_355=tk.Button(root)
        GButton_355["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_355["font"] = ft
        GButton_355["fg"] = "#000000"
        GButton_355["justify"] = "center"
        GButton_355["text"] = "Graf protokolu"
        GButton_355.place(x=10,y=270,width=112,height=41)
        GButton_355["command"] = self.GButton_355_command

        GLabel_19=tk.Label(root)
        GLabel_19["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_19["font"] = ft
        GLabel_19["fg"] = "#333333"
        GLabel_19["justify"] = "left"
        GLabel_19["text"] = "Počet šifrovaných paketů:"
        GLabel_19.place(x=263,y=120,width=260,height=42)

        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "left"
        GLabel_768["text"] = "5098"
        GLabel_768.place(x=570,y=120,width=57,height=42)

        GLabel_648=tk.Label(root)
        GLabel_648["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_648["font"] = ft
        GLabel_648["fg"] = "#333333"
        GLabel_648["justify"] = "left"
        GLabel_648["text"] = " Celkový objem šifrovaných dat [B]:"
        GLabel_648.place(x=295,y=170,width=260,height=42)

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#333333"
        GLabel_622["justify"] = "left"
        GLabel_622["text"] = "3 456 543"
        GLabel_622.place(x=570,y=170,width=100,height=42)

        GLabel_942=tk.Label(root)
        ft = tkFont.Font(family='Times',size=26)
        GLabel_942["font"] = ft
        GLabel_942["fg"] = "#333333"
        GLabel_942["justify"] = "center"
        GLabel_942["text"] = "Detekované odchylky v provozu"
        GLabel_942.place(x=280,y=300,width=500,height=42)

        GLabel_248=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_248["font"] = ft
        GLabel_248["fg"] = "#333333"
        GLabel_248["justify"] = "left"
        GLabel_248["text"] = "Změna počtu šifrovaných paketů:"
        GLabel_248.place(x=288,y=350,width=260,height=42)

        GLabel_449=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_449["font"] = ft
        GLabel_449["fg"] = "#333333"
        GLabel_449["justify"] = "left"
        GLabel_449["text"] = "Ano"
        GLabel_449.place(x=590,y=350,width=57,height=42)

        GLabel_815=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_815["font"] = ft
        GLabel_815["fg"] = "#333333"
        GLabel_815["justify"] = "left"
        GLabel_815["text"] = "o 16 % více"
        GLabel_815.place(x=670,y=350,width=100,height=42)

        GLabel_180=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_180["font"] = ft
        GLabel_180["fg"] = "#333333"
        GLabel_180["justify"] = "left"
        GLabel_180["text"] = "Změna objemu šifrovaných dát"
        GLabel_180.place(x=278,y=390,width=260,height=42)

        GLabel_270=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_270["font"] = ft
        GLabel_270["fg"] = "#333333"
        GLabel_270["justify"] = "left"
        GLabel_270["text"] = "Ano"
        GLabel_270.place(x=590,y=390,width=57,height=42)

        GLabel_707=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_707["font"] = ft
        GLabel_707["fg"] = "#333333"
        GLabel_707["justify"] = "left"
        GLabel_707["text"] = "o 24 % více"
        GLabel_707.place(x=670,y=390,width=100,height=42)

    def GButton_19_command(self):
        print("command")


    def GButton_917_command(self):
        print("command")


    def GButton_278_command(self):
        print("command")


    def GButton_355_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
