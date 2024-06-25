def recomendar_plano(consumo_medio):
    print("Olá seja bem-vindo(a) a nossa empresa de Telecomunicações.")
    print("Vamos recomendar um plano para você com base em seu consumo de internet.")
    consumo_medio = float(input("Insira o seu consumo médio mensal de dados (GB): "))
    print("Recomendamos o :")

    if (consumo_medio > 0 and consumo_medio <= 10):
        print("Plano Essencial Fibra - 50 Mbps")
    
    elif (consumo_medio > 10 and consumo_medio <= 20):
        print("Plano Prata Fibra - 100 Mbps")
    
    elif (consumo_medio > 20):
        print("Plano Premium Fibra - 300 Mbps")
    
    else:
        print("Valor inserido é inválido. Por gentileza, digite novamente!")
        return recomendar_plano(consumo_medio)
    
def main():
    consumo_medio = 0
    recomendar_plano(consumo_medio)

main()



        