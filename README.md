# Usb Format

GUI Application to format USB Devices in Ubuntu


## Installation

For Python:
```bash
sudo apt-get update sudo apt-get install python3.
```

Install pip
```bash
sudo apt install python3-pip
```
Install tkinter
```bash
 sudo apt-get install python3-pil.imagetk
```

## Methodology
Methodology:

-->GUI: Python Tkinter\
-->We will be running the disk format command in the terminal from the application\
-->A command to get the list of drives attached to the sytem is run from the application\
   (refer:list_devices() in usb.py)\
-->Display the details in the drop down menu of the application
-->The application will help user choose a drive from the available list of drives
-->Details of the chosen drive are attached to a string  (refer: f() in usb.py)
-->This string is the command that will be run in the terminal
-->The command is then executed in the terminal and the Format complete alert is shown.


## Recommended

Use Conda Virtual Environment

## Contributing

Pull requests are welcome

