import xml.etree.ElementTree as etree

xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()       # get root(element) of file

# Voltage-Current
vol, cur = [], []
print('<IV-analysis>')
for i in root.iter():           # return iterator for the root element
    if i.tag == 'Voltage':
        vol = list(map(float, i.text.split(',')))       # if tag name is 'Voltage', save voltage value as list form
        print(f'Voltage = {vol}')                       # print voltage value
    elif i.tag == 'Current':
        cur = list(map(float, i.text.split(',')))       # else if tag name is 'Current', save current value as list form
        print(f'Current = {cur}')                       # print current value

# Wavelength-Transmission
wl, tm = [], []
DC_bias = -2.0      # initial DC bias Value

print('\n<Transmission spectra - as measured>')
for i in root.iter():           # return iterator for the root element
    if i.tag == 'WavelengthSweep':          # if tag name is 'WavelengthSweep'
        if i.attrib.get('DCBias') == str(DC_bias):      # and if DC bias is 'DC_bias'
            wl = list(map(float, i.find('L').text.split(',')))      # save wavelength value as list form
            tm = list(map(float, i.find('IL').text.split(',')))     # save transmission value as list form
            print(f'Wavelength = {wl}')                             # print wavelength value
            print(f'Measured transmission = {tm}')                  # print transmission value
            DC_bias += 0.5                  # add 0.5 to DC bias value

    # Grating coupler spectrum
    elif i.tag == 'Modulator':              # else if tag name is 'Modulator'
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':        # and if attribution name is 'DCM_LMZC_ALIGN'
            wl = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            # save wavelength value as list form
            tm = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            # save transmission value as list form
            print('\n<Grating coupler spectrum>')
            print(f'Wavelength = {wl}')                 # print wavelength value
            print(f'Measured transmission = {tm}')      # print transmission value