import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from lmfit import Model
import time


def current(V_D, I_s, n):                           # define equation of current
    return I_s*(np.exp((V_D/(n*0.026))-1))


def load_data(file_root):
    wafer, mask, test, name, date, oper, row, col, analysis_wl = [], [], [], [], [], [], [], [], []

    for data in root.iter():
        if data.tag == 'OIOMeasurement':
            date.append(data.get('CreationDate'))
            oper.append(data.get('Operator'))

        elif data.tag == 'TestSiteInfo':
            test.append(data.get('TestSite'))
            wafer.append(data.get('Wafer'))
            mask.append(data.get('Maskset'))
            row.append(data.get('DieRow'))
            col.append(data.get('DieColumn'))

        elif data.tag == 'DesignParameter':
            if data.attrib.get('Name') == 'Design wavelength':
                analysis_wl.append(data.text)

        elif data.tag == 'ModulatorSite':
            name.append(data.find('Modulator').get('Name'))

    return wafer, mask, test, name, date, oper, row, col, analysis_wl


xml_file = etree.parse("sample.xml")     # load xml file
root = xml_file.getroot()           # get root(element) of file

# setting of font
font_title = {                  # font setting for title
    'family': 'monospace',     # font style
    'weight': 'bold',          # font weight
    'size': 15                 # font size
}

# ==================================================================================================================== #
plt.figure(figsize=(20, 10))
plt.suptitle('HY202103_D08_(0,2)_LION1_DCM_LMZC', fontsize=20, weight='bold')

# Voltage-Current(Raw data)
vol, cur = [], []
plt.subplot(2, 3, 4)

for i in root.iter():
    if i.tag == 'Voltage':
        vol = list(map(float, i.text.split(',')))
    elif i.tag == 'Current':
        cur = list(map(float, i.text.split(',')))

plt.plot(vol, list(map(abs, cur)), 'co', label='raw_data')

# Voltage-Current(Fitting)
# V_D <= 0.25V(threshold voltage)
p_num = 5
fit = np.polyfit(np.array(vol)[:10], np.array(list(map(abs, cur)))[:10], p_num)
fit_eq = np.poly1d(fit)
print('[Fitting about V_D <= 0.25 (IV analysis)]')
print('[Fitting equation]')
print(fit_eq)
print(f'r² = {r2_score(list(map(abs, cur))[:10], fit_eq(vol[:10]))}\n')


# V_D > 0.25V(threshold voltage)
Cmodel = Model(current)
params = Cmodel.make_params(I_s=5e-12, n=1)
result = Cmodel.fit(list(map(abs, cur))[10:], params, V_D=vol[10:])
print('[Fitting about V_D > 0.25 (IV analysis)]')
print(f'result of best values : {result.best_values}')
print(f'result of best fit : {result.best_fit}')
print(f'r² = {r2_score(list(map(abs, cur))[10:], result.best_fit)}\n')

fit_plot = []
n1, n2 = 0, 0
for v in vol:
    if v <= 0.25:
        fit_plot.append(fit_eq(vol[n1]))
        n1 += 1
    else:
        fit_plot.append(result.best_fit.tolist()[n2])
        n2 += 1

rsq_iv = r2_score(list(map(abs, cur)), fit_plot)
print('[Result of fitting (IV analysis)]')
print(f'r² = {rsq_iv}\n')
plt.plot(vol, fit_plot, '--', label='Fitting')

# Setting of graph
plt.title('IV-analysis', fontdict=font_title)
plt.xlabel('Voltage[V]', fontsize=10)
plt.ylabel('Current[A]', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.yscale('logit')
plt.minorticks_off()
plt.legend(loc='best', ncol=2, fontsize=10)
plt.grid(True, which='major', alpha=0.5)

# ==================================================================================================================== #

# Wavelength-Transmission(Raw data)
wl_list, tm_list = [], []
wl_ref, tm_ref = [], []
arr_tm = []
DC_bias = -2.0
plot_color = ['lightcoral', 'coral', 'gold', 'lightgreen', 'lightskyblue', 'plum']
color_number = 0

plt.subplot(2, 3, 1)
for i in root.iter():
    if i.tag == 'WavelengthSweep':
        if i.attrib.get('DCBias') == str(DC_bias):
            wl = list(map(float, i.find('L').text.split(',')))
            wl_list.append(wl)
            tm = list(map(float, i.find('IL').text.split(',')))
            tm_list.append(tm)
            plt.plot(wl, tm, plot_color[color_number], label=f'DCBias = {DC_bias}V')
            DC_bias += 0.5
            color_number += 1

        plt.title('Transmission spectra - as measured', fontdict=font_title)
        plt.xlabel('Wavelength[nm]', fontsize=10)
        plt.ylabel('Measured transmission[dB]', fontsize=10)
        plt.legend(loc='lower center', ncol=2, fontsize=10)

    # Reference
    elif i.tag == 'Modulator':
        if i.attrib.get('Name') == 'DCM_LMZC_ALIGN':
            wl_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
            tm_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
            plt.plot(wl_ref, tm_ref, color='#7f7f7f', linestyle=':', label='Reference')
            plt.subplot(2, 3, 2)
            plt.plot(wl_ref, tm_ref, color='#7f7f7f', linestyle=':', label='Reference')
            arr_tm = np.array(tm_ref)
            print(f'Max transmission of Ref. spec : {np.max(arr_tm)}dB at wavelength : {wl_ref[np.argmax(arr_tm)]}nm')
            print(f'Min transmission of Ref. spec : {np.min(arr_tm)}dB at wavelength : {wl_ref[np.argmin(arr_tm)]}nm\n')

# Wavelength-Transmission(Fitting)
rsq_ref = []
for p in range(2, 7):
    start_time = time.time()
    fit = np.polyfit(np.array(wl_ref), np.array(tm_ref), p)
    run_time = time.time() - start_time
    fit_eq = np.poly1d(fit)
    print(f'[Fitting equation(ref)-{p}th]')
    print(fit_eq)
    print(f'r²={r2_score(tm_ref, fit_eq(wl_list[0]))}')
    print(f'run time : {run_time}s\n')
    rsq_ref.append(r2_score(tm_ref, fit_eq(wl_list[0])))
    plt.plot(wl_ref, fit_eq(wl_ref), label=f'{p}th R² : {r2_score(tm_ref, fit_eq(wl_list[0]))}')

plt.title('Transmission spectra - as measured', fontdict=font_title)
plt.xlabel('Wavelength[nm]', fontsize=10)
plt.ylabel('Measured transmission[dB]', fontsize=10)
plt.legend(loc='lower center', fontsize=10)

DC_bias = -2.0
plt.subplot(2, 3, 3)

for j in range(6):
    plt.plot(wl_ref, tm_ref - fit_eq(wl_ref))
    plt.plot(wl_list[j], tm_list[j]-fit_eq(wl_list[j]), plot_color[j], label=f'DC_bias={DC_bias}')
    DC_bias += 0.5

plt.title('Flat Transmission spectra - as measured', fontdict=font_title)
plt.xlabel('Wavelength[nm]', fontsize=10)
plt.ylabel('Measured transmission[dB]', fontsize=10)
plt.legend(loc='lower center', ncol=2, fontsize=10)

plt.savefig('HY202103_D08_(0,2)_LION1_DCM_LMZC.png')

wafer, mask, test, name, date, oper, row, col, analysis_wl = load_data(root)

df = pd.DataFrame({'Wafer': wafer, 'Mask': mask, 'TestSite': test, 'Name': name, 'Date': date,
                   'Operator': oper, 'Row': row, 'Column': col, 'Analysis Wavelength': analysis_wl,
                   'Rsq of Ref. spectrum (Nth)': rsq_ref[2], 'Max transmission of Ref. spec. (dB)': np.max(arr_tm),
                   'Rsq of IV': rsq_iv, 'I at -1V [A]': cur[4],
                   'I at 1V [A]': abs(cur[-1])})

df.to_csv('HY202103_D08_(0,2)_LION1_DCM_LMZC.csv')
