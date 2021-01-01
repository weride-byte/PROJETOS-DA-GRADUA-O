import PySimpleGUI as sg

#definição de tema

#definição de tema
sg.theme('Black')
#construção layout
layout = [ 
    [sg.Text("\nGRUPO:  ARLESON MENEZES, MATEUS GUILERME, WERGGRY, WERIDE MARCONDES\n ",text_color='Yellow',)],
    [sg.Text("PESO",size=(6,1)),sg.Input(key="peso",size=(5,1)),sg.Text("Ex. 88,88")],
    [sg.Text("ALTURA",size=(6,1)),sg.Input(key='altura',size=(5,1)),sg.Text("Ex. 1,78")],
    [sg.Output(key='campo',size=(80,7))],# Key usada para identificação # output mostrar resultado 
    [sg.Button('IMC',size=(7,1),button_color='Black on yellow', key ='IMC'), sg.Button('LIMPAR TELA',button_color='Black on yellow', key = ('LIMPAR TELA')),]
         ]
# atribuir o layout a uma tela

window = sg.Window("IMC BASICA",layout)
# apresentar a tela 
while True:# enquanto tudo for veraddeiro
 event, values = window.read()

# declarando as variaveis
 if event == sg.WIN_CLOSED: #validando o botão X para fechar 
     break
 if event == 'IMC': # EVENTO botão para calular IMC
    PESO = values.get('peso') # acessa o evento e retorna o valor
    ALTURA = values.get('altura') # acessa o evento e retorna o valor
    print("VOCE NÃO PREENCHEU UM DOS CAMPOS \n")

        

    
    
    

 if (PESO =='') or (ALTURA == ''):# verificando os campos se preechidos
  print("VOCE NÃO PREENCHEU UM DOS CAMPOS \n") #\n para pular uma linha    
        
       
 else:# verificando valores aceitaveis quanto o tipo de variavel str e convertendo p/ float
    PESO1 = values.get('peso')# get usandos os valores das caixas de texto
    ALTURA1 = values.get('altura')
    PESO = float(PESO1.replace(',','.'))# reaplece usado para subistituir o caractere caso o usuario se confunda 
    ALTURA = float(ALTURA1.replace(',','.'))
    PESO_EX =float()# variavel para limite peso ideal
    PESO_AUX=float()# variavel para calcular peso exedente
    PESO_AB=float()# variavel pata limite minimo ideal
    PESO_AUX1=float()#variavel para calcular peso inferior
    if (PESO == 0) or (ALTURA == 0):# verificando valores aceitaveis quanto o tipo de variavel Float
     print("0 NÃO E UM VALOR VALIDO \n")
      
            
    else:# dando continuidade ao codigo
       IMC = (PESO/(ALTURA**2)) 
       PESO_EX = (ALTURA**2)*24.9# verificando peso exedente
       PESO_AUX= PESO-PESO_EX#  
       PESO_AB= (ALTURA**2)*18.6
       PESO_AUX1=PESO-PESO_AB
            
       if (IMC <= 18.33):
         print ("ABAIXO DO PESO SEU IMC =%.2f"%IMC) # %.2f% IMC utilizadao para quebrar as casa decimais
         print("\nVOCE ESTA %.2f"%PESO_AUX1," KILOS ABAIXO DO PESO IDEAL")
       if (IMC >= 18.6) and (IMC <= 24.9):
           print("PESO NORMAL SEU IMC = %.2f"%IMC)
       if (IMC>= 25) and (IMC <= 29.9):
           print("SOBRE PESO SEU IMC = %.2f"%IMC)
           print("\nVOCE ESTA %.2f"%PESO_AUX," KILOS ACIMA DO PESO")
       if (IMC >= 30) and (IMC <= 34.9):
           print("OBESIDADE GRAU 1º SEU IMC =%.2f"%IMC)
           print("\nVOCE ESTA %.2f"%PESO_AUX,"KILOS ACIMA DO PESO")
       if (IMC >= 35) and (IMC <= 39.9):
           print("OBESIDADE GRAU 2º SEU IMC =%.2f"%IMC)
           print("\nVOCE ESTA %.2f"%PESO_AUX,"KILOS ACIMA DO PESO")
       if (IMC >= 40):
           print(" OBESIDADE GRAU 3º SEU IMC = %.2f"%IMC)
           print("\nVOCE ESTA %.2f"%PESO_AUX,"KILOS ACIMA DO PESO")
            
 if event == 'LIMPAR TELA': # EVENTO BOTÃO LIMPAR A TELA IMC
    window['peso'].update('')
    window['altura'].update('')
    window['campo'].update('')# atribuição para limpar o comando Output
   
   
    
    
    


   
    


   
    