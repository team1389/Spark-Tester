import PySimpleGUI as sg

layout = [
    [sg.Listbox(values=['Spark 1', 'Spark 2', 'Spark 3'], size=(
        30, 6), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
    [sg.Slider(range=(-1, 1), default_value=0, size=(20, 15),
               orientation='horizontal', resolution=0.1, change_submits=True)],
    [sg.Exit()]]

window = sg.Window('Spark Tester').Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)

window.Close()


def get_all_sparks():
    # TODO:Find some way of checking network tables for the port of each spark thats initialized,
    # make list string of 'Spark + port', return it
    pass


def set_motors(percent_to_apply):
    # Send motor vals to apply to robot side through network tables
    pass
