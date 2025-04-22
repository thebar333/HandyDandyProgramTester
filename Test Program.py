import os 
#READ ME:
# It is a good idea to install PysimpleGUI otherwise this wont work
# just go to console and typ pip install PySimpleGUI
# it should work
# BTW pass is 123
import PySimpleGUI as sg
fa = 0
c = 0
print("hi")
sg.theme('DarkAmber')
layout = [  [sg.Text('Bartek Handy-Dandy Program tester')],
         [sg.Text('Expected Value:'), sg.Input(key='-EXPV-')],
         [sg.Text('File:'), sg.Input(key='-FILE-')],   
         [sg.Button('Check file'), sg.Cancel()],
         [sg.Text('Result: '), sg.Text('', key='-OTPT-')],
         ]
window = sg.Window('Barteks Handy-Dandy Program tester', layout)
#window.read()
import subprocess
result = subprocess.run(["python", "T1.py"], capture_output=True, text=True)
lotpt = result.stdout.strip()

while True:
    event, values = window.read()
    print(f"Event: {event}, Values: {values}")
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        if event == 'Check file':
            os.system('python T1.py')
            if lotpt == '-EXPV-': 
                window['-OUTPUT-'].update(f'Pass')
            else:
                window['-OUTPUT-'].update(f'Fail')                
    except ValueError:
        print("Invalid input detected")
        window['-OUTPUT-'].update('Please enter a valid number')
window.close()






