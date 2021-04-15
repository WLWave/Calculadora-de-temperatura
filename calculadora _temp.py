print('Bem-vindo ao conversor de temperatura. \n')
print('Para utiliza-lo é simples, escolha a opção das opções \nabaixo referente ao valor que será inserido e \ndigite o valor para conversão.\n')
print('1 - Kelvin \n2 - Celsius \n3 - Fahrenheit \n')

Kelv = float
Cels = float
Fahr = float
temp = int
num = int


valor = float(input('Qual é o valor para converter?\n'))

FahrL = valor - 273.15

CelsK = valor - 273.15
FahrK = FahrL * 1.8 + 32
FahrC = valor * 1.8 + 32
KelvC = valor + 273.15
CelsF = valor - 32 * 0.55
KelvF = valor - 32 * 0.55 + 273.15

temp = int(input('De qual unidade você quer converter?'))

if temp == 1:

    print('Os valores convertidos de', valor,'Kelvins são: \n')
    print(CelsK,'Celsius\n',FahrK,'Fahrenheit')


elif temp == 2:

    print('Os valores convertidos de', valor,'Celsius são: \n')
    print(FahrC,'Fahrenheits\n',KelvC,'Kelvins')

elif temp == 3:

    print('Os valores convertidos de', valor,'Fahrenheits são: \n')
    print(CelsF,'Celsius\n',KelvF,'Kelvins')