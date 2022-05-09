import xml.etree.ElementTree as etree

xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()       # get root(element) of file

# Voltage-Current
voltage = root[6][0][0][2][1][0]        # voltage value indexing
current = root[6][0][0][2][1][1]        # current value indexing

print('<IV-analysis>')
print('Voltage = {}'.format(list(map(float, voltage.text.split(',')))))         # print voltage value as list form
print('Current = {}'.format(list(map(float, current.text.split(',')))))         # print current value as list form

# Wavelength-Transmission
wl_1 = root[6][0][0][2][2][0]       # wavelength value indexing(DC bias at -2V)
tm_1 = root[6][0][0][2][2][1]       # measured transmission value indexing(DC bias at -2V)
wl_2 = root[6][0][0][2][3][0]       # wavelength value indexing(DC bias at -1.5V)
tm_2 = root[6][0][0][2][3][1]       # measured transmission value indexing(DC bias at -1.5V)
wl_3 = root[6][0][0][2][4][0]       # wavelength value indexing(DC bias at -1V)
tm_3 = root[6][0][0][2][4][1]       # measured transmission value indexing(DC bias at -1V)
wl_4 = root[6][0][0][2][5][0]       # wavelength value indexing(DC bias at -0.5V)
tm_4 = root[6][0][0][2][5][1]       # measured transmission value indexing(DC bias at -0.5V)
wl_5 = root[6][0][0][2][6][0]       # wavelength value indexing(DC bias at 0V)
tm_5 = root[6][0][0][2][6][1]       # measured transmission value indexing(DC bias at 0V)
wl_6 = root[6][0][0][2][7][0]       # wavelength value indexing(DC bias at 0.5V)
tm_6 = root[6][0][0][2][7][1]       # measured transmission value indexing(DC bias at 0.5V)

wl_7 = root[6][0][1][2][1][0]       # wavelength value indexing
tm_7 = root[6][0][1][2][1][1]       # measured transmission value indexing

print('\n<Transmission spectra - as measured>')
print('Wavelength = {}'.format(list(map(float, wl_1.text.split(',')))))             # print wavelength value as list form
print('Measured transmission = {}'.format(list(map(float, tm_1.text.split(',')))))  # print transmission value as list form
print('Wavelength = {}'.format(list(map(float, wl_2.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_2.text.split(',')))))
print('Wavelength = {}'.format(list(map(float, wl_3.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_3.text.split(',')))))
print('Wavelength = {}'.format(list(map(float, wl_4.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_4.text.split(',')))))
print('Wavelength = {}'.format(list(map(float, wl_5.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_5.text.split(',')))))
print('Wavelength = {}'.format(list(map(float, wl_6.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_6.text.split(',')))))
print('Wavelength = {}'.format(list(map(float, wl_7.text.split(',')))))
print('Measured transmission = {}'.format(list(map(float, tm_7.text.split(',')))))