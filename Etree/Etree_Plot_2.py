import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt

xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()           # get root(element) of file

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
vol, cur = [], []               # reset the value of Voltage and Current
plt.subplot(1, 2, 1)            # Make a space for graphing in the first row and column  of dimension of (1, 2)

for i in root.iter():           # Return iterator for the root element
    if i.tag == 'Voltage':
        vol = list(map(float, i.text.split(',')))       # if tag name is 'Voltage', save voltage value as list form
    elif i.tag == 'Current':
        cur = list(map(float, i.text.split(',')))       # else if tag name is 'Current', save current value as list form

plt.plot(vol, list(map(abs, cur)), 'co-')   # Draw the graph vol-cur with color cyan, dotted lines, and circular marks

# Setting of graph
plt.title('IV-analysis', fontdict=font_title)       # Write a label with a setting of font_title
plt.xlabel('Voltage[V]', labelpad=15, fontdict=font_axis)   # Write a label with a setting of axis and a margin of 15pt
plt.ylabel('Current[A]', labelpad=15, fontdict=font_axis)   # Write a label with a setting of axis and a margin of 15pt
plt.yscale('log')       # Set the y-axis scale to log type
plt.xticks(fontsize=12)         # Set the font size of axis value
plt.yticks(fontsize=12)         # Set the font size of axis value


# Wavelength-Transmission
wl, tm = [], []         # reset the value of wavelength and transmission
DC_bias = -2.0          # initial value of DC bias

plt.subplot(1, 2, 2)    # make a space for graphing in the first row and second column of dimension of (1, 2)

plot_color = ['lightcoral', 'coral', 'gold', 'lightgreen', 'lightskyblue', 'plum']      # Make a color list for graph
color_number = 0    # the initial order of color list

for i in root.iter():           # Return iterator for the root element
    if i.tag == 'WavelengthSweep':          # if tag name is 'WavelengthSweep'
        if i.attrib.get('DCBias') == str(DC_bias):      # and if value of attribution 'DC bias' is DC_bias
            wl = list(map(float, i.find('L').text.split(',')))      # save wavelength value as list form
            tm = list(map(float, i.find('IL').text.split(',')))     # save transmission value as list form
            plt.plot(wl, tm, plot_color[color_number], label=f'DCBias = {DC_bias}V')
            # Draw the graph of wl-tm with color of color list, label of DC bias
            DC_bias += 0.5      # add 0.5 to DC bias value
            color_number += 1       # add 1 to color number

    # Reference
    elif i.tag == 'Modulator':          # else if tag name is 'Modulator'
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':        # and if attribution name is 'DCM_LMZC_ALIGN'
            wl = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            # find the value of wavelength and save the value as list form
            tm = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            # find the value of transmission and save the value as list form
            plt.plot(wl, tm, color='#7f7f7f', linestyle=':', label='Reference')
            # Draw the graph of reference with color of color list, label of DC bias

plt.title('Transmission spectra - as measured', fontdict=font_title)    # Write a label with a setting of font_title
plt.xlabel('Wavelength[nm]', labelpad=15, fontdict=font_axis)       # Write a label with a setting of axis
plt.ylabel('Measured transmission[dB]', labelpad=15, fontdict=font_axis)    # Write a label with a setting of axis
plt.xticks(fontsize=12)     # Set the font size of axis value
plt.yticks(fontsize=12)     # Set the font size of axis value
plt.legend(loc='lower center', ncol=2, fontsize=13)
# Make a legend with location of lower center, 2 column, and font size of 13pt

plt.show()