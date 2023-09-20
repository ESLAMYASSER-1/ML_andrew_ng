from pynput.keyboard import Key,Listener
import winsound

def on_press(key):
    winsound.PlaySound("click.wav",winsound.SND_ASYNC)


def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()