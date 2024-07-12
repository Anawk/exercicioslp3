from aquario import calculavolume,calculapotenciatermostato,calculafiltragem

def main ():
    
    print("Olá, responda algumas perguntas!")
    com = float(input("Qual o comprimento do aquário?"))
    alt = float(input("Qual a altura do aquário?"))
    lar = float(input("Qual a largura do aquário?"))
    des = float(input("Qual a temperatura desejada?"))
    amb = float(input("Qual a temperatura ambiente?"))
    
    vol = calculavolume(com,alt,lar)
    pot = calculapotenciatermostato(vol,des,amb)
    
    filtmin, filtmax = calculafiltragem(vol)
    
    print("Esse é o volume do aquario em litros: {:.2f}L".format(vol))
    print("Essa é a potencia do termostato em watts: {:.2f}W".format(pot))
    print("Essa é a filtragem necessária: de {:.2f}L a {:.2f}L por hora ".format(filtmin,filtmax))

     
if __name__ == "__main__":
    main()