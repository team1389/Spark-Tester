import PySimpleGUI as sg
from networktables import NetworkTables

# Network Tables var setup
network_table_spark_prefix = "Spark"
network_table_server = "roborio-1389-frc.local"
network_table_table_name = "Spark-Tester-Table"

table = get_network_table()
sparks = get_spark_entries(table)
spark_entry_ids = get_spark_ids(table)

layout = [
    [sg.Listbox(values=spark_entry_ids, size=(
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


def get_network_table():
    NetworkTables.initialize(server=network_table_server)
    return NetworkTables.getTable(network_table_table_name)


def get_spark_entries(table):
    return table.getEntries(network_table_spark_prefix)


def get_spark_ids(table):
    return map(lambda entry: entry.getName(), table.getEntries(network_table_spark_prefix))


def set_motors(sparks_ids, table, percent_to_apply):
    map(lambda spark_id: table.getEntry(
        spark_id).setDouble(percent_to_apply), sparks_ids)
