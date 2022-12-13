import PySimpleGUI as sg

## Loading popup test. 
## May implement later.
images = [
    sg.EMOJI_BASE64_HAPPY_STARE,
    sg.EMOJI_BASE64_PONDER,
    sg.EMOJI_BASE64_THINK,
    sg.EMOJI_BASE64_READING,
    sg.EMOJI_BASE64_HAPPY_IDEA,
    sg.EMOJI_BASE64_HAPPY_JOY,
    sg.EMOJI_BASE64_HAPPY_LAUGH,
    sg.EMOJI_BASE64_CLAP
    
]

layout = [[
    sg.Image(
        data=sg.EMOJI_BASE64_DREAMING,
        key='-EMOJI_GUY-'
    ),
    sg.Text(
        'Loading...',
        font='Segoe 32 bold'
    )
]]

window = sg.Window('Window',layout)

count = 0

while True: # Event Loop
    event, values = window.read(timeout=500)
    #print(count)
    if event != sg.WIN_CLOSED:
        window['-EMOJI_GUY-'].update(data=images[count])

        if count == 7:
            count =0
        else:
            count +=1

    if event == sg.WIN_CLOSED:
        break

window.close()