# hmiapp/views.py

from django.shortcuts import render
from pyads import Connection
import pyads
def home(request):
    if request.method == 'POST':
        # Handle form submission
        flowrate_value = float(request.POST.get('flowrate', 0.0))

        # Connect to PLC and write the value
        with Connection('192.168.3.239.1.1', pyads.PORT_TC3PLC1) as plc:
            plc.open()
            plc.write_by_name("Ghmi_control.Line1_Flowrate1", flowrate_value)

    return render(request, 'home.html')




