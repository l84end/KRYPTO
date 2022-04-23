import tkinter as tk
import tkinter.font as tkFont
import main
from threading import Thread
import time

class App:
    def __init__(self, root):

        self.capture_time = ""
        self.pocet_paketu = 0

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

        GButton_start=tk.Button(root)
        GButton_start["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_start["font"] = ft
        GButton_start["fg"] = "#000000"
        GButton_start["justify"] = "center"
        GButton_start["text"] = "START"
        GButton_start.place(x=10,y=10,width=112,height=41)
        GButton_start["command"] = self.GButton_start_command

        # GButton_stop=tk.Button(root)
        # GButton_stop["bg"] = "#efefef"
        # ft = tkFont.Font(family='Times',size=12)
        # GButton_stop["font"] = ft
        # GButton_stop["fg"] = "#000000"
        # GButton_stop["justify"] = "center"
        # GButton_stop["text"] = "STOP"
        # GButton_stop.place(x=10,y=70,width=112,height=41)
        # GButton_stop["command"] = self.GButton_stop_command

        GLabel_cas=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_cas["font"] = ft
        GLabel_cas["fg"] = "#333333"
        GLabel_cas["justify"] = "left"
        GLabel_cas["text"] = "Čas:"
        GLabel_cas.place(x=10,y=120,width=54,height=41)

        GLabel_zachyceno=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_zachyceno["font"] = ft
        GLabel_zachyceno["fg"] = "#333333"
        GLabel_zachyceno["justify"] = "left"
        GLabel_zachyceno["text"] = "Zachyceno paketů:"
        GLabel_zachyceno.place(x=5,y=160,width=150,height=43)

        self.GLabel_cas_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.GLabel_cas_text["font"] = ft
        self.GLabel_cas_text["fg"] = "#333333"
        self.GLabel_cas_text["justify"] = "left"
        self.GLabel_cas_text["text"] = "0:0:0"
        self.GLabel_cas_text.place(x=160,y=120,width=72,height=41)

        self.GLabel_zachyceno_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.GLabel_zachyceno_text["font"] = ft
        self.GLabel_zachyceno_text["fg"] = "#333333"
        self.GLabel_zachyceno_text["justify"] = "left"
        self.GLabel_zachyceno_text["text"] = "0"
        self.GLabel_zachyceno_text.place(x=160,y=160,width=70,height=41)

        GButton_vysledky=tk.Button(root)
        GButton_vysledky["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_vysledky["font"] = ft
        GButton_vysledky["fg"] = "#000000"
        GButton_vysledky["justify"] = "center"
        GButton_vysledky["text"] = "Výsledky"
        GButton_vysledky.place(x=10,y=210,width=112,height=41)
        GButton_vysledky["command"] = self.GButton_vysledky_command

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

        GLabel_pomer_dat_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_pomer_dat_text["font"] = ft
        GLabel_pomer_dat_text["fg"] = "#333333"
        GLabel_pomer_dat_text["justify"] = "left"
        GLabel_pomer_dat_text["text"] = "86"
        GLabel_pomer_dat_text.place(x=570,y=70,width=57,height=42)

        GButton_graf_protokolu=tk.Button(root)
        GButton_graf_protokolu["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=12)
        GButton_graf_protokolu["font"] = ft
        GButton_graf_protokolu["fg"] = "#000000"
        GButton_graf_protokolu["justify"] = "center"
        GButton_graf_protokolu["text"] = "Graf protokolu"
        GButton_graf_protokolu.place(x=10,y=270,width=112,height=41)
        GButton_graf_protokolu["command"] = self.GButton_graf_protokolu_command

        GLabel_19=tk.Label(root)
        GLabel_19["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_19["font"] = ft
        GLabel_19["fg"] = "#333333"
        GLabel_19["justify"] = "left"
        GLabel_19["text"] = "Počet šifrovaných paketů:"
        GLabel_19.place(x=263,y=120,width=260,height=42)

        GLabel_pocet_sif_pkt_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_pocet_sif_pkt_text["font"] = ft
        GLabel_pocet_sif_pkt_text["fg"] = "#333333"
        GLabel_pocet_sif_pkt_text["justify"] = "left"
        GLabel_pocet_sif_pkt_text["text"] = "5098"
        GLabel_pocet_sif_pkt_text.place(x=570,y=120,width=57,height=42)

        GLabel_648=tk.Label(root)
        GLabel_648["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_648["font"] = ft
        GLabel_648["fg"] = "#333333"
        GLabel_648["justify"] = "left"
        GLabel_648["text"] = " Celkový objem šifrovaných dat [B]:"
        GLabel_648.place(x=295,y=170,width=260,height=42)

        GLabel_objem_sif_dat_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_objem_sif_dat_text["font"] = ft
        GLabel_objem_sif_dat_text["fg"] = "#333333"
        GLabel_objem_sif_dat_text["justify"] = "left"
        GLabel_objem_sif_dat_text["text"] = "3 456 543"
        GLabel_objem_sif_dat_text.place(x=570,y=170,width=100,height=42)

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

        GLabel_zmena_poct_sif_pkt_bool=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_zmena_poct_sif_pkt_bool["font"] = ft
        GLabel_zmena_poct_sif_pkt_bool["fg"] = "#333333"
        GLabel_zmena_poct_sif_pkt_bool["justify"] = "left"
        GLabel_zmena_poct_sif_pkt_bool["text"] = "Ano"
        GLabel_zmena_poct_sif_pkt_bool.place(x=590,y=350,width=57,height=42)

        GLabel_zmena_poc_sif_pkt_hodnota=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_zmena_poc_sif_pkt_hodnota["font"] = ft
        GLabel_zmena_poc_sif_pkt_hodnota["fg"] = "#333333"
        GLabel_zmena_poc_sif_pkt_hodnota["justify"] = "left"
        GLabel_zmena_poc_sif_pkt_hodnota["text"] = "o 16 % více"
        GLabel_zmena_poc_sif_pkt_hodnota.place(x=670,y=350,width=100,height=42)

        GLabel_180=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_180["font"] = ft
        GLabel_180["fg"] = "#333333"
        GLabel_180["justify"] = "left"
        GLabel_180["text"] = "Změna objemu šifrovaných dát"
        GLabel_180.place(x=278,y=390,width=260,height=42)

        GLabel_zmena_obj_sif_dat_bool=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_zmena_obj_sif_dat_bool["font"] = ft
        GLabel_zmena_obj_sif_dat_bool["fg"] = "#333333"
        GLabel_zmena_obj_sif_dat_bool["justify"] = "left"
        GLabel_zmena_obj_sif_dat_bool["text"] = "Ano"
        GLabel_zmena_obj_sif_dat_bool.place(x=590,y=390,width=57,height=42)

        GLabel_zmena_obj_sif_dat_hodnota=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_zmena_obj_sif_dat_hodnota["font"] = ft
        GLabel_zmena_obj_sif_dat_hodnota["fg"] = "#333333"
        GLabel_zmena_obj_sif_dat_hodnota["justify"] = "left"
        GLabel_zmena_obj_sif_dat_hodnota["text"] = "o 24 % více"
        GLabel_zmena_obj_sif_dat_hodnota.place(x=670,y=390,width=100,height=42)

        self.GLineEdit_293 = tk.Entry(root)
        self.GLineEdit_293["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.GLineEdit_293["font"] = ft
        self.GLineEdit_293["fg"] = "#333333"
        self.GLineEdit_293["justify"] = "left"
        self.GLineEdit_293["text"] = "Entry"
        self.GLineEdit_293.place(x=10, y=70, width=112, height=30)

    def time_convert(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        return "{0}:{1}:{2}".format(int(hours), int(mins), round(sec))

    def update_capture_time(self):
        start_time = time.time()
        while (self.is_capture == True):
            end_time = time.time()
            time_lapsed = end_time - start_time
            self.capture_time = self.time_convert(time_lapsed)
            self.GLabel_cas_text["text"] = self.capture_time
            time.sleep(0.5)

    def update_capture_pkt(self):
        while (self.is_capture == True):
            pkt = main.get_number_of_packets()
            self.GLabel_zachyceno_text["text"] = str(pkt)

            if int(pkt) >= self.pocet_paketu:
                self.GButton_stop_command()

    def GButton_start_command(self):
        print("Start...")
        self.pocet_paketu = int(self.GLineEdit_293.get())
        print(self.pocet_paketu)
        thread = Thread(target=main.live_capturing, args=[self.pocet_paketu])
        thread.start()
        self.is_capture = True
        threadTime = Thread(target=self.update_capture_time, args=())
        threadTime.start()
        threadPkt = Thread(target=self.update_capture_pkt, args=())
        threadPkt.start()


    def GButton_stop_command(self):
        print("Stop...")
        self.is_capture = False

    def GButton_vysledky_command(self):
        print("Vysledky...")


    def GButton_graf_protokolu_command(self):
        print("Graf protokolu...")
        main.create_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
