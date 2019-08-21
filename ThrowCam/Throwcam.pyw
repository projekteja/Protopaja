# import external libraries
import vlc
import sys
import paramiko
import subprocess
import re

if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter.filedialog import askopenfilename
else:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk
import os
import pathlib
from threading import Thread, Event
import time
import platform


class ttkTimer(Thread):
    """
    Class for timing , used for VLC
    """
    def __init__(self, callback, tick):
        Thread.__init__(self)
        self.callback = callback
        self.stopFlag = Event()
        self.tick = tick
        self.iters = 0

    def run(self):
        while not self.stopFlag.wait(self.tick):
            self.iters += 1
            self.callback()

    def stop(self):
        self.stopFlag.set()

    def get(self):
        return self.iters


class Player(Tk.Frame):
    """
    Class for video players
    """
    def __init__(self, parent, nbr = 0):
        Tk.Frame.__init__(self, parent)
        self.nbr = nbr
        self.parent = parent

        #Setup video/audio player frames
        self.player = None
        self.videopanel = ttk.Frame(self.parent, width=640, height=480)

        self.canvas = Tk.Canvas(self.videopanel, width=640, height=480).pack(fill=Tk.NONE,expand=False)

        if nbr == 0 or nbr == 2:
            self.videopanel.grid(row=nbr + 1, column=1)
        elif nbr == 1:
            self.videopanel.grid(row=1, column=2)

        self.controlx = 700

        if self.nbr == 3:
            self.controly = 515 + (self.nbr * 58)
        else:
            self.controly = 515 + (self.nbr * 55)

        #Setup control buttons
        ctrlpanel = ttk.Frame(self.parent)

        pause  = ttk.Button(ctrlpanel, text="Pause", command=self.OnPause)
        play   = ttk.Button(ctrlpanel, text="Play", command=self.OnPlay)
        stop   = ttk.Button(ctrlpanel, text="Stop", command=self.OnStop)
        pause.pack(side=Tk.LEFT)
        play.pack(side=Tk.LEFT)
        stop.pack(side=Tk.LEFT)

        if self.nbr > 2:
            self.volume_var = Tk.IntVar()
            self.volslider = Tk.Scale(ctrlpanel, variable=self.volume_var, command=self.volume_sel,
                    from_=0, to=100, orient=Tk.HORIZONTAL, length=100)
            self.volslider.set(100)
            self.volslider.pack(side=Tk.LEFT)

        ctrlpanel.place(x=self.controlx, y=self.controly)

        #Setup rest of the graphics
        title = Tk.Text(self.parent, height=1, width=15, relief=Tk.FLAT, bg=self.parent.cget('bg'))
        title2 = Tk.Text(self.parent, height=1, width=8, relief=Tk.FLAT, bg=self.parent.cget('bg'))

        if 0 <= self.nbr <= 2:
            text = "Camera %d" % (self.nbr + 1)

            if self.nbr == 0:
                title2.insert(Tk.END, text)
                title2.place(x=0, y=0)
            elif self.nbr == 1:
                title2.insert(Tk.END, text)
                title2.place(x=640, y=0)
            else:
                title2.insert(Tk.END, text)
                title2.place(x=0, y=0 + 480)
        else:
            text = "Audio"

        title.insert(Tk.END, text)
        title.place(x=self.controlx, y=self.controly - 20)

        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.OnPlay()


    def OnExit(self, evt):
        #Closes the window
        self.Close()


    def OnOpen(self):
        #Actions when opening the program
        
        if self.nbr == 0:
            self.Media = self.Instance.media_new("http://192.168.4.1:8080")
        elif self.nbr == 1:
            self.Media = self.Instance.media_new("http://192.168.4.1:8081")
        elif self.nbr == 2:
            self.Media = self.Instance.media_new("http://192.168.4.1:8082")
        elif self.nbr == 3:
            self.Media = self.Instance.media_new("http://192.168.4.1:8083")

        self.player.set_media(self.Media)
        if platform.system() == 'Windows':
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle())
        self.OnPlay()


    def OnPlay(self):
        #Toggle the status to Play/Pause
        #If no file is loaded, open the dialog window

        # check if there is a file to play, otherwise open a
        # Tk.FileDialog to select a file

        if not self.player.get_media():
            self.OnOpen()
        else:
            # Try to launch the media, if this fails display an error message
            if self.player.play() == -1:
                self.errorDialog("Unable to play.")


    def GetHandle(self):
        return self.videopanel.winfo_id()


    def OnPause(self):
        #Pause the player
        self.player.pause()


    def OnStop(self):
        #Stop the player
        self.player.stop()
        self.timeslider.set(0)


    def volume_sel(self, evt):
        #For valume selecting in videoplayer
        if self.player == None:
            return
        volume = self.volume_var.get()
        if volume > 100:
            volume = 100
        if self.player.audio_set_volume(volume) == -1:
            self.errorDialog("Failed to set volume")


    def OnSetVolume(self):
        #Set the volume according to the volume sider.
        volume = self.volume_var.get()
        
        if volume > 100:
            volume = 100
        if self.player.audio_set_volume(volume) == -1:
            self.errorDialog("Failed to set volume")


    def errorDialog(self, errormessage):
        #Display a simple error dialog.
        Tk.tkMessageBox.showerror(self, 'Error', errormessage)


class LED_BUTTONS(Tk.Frame):
    """
    Setup and control LEDS
    """

    def __init__(self, parent, client, status):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.client = client
        self.status = status

        #Setup buttons 
        LED_OFF  = ttk.Button(self, text="OFF", command=self.run_ledscript_off)
        LED_ON   = ttk.Button(self, text="ON", command=self.run_ledscript_on)
        LED_1   = ttk.Button(self, text="LED 1", command=self.run_ledscript_1)
        LED_2   = ttk.Button(self, text="LED 2", command=self.run_ledscript_2)
        LED_3   = ttk.Button(self, text="LED 3", command=self.run_ledscript_3)

        LED_3.pack(side=Tk.BOTTOM)
        LED_2.pack(side=Tk.BOTTOM)
        LED_1.pack(side=Tk.BOTTOM)
        LED_ON.pack(side=Tk.BOTTOM)
        LED_OFF.pack(side=Tk.BOTTOM)

        self.place(x=952.5, y=520)

        #Setup graphics
        text = "LEDS:"
        title = Tk.Text(self.parent, height=1, width=5, relief=Tk.FLAT, bg=self.parent.cget('bg'))
        title.insert(Tk.END, text)
        title.place(x=967.5, y=495)

    def end_loops(self):
        stdin, stdout, stderr = self.client.exec_command('pkill -f led_mato.py')
        stdin, stdout, stderr = self.client.exec_command('pkill -f led_kummitus.py')
        stdin, stdout, stderr = self.client.exec_command('pkill -f led_disko.py')
        

    def run_ledscript_off(self):
        if self.status == 1:
            self.end_loops()
            #run OFF script through SSH
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/led_off.py')

    def run_ledscript_on(self):
        if self.status == 1:
            self.end_loops()
            #run ON script through SSH
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/led_on.py')

    def run_ledscript_1(self):
        if self.status == 1:
            self.end_loops()
            #run 1st script through SSH
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/led_mato.py')

    def run_ledscript_2(self):
        if self.status == 1:
            self.end_loops()
            #run 2nd script through SSH
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/led_kummitus.py')

    def run_ledscript_3(self):
        if self.status == 1:
            self.end_loops()
            #run 3rd script through SSH
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/led_disko.py')
        

class Orientation_DSP(Tk.Frame):
    """
    Setup and control Orientation Display
    """

    def __init__(self, parent, canvas, client):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas = canvas
        self.client = client

        #for side
        self.angle = 0

        #for above
        self.a_x = 0
        self.a_y = 0

        self.b_x = 0
        self.b_y = 0

        #Setup Graphics
        path= "Graphics/acc_1.png"
        path2 = "Graphics/acc_2.png"

        self.img = Image.open(path)
        self.image = ImageTk.PhotoImage(self.img)
        self.side = self.canvas.create_image(135,350, image=self.image)

        self.img2 = Image.open(path2)
        self.image2 = ImageTk.PhotoImage(self.img2)
        self.above = self.canvas.create_image(315,350, image=self.image2)

        self.above_p = self.canvas.create_oval(310, 345, 320, 355,outline= "black" ,fill="lawn green", width = 2)

        text = "ABOVE"
        title = Tk.Text(self.parent, height=1, width=5, relief=Tk.FLAT, bg=self.parent.cget('bg'))
        title.insert(Tk.END, text)
        title.place(x=935, y=925)

        text = "SIDE"
        title = Tk.Text(self.parent, height=1, width=5, relief=Tk.FLAT, bg=self.parent.cget('bg'))
        title.insert(Tk.END, text)
        title.place(x=755, y=925)

        #Setup button
        UPDATE = ttk.Button(self, text="UPDATE", command=self.update)
        UPDATE.pack(side=Tk.BOTTOM)
        self.place(x=827.5, y=917.5)


    def get_angles(self):
        #get new data for both displays
        try:
            stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/commands/MMA8452.py')
            data = stdout.readlines()
            self.a_x = float(data[0][0:4])
            self.a_y = float(data[0][4:8])
            self.angle = float(data[0][8:12])
            
        except:
            print("Failed to update")


    def update_pos_side(self):
        #update graphics for 'side' display
        self.canvas.delete(self.side)

        if self.angle == 360:
            self.angle = 0

        self.get_angles()
        self.image = ImageTk.PhotoImage(self.img.rotate(self.angle))
        self.side = self.canvas.create_image(135,350, image=self.image)


    def update_pos_above(self):
        #update graphics for 'above' display
        self.canvas.move(self.above_p,self.b_x,self.b_y)
        self.canvas.move(self.above_p,self.a_x,self.a_y)
        self.b_x = -self.a_x
        self.b_y = -self.a_y


    def update(self):
        #update both displays
        self.get_angles()
        self.update_pos_side()
        self.update_pos_above()

        
class SIGNAL_BUTTON(Tk.Frame):
    """
    Setup and control signal testing
    """

    def __init__(self, parent, canvas):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas = canvas
        self.strength = 0

        #Setup background square
        self.canvas.create_rectangle(430, 275, 605, 430,outline= "black" ,fill="black")

        #Setup bar graphics
        self.bar1 = self.canvas.create_rectangle(440, 280, 595, 305,fill="green", state='hidden')
        self.bar2 = self.canvas.create_rectangle(440, 310, 595, 335,fill="lawn green", state='hidden')
        self.bar3 = self.canvas.create_rectangle(440, 340, 595, 365,fill="yellow", state='hidden')
        self.bar4 = self.canvas.create_rectangle(440, 370, 595, 395,fill="orange", state='hidden')
        self.bar5 = self.canvas.create_rectangle(440, 400, 595, 425,fill="red2", state='hidden')

        #Setup signal button
        SIGNAL  = ttk.Button(self, text="SIGNAL", command=self.get_signal_strength)
        SIGNAL.pack(side=Tk.BOTTOM)
        self.place(x=1120, y=920)


    def get_signal_strength(self):
        #Check signal with read_data_from_cmd(), and save it to self.strenght
        data = self.read_data()
        self.strength = int (data[0][1])

        #Hide all bars
        self.canvas.itemconfigure(self.bar1, state='hidden')
        self.canvas.itemconfigure(self.bar2, state='hidden')
        self.canvas.itemconfigure(self.bar3, state='hidden')
        self.canvas.itemconfigure(self.bar4, state='hidden')
        self.canvas.itemconfigure(self.bar5, state='hidden')

        #Set corresponding amount of bars visible
        if 0 <= self.strength < 20:
            self.canvas.itemconfigure(self.bar5, state='normal')
        elif 20 <= self.strength < 40:
            self.canvas.itemconfigure(self.bar5, state='normal')
            self.canvas.itemconfigure(self.bar4, state='normal')
        elif 40 <= self.strength < 60 :
            self.canvas.itemconfigure(self.bar5, state='normal')
            self.canvas.itemconfigure(self.bar4, state='normal')
            self.canvas.itemconfigure(self.bar3, state='normal')
        elif 60 <= self.strength < 80:
            self.canvas.itemconfigure(self.bar5, state='normal')
            self.canvas.itemconfigure(self.bar4, state='normal')
            self.canvas.itemconfigure(self.bar3, state='normal')
            self.canvas.itemconfigure(self.bar2, state='normal')
        elif 80 <= self.strength <= 100:
            self.canvas.itemconfigure(self.bar5, state='normal')
            self.canvas.itemconfigure(self.bar4, state='normal')
            self.canvas.itemconfigure(self.bar3, state='normal')
            self.canvas.itemconfigure(self.bar2, state='normal')
            self.canvas.itemconfigure(self.bar1, state='normal')


    def read_data(self):
        #Open cmd and read signal strenght, save it and close cmd
        p = subprocess.Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode()
        m = re.findall('Name.*?:.*?([A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
        p.communicate()

        return m


class SSH_BUTTON(ttk.Frame):
    """
    Setup and control SSH
    """

    def __init__(self, parent, canvas):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas = canvas
        self.state = 0 #set 0 when no SSH and 1 when connected

        #Sets the needed parametres:
        #server = server IP
        #username = username in server
        #password = usernames password (needs tp be hashed in the future)

        self.server = "192.168.4.1"
        self.username = "pi"
        self.password = "SavoxProto2019"
        self.client = paramiko.SSHClient()

        #Creates button for SSH
        SSH_BUTTON  = ttk.Button(self, text="CONNECT SSH", command=self.get_ssh_connection)
        SSH_BUTTON.pack(side=Tk.BOTTOM)
        self.status_color = "red2"
        self.status = self.canvas.create_rectangle(460, 197, 470, 207,outline= "black" ,fill=self.status_color, width = 1)
        self.place(x=1115, y=670)


    def get_ssh_connection(self):
        #Try to connect to SSH client
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.server, username=self.username, password=self.password)

        #Changes the color of the button if connection is there.
        if self.client.get_transport() is not None:
            if self.client.get_transport().is_active():
                self.status_color = "green"
                self.state = 1
        
        #Set button color
        self.canvas.itemconfig(self.status, fill = self.status_color)


class AUDIO_UPSTREAM_BUTTON(ttk.Frame):
    """
    Setup audio upstream
    """

    def __init__(self, parent, canvas, client, state):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas = canvas
        self.client = client
        self.state = state

        self.stream = 0
        
        #Creates button for Audio upstreaming
        AU_BUTTON  = ttk.Button(self, text="CONNECT AUS", command=self.set_upstream)
        AU_BUTTON.pack(side=Tk.BOTTOM)
        self.status_color = "red2"
        self.status = self.canvas.create_rectangle(460, 227, 470, 237,outline= "black" ,fill=self.status_color, width = 1)
        self.place(x=1115, y=700)


    def check_state(self):
        if self.state == 1:
            return True
        else:
            return False
        

    def disconnect_rasp(self):
        stdin, stdout, stderr = self.client.exec_command('pkill -f audiostream.sh')
        
        
    def connect_rasp(self):
        stdin, stdout, stderr = self.client.exec_command('python3 /home/pi/audiostream.py')


    def set_upstream(self):
        self.disconnect_rasp()
        if self.check_state and self.stream == 0:
            self.status_color = "green"

            subprocess.Popen('cvlc dshow://  --sout "#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}"', shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            time.sleep(5)
            self.connect_rasp()
            #Set button color
            self.canvas.itemconfig(self.status, fill = self.status_color)

            self.stream = 1


class UI_INIT():
    """
    Class that inits most of UI elements
    """

    def __init__(self, root):
        #Setup background canvas
        self.canvas = Tk.Canvas(root, width=640, height=480)
        self.canvas.place(x=640,y=480)

        #Setup background graphics
        self.canvas.create_rectangle(45, 5, 635, 475,outline= "black" ,fill="white")
        self.canvas.create_rectangle(50, 10, 295, 175,outline= "black" ,fill=root.cget('bg'))
        self.canvas.create_rectangle(50, 180, 400, 255,outline= "black" ,fill=root.cget('bg'))
        self.canvas.create_rectangle(300, 10, 400, 175,outline= "black" ,fill=root.cget('bg'))
        self.canvas.create_rectangle(50, 260, 400, 470,outline= "black" ,fill=root.cget('bg'))
        self.canvas.create_rectangle(405, 180, 630, 255,outline= "black" ,fill=root.cget('bg'))
        self.canvas.create_rectangle(405, 260, 630, 470,outline= "black" ,fill=root.cget('bg'))

        #Setup Image
        path = "Graphics/savox-logo.png"
        self.img = Image.open(path)
        self.image = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(520,95, image=self.image)

        #Setup video and audio players
        self.vplayer1 = Player(root, nbr = 0)
        self.vplayer2 = Player(root, nbr = 1)
        self.vplayer3 = Player(root, nbr = 2)
        self.aplayer1 = Player(root, nbr = 3)

        #Setup buttons
        self.SSH = SSH_BUTTON(root, self.canvas)
        self.AU = AUDIO_UPSTREAM_BUTTON(root, self.canvas,self.SSH.client, self.SSH.state)
        self.LED = LED_BUTTONS(root, self.SSH.client, self.SSH.state)
        self.ACCELEROMETER = Orientation_DSP(root, self.canvas, self.SSH.client)
        self.WIFI_SIGNAL = SIGNAL_BUTTON(root, self.canvas)


def Tk_get_root():
    """
    Setup window
    """
    if not hasattr(Tk_get_root, "root"):
        Tk_get_root.root= Tk.Tk()  #initialization call is inside the function
        Tk_get_root.root.geometry("1280x960+5+5") #Setup window size
        Tk_get_root.root.resizable(False, False) #Disable resizing
        Tk_get_root.root.attributes("-topmost", True) #Force window on top

    return Tk_get_root.root


def _quit():
    """
    Quit window
    """
    root = Tk_get_root()
    root.quit()
    root.destroy()
    os.system("TASKKILL /F /IM vlc.exe")
    os._exit(1)

    
if __name__ == "__main__":
    #Init root (main window) and set icon and title
    root = Tk_get_root()
    root.protocol("WM_DELETE_WINDOW", _quit)

    root.iconbitmap(r'Graphics/savoxl.ico')

    title = "SavoX ThrowCam - Camera panel"
    root.title(title)

    #Init UI
    UI = UI_INIT(root)

    # show the player window centred and run the application
    root.mainloop()
