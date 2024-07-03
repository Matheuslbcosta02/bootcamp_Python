#instalar primeiramente o pytz \\\\\\\\\\\\ pip install pytz
#módulo datetime 
from datetime import date , datetime , time , timedelta, timezone
a = date(2024,7,3)

#data de hoje
print(date.today())

data_hora = datetime (2023,7,3,10,10,20)
print(data_hora)

#data e hora local
print(datetime.today())

#criar hora
hora = time(10,20,0)
print(hora)

#manipular objetos date,time,datetime ->>>>  timedelta

d = datetime(2023,7,19,13,45)
d = d + timedelta(weeks = 1)
print(d)



tipo_carro ="P" #M #G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
#pegar data e hora atual
data_atual = datetime.now()
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f"o carro chegou {data_atual} e ficará pronto {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f"o carro chegou {data_atual} e ficará pronto {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f"o carro chegou {data_atual} e ficará pronto {data_estimada}")

#Converter e formatar datas e horas ->>> usar métodos strftime(string format time) e strptime(string parse time)
#pegar um objeto datetime e exibir de uma certa forma

teste = datetime.now()
#formatar
print(teste.strftime("%d/%m/%y %H:%M"))

#converter string para datetime
data_string = "2023-10-20 10:20"
mascara = "%Y-%m-%d %H:%M"
teste2 = datetime.strptime(data_string, mascara)
print(teste2)
print(type(teste2))

#lidar com fusos horários ->>  pip install pytz, import pytz, depois import datetime
#BOA PRÁTICA ->>> Armazenar data e hora em UTC -> melhor para manipular
#d = datetime.now(pytz.timezone("America/Sao-Paulo"))
#pytz -> biblioteca que fornece suporte para trabalhar com fusos-horários

#Trabalhando Tz(timezone) sem bibliotecas externas:
#from datetime import datetime, timedelta, timezone
 
#criando datetime com timezone
teste3 = datetime.now(timezone(timedelta(hours=-3),"BRT"))
print(teste3)

#convertendo para outro timezone
d_utc = d.astimezone(timezone.utc)
print(d_utc)
