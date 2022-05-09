import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from lmfit import Model


def current(V_D, I_s, n):                           # define equation of current
    return I_s*(np.exp((V_D/(n*0.026))-1))


xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()           # get root(element) of file

# setting of font
font_axis = {                  # font setting for axis label
    'family': 'monospace',     # font style
    'weight': 'bold',          # font weight
    'size': 18                 # font size
}

font_title = {                 # font setting for title
    'family': 'monospace',     # font style
    'weight': 'bold',          # font weight
    'size': 25                 # font size
}

# ==================================================================================================================== #

# Voltage-Current(Raw data)
plt.figure(figsize=(20,10))
vol, cur = [], []               # reset the value of Voltage and Current
plt.subplot(1, 2, 1)            # Make a space for graphing in the first row and column  of dimension of (1, 2)

for i in root.iter():           # Return iterator for the root element
    if i.tag == 'Voltage':
        vol = list(map(float, i.text.split(',')))       # if tag name is 'Voltage', save voltage value as list form
    elif i.tag == 'Current':
        cur = list(map(float, i.text.split(',')))       # else if tag name is 'Current', save current value as list form

plt.plot(vol, list(map(abs, cur)), 'co', label='raw_data')
# Draw the graph vol-cur with color cyan, and circular marks

# Voltage-Current(Fitting)
# V_D <= 0.25V(threshold voltage)
p_num = 5     # polynomial number
fit = np.polyfit(np.array(vol)[:10], np.array(list(map(abs, cur)))[:10], p_num)
# fit the current to the voltage and get coefficients
fit_eq = np.poly1d(fit)         # make fitting equation by coefficients
print(f'Fitting equation : {fit_eq}')
print(f'r2 = {r2_score(list(map(abs, cur))[:10], fit_eq(vol[:10]))}\n')         # print R square
# plt.plot(vol[:10], fit_eq(vol[:10]), '--', label='poly_fit')                  # draw the fitting graph

# V_D > 0.25V(threshold voltage)
Cmodel = Model(current)             # define fitting model
params = Cmodel.make_params(I_s=5e-12, n=1)         # set initial parameters
result = Cmodel.fit(list(map(abs, cur))[10:], params, V_D=vol[10:])             # fit the current to the voltage
print(f'result of best values : {result.best_values}')          # get parameters of best fitting
print(f'result of best fit : {result.best_fit}')                # get current data after fitting
print(f'r2 = {r2_score(list(map(abs, cur))[10:], result.best_fit)}\n')          # print R square
# plt.plot(vol[10:], result.best_fit, '--', label='exp_fit')                    # draw the fitting graph

fit_plot = []
n1, n2 = 0, 0
for v in vol:
    if v <= 0.25:
        fit_plot.append(fit_eq(vol[n1]))
        n1 += 1
    else:
        fit_plot.append(result.best_fit.tolist()[n2])
        n2 += 1

print(f'r2 = {r2_score(list(map(abs, cur)), fit_plot)}\n')
plt.plot(vol, fit_plot, '--', label='Fitting')

# Setting of graph

plt.title('IV-analysis', fontdict=font_title)       # Write a label with a setting of font_title
plt.xlabel('Voltage[V]', labelpad=10, fontdict=font_axis)   # Write a label with a setting of axis and a margin of 15pt
plt.ylabel('Current[A]', labelpad=10, fontdict=font_axis)   # Write a label with a setting of axis and a margin of 15pt
plt.xticks(fontsize=14)         # Set the font size of axis value
plt.yticks(fontsize=14)         # Set the font size of axis value
plt.yscale('logit')       # Set the y-axis scale to log type
plt.minorticks_off()
plt.legend(loc='best', ncol=2, fontsize=13)
plt.grid(True, which='major', alpha=0.5)

# ==================================================================================================================== #

# Wavelength-Transmission(Raw data)
wl_list, tm_list = [], []         # reset the value of wavelength and transmission
wl_ref, tm_ref = [], []
DC_bias = -2.0          # initial value of DC bias

plt.subplot(1, 2, 2)    # make a space for graphing in the first row and second column of dimension of (1, 2)

for i in root.iter():           # Return iterator for the root element
    if i.tag == 'WavelengthSweep':          # if tag name is 'WavelengthSweep'
        if i.attrib.get('DCBias') == str(DC_bias):      # and if value of attribution 'DC bias' is DC_bias
            wl = list(map(float, i.find('L').text.split(',')))      # save wavelength value as list form
            wl_list.append(wl)
            tm = list(map(float, i.find('IL').text.split(',')))     # save transmission value as list form
            tm_list.append(tm)
            DC_bias += 0.5      # add 0.5 to DC bias value

    # Reference
    elif i.tag == 'Modulator':          # else if tag name is 'Modulator'
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':        # and if attribution name is 'DCM_LMZC_ALIGN'
            wl_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            # find the value of wavelength and save the value as list form
            tm_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            # find the value of transmission and save the value as list form

# Wavelength-Transmission(Fitting)
p_num = 4     # polynomial number
fit = np.polyfit(np.array(wl_ref), np.array(tm_ref), p_num)
fit_eq = np.poly1d(fit)
print(f'Reference fitting equation : {fit_eq}')
print(f'r2={r2_score(tm_ref, fit_eq(wl_list[0]))}')

DC_bias = -2.0          # reset the value of DC_bias
plot_color = ['lightcoral', 'coral', 'gold', 'lightgreen', 'lightskyblue', 'plum']      # Make a color list for graph

for j in range(6):
    plt.plot(wl_list[j], tm_list[j]-fit_eq(wl_list[j]), plot_color[j], label=f'DC_bias={DC_bias}')
    DC_bias += 0.5

plt.title('Transmission spectra - as measured', fontdict=font_title)    # Write a label with a setting of font_title
plt.xlabel('Wavelength[nm]', labelpad=10, fontdict=font_axis)       # Write a label with a setting of axis
plt.ylabel('Measured transmission[dB]', labelpad=10, fontdict=font_axis)    # Write a label with a setting of axis
plt.xticks(fontsize=14)     # Set the font size of axis value
plt.yticks(fontsize=14)     # Set the font size of axis value
plt.legend(loc='lower center', ncol=2, fontsize=13)
# Make a legend with location of lower center, 2 column, and font size of 13pt

#plt.show()

plt.savefig('Fitting.png', facecolor='#eeeeee', bbox_inches='tight', pad_inches=0.5)