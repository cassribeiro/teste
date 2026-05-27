dados=[]
while len(dados)<5:
    cidade=input("Digite uma cidade:").upper()
    if cidade in dados:
        print("Cidade repetida!")
    else:
        dados.append(cidade)

arquivo=open("cidade.txt","w", encoding="utf-8")
for cidade in dados:
    arquivo.write(f"{cidade}\n")

arquivo.close()