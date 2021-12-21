#function convert kelvin ke celsius, celsius ke kelvin
def to_celcius_kelvin(value, to):
    '''
    Mengkonversi Kelvin ke Celsius / Celsius ke Kelvin
    :param value: nilai yang ingin dikonversi | int atau float
    :param to: tujuan / hasil konversi suhu | 'celcius' atau 'kelvin' string
    
    :return: hasil konversi nilai tujuan suhu | int atau float
    '''
    # mengecek tujuan kelvin atau celcius
    if to == 'celcius':
        return value - 273.15
    
    if to == 'kelvin':
        return value + 273.15

#function convert ke fahrenheit
def to_fahrenheit(value, celsiuskelvin):
    '''
    Mengkonversi nilai celcius ke fahrenheit atau kelvin ke farenheit
    :param value: nilai yang ingin dikonversi ke fahrenheit | int atau float
    :param celsiskelvin: asal nilai temperature yang dikonversi | 'celcius' atau 'kelvin' string
    
    :return: hasil konversi nilai ke fahrenheit | int atau float
    '''

    # mengecek dari kelvin atau celcius
    if celsiuskelvin == 'kelvin':
        # menggunakan function to_celcius_kelvin()
        return (9 / 5) * (to_celcius_kelvin(value, 'celcius')) + 32
    
    if celsiuskelvin == 'celcius':
        return (9 / 5) * (value) + 32

#function convert dari fahrenheit
def from_fahrenheit(value, to):
    '''
    Mengkonversi nilai fahrenheit ke celcius atau kelvin
    :param value: nilai fahrenheit yang ingin dikovenrsi | int atau float
    :param to: tujuan konversi suhu | 'celcius' atau 'kelvin' string

    :return: hasil konversi nilai dari fahrenheit ke celcius atau kelvin | int atau float
    '''
    # mengubah nilai ke celcius dulu
    to_celsius = (5 / 9) * (value - 32)

    # mengecek tujuan kelvin atau celcius
    if to == 'celcius':
        return to_celsius
   
    if to == 'kelvin':
        return to_celsius + 273


print(f"500 Kelvin = {to_celcius_kelvin(500,'celcius')} Celsius")
print(f"300 Celsius = {to_celcius_kelvin(300,'kelvin')} Kelvin")

print(f"200 Celsius = {to_fahrenheit(200, 'celcius')} Fahrenheit")
print(f"300 Kelvin = {to_fahrenheit(300, 'kelvin')} Fahrenheit")

print(f"500 Fahrenheit = {from_fahrenheit(500, 'celcius')} Celsius")
print(f"200 Fahrenheit = {from_fahrenheit(320, 'kelvin')} Kelvin")