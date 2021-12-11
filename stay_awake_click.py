from pynput.mouse import Controller, Button
import time

'''
Keeps colab awake for a maximum time of 12 hrs
If nedded: `pip install pynput`
1. Run script in your terminal.2. Start training 
the model in colab and open a new cell. Move
the curser to that cell and click into it.
The program will click into that cell until
stoped via ctrl + C. Good luck!

Source: https://www.youtube.com/watch?v=78rSqtkw3Gk
'''


mouse = Controller()

while True:
    mouse.click(Button.left, 1)
    print('clicked')

    time.sleep(5)
