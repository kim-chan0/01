import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt

xml_file = etree.parse("sample.xml")     # xml 파일 불러오기
root = xml_file.getroot()       # 파일의 root 얻어오기

voltage = root[6][0][0][2][1][0]
current = root[6][0][0][2][1][1]

plt.subplot(1, 2, 1)
plt.plot(list(map(float, voltage.text.split(','))), list(map(abs, map(float, current.text.split(',')))), 'ko-')

plt.title('IV-analysis')
plt.xlabel('Voltage[V]')
plt.ylabel('Current[A]')
plt.yscale('log')

wl_1 = root[6][0][0][2][2][0]
irr_1 = root[6][0][0][2][2][1]
wl_2 = root[6][0][0][2][3][0]
irr_2 = root[6][0][0][2][3][1]
wl_3 = root[6][0][0][2][4][0]
irr_3 = root[6][0][0][2][4][1]
wl_4 = root[6][0][0][2][5][0]
irr_4 = root[6][0][0][2][5][1]
wl_5 = root[6][0][0][2][6][0]
irr_5 = root[6][0][0][2][6][1]
wl_6 = root[6][0][0][2][7][0]
irr_6 = root[6][0][0][2][7][1]

wl_7 = root[6][0][1][2][1][0]
irr_7 = root[6][0][1][2][1][1]

plt.subplot(1, 2, 2)
plt.plot(list(map(float, wl_1.text.split(','))), list(map(float, irr_1.text.split(','))), label='DCBias = -2.0V')
plt.plot(list(map(float, wl_2.text.split(','))), list(map(float, irr_2.text.split(','))), label='DCBias = -1.5V')
plt.plot(list(map(float, wl_3.text.split(','))), list(map(float, irr_3.text.split(','))), label='DCBias = -1.0V')
plt.plot(list(map(float, wl_4.text.split(','))), list(map(float, irr_4.text.split(','))), label='DCBias = -0.5V')
plt.plot(list(map(float, wl_5.text.split(','))), list(map(float, irr_5.text.split(','))), label='DCBias = 0.0V')
plt.plot(list(map(float, wl_6.text.split(','))), list(map(float, irr_6.text.split(','))), label='DCBias = 0.5V')
plt.plot(list(map(float, wl_7.text.split(','))), list(map(float, irr_7.text.split(','))), 'k', label='Reference')

plt.title('Transmission spectra - as measured')
plt.xlabel('Wavelength[nm]')
plt.ylabel('Measured transmission[dB]')
plt.legend(loc='lower center', ncol=2)

plt.show()
