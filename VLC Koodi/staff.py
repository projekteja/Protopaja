# import external libraries
import vlc
import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter.filedialog import askopenfilename
else:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename

# import standard libraries
import os
import pathlib
from threading import Thread, Event
import time
import platform


class ttkTimer(Thread):
    """a class serving same function as wxTimer... but there may be better ways to do this
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
    """The main window has to deal with events.
    """
    def __init__(self, parent, nbr = 0):
        Tk.Frame.__init__(self, parent)
        self.nbr = nbr
        self.parent = parent

        title = "SavoX ThrowCam - Camera panel"
        self.parent.title(title)
		
        

        # The second panel holds controls
        self.player = None
        self.videopanel = ttk.Frame(self.parent, width=640, height=480)
    
        self.canvas = Tk.Canvas(self.videopanel).pack(fill=Tk.NONE,expand=False)

        
   

        if nbr == 0 or nbr == 2:
            self.videopanel.grid(row=nbr + 1, column=1)
        elif nbr == 1:
            self.videopanel.grid(row=1, column=2)

        self.controlx = 395

        if self.nbr == 3:
            self.controly = 290 + (self.nbr * 55)
        else:
            self.controly = 290 + (self.nbr * 45)

        
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
            self.volslider.pack(side=Tk.LEFT)

        ctrlpanel.place(x=self.controlx, y=self.controly)
        

        title = Tk.Text(self.parent, height=1, width=15, relief=Tk.FLAT, bg=self.parent.cget('bg'))
        title2 = Tk.Text(self.parent, height=1, width=15, relief=Tk.FLAT, bg=self.parent.cget('bg'))

        if 0 <= self.nbr <= 2:
            text = "Camera %d" % (self.nbr + 1)

            if self.nbr == 0:
                title2.insert(Tk.END, text)
                title2.place(x=0, y=0)
            elif self.nbr == 1:
                title2.insert(Tk.END, text)
                title2.place(x=380, y=0)
            else:
                title2.insert(Tk.END, text)
                title2.place(x=0, y=0 + 265)
        else:
            text = "Audio"

        
        title.insert(Tk.END, text)
        title.place(x=self.controlx, y=self.controly - 20)

        # VLC player controls
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.OnPlay()
		

        # below is a test, now use the File->Open file menu
        #media = self.Instance.media_new("C:/Users/Work/Downloads/video.mp4")
        #self.player.set_media(media)
        #self.player.play() # hit the player button
        #self.player.video_set_deinterlace(str_to_bytes('yadif'))

        self.timer = ttkTimer(self.OnTimer, 1.0)
        self.timer.start()
        self.parent.update()

        #self.player.set_hwnd(self.GetHandle()) # for windows, OnOpen does does this


    def OnExit(self, evt):
        """Closes the window.
        """
        self.Close()

    def OnOpen(self):
        self.Media = self.Instance.media_new("C:/Users/ottos/Desktop/VLC Koodi/video.mp4")
        self.player.set_media(self.Media)
        if platform.system() == 'Windows':
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle()) 
        self.OnPlay()
        
        """Pop up a new dialow window to choose a file, then play the selected file.
        """
        # if a file is already running, then stop it.
#        self.OnStop()

        # Create a file dialog opened in the current home directory, where
        # you can display all kind of files, having as title "Choose a file".
#        p = pathlib.Path(os.path.expanduser("~"))
#        fullname =  askopenfilename(initialdir = p, title = "choose your file",filetypes = (("all files","*.*"),("mp4 files","*.mp4")))
#        if os.path.isfile(fullname):
#            dirname  = os.path.dirname(fullname)
#            filename = os.path.basename(fullname)
            # Creation
#            self.Media = self.Instance.media_new(str(os.path.join(dirname, filename)))
#            self.player.set_media(self.Media)
            # Report the title of the file chosen
            #title = self.player.get_title()
            #  if an error was encountred while retriving the title, then use
            #  filename
            #if title == -1:
            #    title = filename
            #self.SetTitle("%s - tkVLCplayer" % title)

            # set the window id where to render VLC's video output
 #           if platform.system() == 'Windows':
 #               self.player.set_hwnd(self.GetHandle())
 #           else:
 #               self.player.set_xwindow(self.GetHandle()) # this line messes up windows
            # FIXME: this should be made cross-platform
  #          self.OnPlay()

            # set the volume slider to the current volume
            #self.volslider.SetValue(self.player.audio_get_volume() / 2)
   #         self.volslider.set(self.player.audio_get_volume())

    def OnPlay(self):
        """Toggle the status to Play/Pause.
        If no file is loaded, open the dialog window.
        """
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

    #def OnPause(self, evt):
    def OnPause(self):
        """Pause the player.
        """
        self.player.pause()

    def OnStop(self):
        """Stop the player.
        """
        self.player.stop()
        # reset the time slider
        self.timeslider.set(0)

    def OnTimer(self):
        """Update the time slider according to the current movie time.
        """
        if self.player == None:
            return
        # since the self.player.get_length can change while playing,
        # re-set the timeslider to the correct range.
        length = self.player.get_length()
        dbl = length * 0.001
        self.timeslider.config(to=dbl)

        # update the time on the slider
        tyme = self.player.get_time()
        if tyme == -1:
            tyme = 0
        dbl = tyme * 0.001
        self.timeslider_last_val = ("%.0f" % dbl) + ".0"
        # don't want to programatically change slider while user is messing with it.
        # wait 2 seconds after user lets go of slider
        if time.time() > (self.timeslider_last_update + 2.0):
            self.timeslider.set(dbl)

    def scale_sel(self, evt):
        if self.player == None:
            return
        nval = self.scale_var.get()
        sval = str(nval)
        if self.timeslider_last_val != sval:
            # this is a hack. The timer updates the time slider.
            # This change causes this rtn (the 'slider has changed' rtn) to be invoked.
            # I can't tell the difference between when the user has manually moved the slider and when
            # the timer changed the slider. But when the user moves the slider tkinter only notifies
            # this rtn about once per second and when the slider has quit moving.
            # Also, the tkinter notification value has no fractional seconds.
            # The timer update rtn saves off the last update value (rounded to integer seconds) in timeslider_last_val
            # if the notification time (sval) is the same as the last saved time timeslider_last_val then
            # we know that this notification is due to the timer changing the slider.
            # otherwise the notification is due to the user changing the slider.
            # if the user is changing the slider then I have the timer routine wait for at least
            # 2 seconds before it starts updating the slider again (so the timer doesn't start fighting with the
            # user)
            self.timeslider_last_update = time.time()
            mval = "%.0f" % (nval * 1000)
            self.player.set_time(int(mval)) # expects milliseconds


    def volume_sel(self, evt):
        if self.player == None:
            return
        volume = self.volume_var.get()
        if volume > 100:
            volume = 100
        if self.player.audio_set_volume(volume) == -1:
            self.errorDialog("Failed to set volume")



    def OnToggleVolume(self, evt):
        """Mute/Unmute according to the audio button.
        """
        is_mute = self.player.audio_get_mute()

        self.player.audio_set_mute(not is_mute)
        # update the volume slider;
        # since vlc volume range is in [0, 200],
        # and our volume slider has range [0, 100], just divide by 2.
        self.volume_var.set(self.player.audio_get_volume())

    def OnSetVolume(self):
        """Set the volume according to the volume sider.
        """
        volume = self.volume_var.get()
        # vlc.MediaPlayer.audio_set_volume returns 0 if success, -1 otherwise
        if volume > 100:
            volume = 100
        if self.player.audio_set_volume(volume) == -1:
            self.errorDialog("Failed to set volume")

    def errorDialog(self, errormessage):
        """Display a simple error dialog.
        """
        Tk.tkMessageBox.showerror(self, 'Error', errormessage)



def Tk_get_root():
    if not hasattr(Tk_get_root, "root"): #(1)
        Tk_get_root.root= Tk.Tk()  #initialization call is inside the function
        Tk_get_root.root.geometry("765x530")
        #Tk_get_root.root.resizable(False, False)
    return Tk_get_root.root

def _quit():
    root = Tk_get_root()
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    os._exit(1)

	

if __name__ == "__main__":
    # Create a Tk.App(), which handles the windowing system event loop
    root = Tk_get_root()
    root.protocol("WM_DELETE_WINDOW", _quit)

    root.iconbitmap(r'c:/Users/ottos/Desktop/VLC Koodi/savoxl.ico')
    
    path1 = "C:/Users/ottos/Desktop/VLC Koodi/savox-logo.png"
    path2 = "C:/Users/ottos/Desktop/VLC Koodi/savox.png"
    
    c = Tk.Canvas(root, width=640, height=480)      
    c.place(x=380,y=267)
    img1 = Tk.PhotoImage(file=path1)
    img2 = Tk.PhotoImage(file=path2)
    
    c.create_rectangle(0, 0, 385, 270,outline= "black" ,fill=root.cget('bg'))
    c.create_rectangle(7, 2, 250, 145,outline= "black" ,fill=root.cget('bg'))
    c.create_rectangle(7, 165, 350, 235,outline= "black" ,fill=root.cget('bg'))

    c.create_image(315,50, image=img1)
    c.create_image(315,100, image=img2)

    vplayer1 = Player(root, nbr = 0)
    vplayer2 = Player(root, nbr = 1)
    vplayer3 = Player(root, nbr = 2)
    aplayer1 = Player(root, nbr = 3)

    
    
    
    # show the player window centred and run the application
    root.mainloop()
	
