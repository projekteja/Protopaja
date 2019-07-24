
import subprocess

def readSignalData():

    input = str(subprocess.check_output(['iwconfig', 'wlp2s0'])).split(' ')
    
    strq = [q for q in input if "Quality=" in q]
    strs = [s for s in input if "level=" in s]

    quality = strq[0].split('=')[1]
    signal = int(strs[0].split('=')[1])

    print('Signal Quality:', quality)
    print('Signal Strength:', signal, 'dbm')

readSignalData()

