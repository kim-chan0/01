import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
import time

xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()           # get root(element) of file
plt.figure(figsize=(20,10))
# setting of font
font_axis = {                   # font setting for axis label
    'family': 'monospace',     # font style
    'weight': 'bold',          # font weight
    'size': 16                 # font size
}

font_title = {                  # font setting for title
    'family': 'monospace',     # font style
    'weight': 'bold',          # font weight
    'size': 25                 # font size
}

wl_R, tm_R = [], []

for i in root.iter():           # Return iterator for the root element
    if i.tag == 'Modulator':          # else if tag name is 'Modulator'
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':        # and if attribution name is 'DCM_LMZC_ALIGN'
            wl_R = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            # find the value of wavelength and save the value as list form
            tm_R = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            # find the value of transmission and save the value as list form
            plt.plot(wl_R, tm_R, color='#7f7f7f', linestyle=':', label='Reference')
            # Draw the graph of reference with color of color list, label of DC bias

start_time = time.time()

p_num = 4     # polynomial number
fit = np.polyfit(np.array(wl_R), np.array(tm_R), p_num)
fit_eq = np.poly1d(fit)
print(f'Fitting equation : {fit_eq}')
plt.plot(wl_R, fit_eq(wl_R), label='Fitting')
run_time = time.time() - start_time
print(f'run time : {run_time}')
print(f'r2={r2_score(tm_R, fit_eq(wl_R))}')

plt.title('Transmission spectra - as measured', fontdict=font_title)    # Write a label with a setting of font_title
plt.xlabel('Wavelength[nm]', labelpad=15, fontdict=font_axis)       # Write a label with a setting of axis
plt.ylabel('Measured transmission[dB]', labelpad=15, fontdict=font_axis)    # Write a label with a setting of axis
plt.xticks(fontsize=13)     # Set the font size of axis value
plt.yticks(fontsize=13)     # Set the font size of axis value
plt.legend(loc='lower center', ncol=2, fontsize=13)
# Make a legend with location of lower center, 2 column, and font size of 13pt

#plt.show()
plt.savefig('Fitting_Ref.png', facecolor='#eeeeee', bbox_inches='tight', pad_inches=0.5)