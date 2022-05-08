import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt

xml_file = etree.parse("sample.xml")
root = xml_file.getroot()

# setting of font
font_axis = {                   # font setting for axis label
    'family' : 'monospace',     # font style
    'weight' : 'bold',          # font weight
    'size' : 16                 # font size
}
font_title = {                  # font setting for title
    'family' : 'monospace',     # font style
    'weight' : 'bold',          # font weight
    'size' : 25                 # font size
}

# Voltage-Current
vol, cur = [], []
plt.subplot(1, 2, 1)

for i in root.iter():
    if i.tag == 'Voltage':
        vol = list(map(float, i.text.split(',')))
    elif i.tag == 'Current':
        cur = list(map(float, i.text.split(',')))

plt.plot(vol, list(map(abs, cur)), 'co-')

# Setting of graph
plt.title('IV-analysis', fontdict=font_title)
plt.xlabel('Voltage[V]', labelpad=15, fontdict=font_axis)
plt.ylabel('Current[A]', labelpad=15, fontdict=font_axis)
plt.yscale('log')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)


# Wavelength-Transmission
wl, tm = [], []
DC_bias = -2.0

plt.subplot(1, 2, 2)

plot_color = ['lightcoral', 'coral', 'gold', 'lightgreen', 'lightskyblue', 'plum']      # Make a color list for graph
color_number = 0

for i in root.iter():
    if i.tag == 'WavelengthSweep':
        if i.attrib.get('DCBias') == str(DC_bias):
            wl = list(map(float, i.find('L').text.split(',')))
            tm = list(map(float, i.find('IL').text.split(',')))
            plt.plot(wl, tm, plot_color[color_number], label=f'DCBias = {DC_bias}V')
            DC_bias += 0.5
            color_number += 1

    # Reference
    elif i.tag == 'Modulator':
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':
            wl = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            tm = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            plt.plot(wl, tm, color='#7f7f7f', linestyle=':', label='Reference')


plt.title('Transmission spectra - as measured', fontdict=font_title)
plt.xlabel('Wavelength[nm]', labelpad=15, fontdict=font_axis)
plt.ylabel('Measured transmission[dB]', labelpad=15, fontdict=font_axis)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='lower center', ncol=2, fontsize=13)

plt.show()