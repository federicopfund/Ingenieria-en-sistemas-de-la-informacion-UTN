def Sodiaco(nombre):
    ##nombre = input("Ingrese su fecha de Nacimiento:Ejem:(25/10/1996): ")
    mes = int(nombre.split("/")[1])
    if 1<= mes <=12:
        try:
            dia = int(nombre.split("/")[0])
            
            if dia>=1 and dia<=31:
                if((mes==1) and (dia>=20)) or ((mes==2) and (dia<=18)):
                    print(("Su signo es Acuario"))
                if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):
                    print("Su signo es Piscis")
                if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)):
                    print("Su signo es Aries")
                if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=20)):
                    print("Su signo es Tauro")
                if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=20)):
                    print("Su signo es Geminis")
                if ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=22)):
                    print("Su signo es Cancer")
                if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=22)):
                    print("Su signo es Leo")
                if ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=22)):
                    print("Su signo es Virgo")
                if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)):
                    print("Su signo es Libra")
                if ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=21)):
                    print("Su signo es Escorpio")
                if ((mes==11) and (dia>=22)) or ((mes==12) and (dia<=21)):
                    print("Su signo es Sagitario")
                if ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=19)):
                    print("Su signo es Capricornio")
            else:
                print("fecha invalida vuelva a intentarlo")
        except ValueError as err:
            print("Tine que ingresar la fecha en el formato indicado:")  
    else:
        print("Numeros de Meses Incorrectos")