"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

-------------------------------------

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

while True:
    cpf = (input('Digite seu CPF: ')).replace('.','').replace(' ','').replace('-','')
    cpf_9d=cpf[:9]#fatiando em 9
    try:
        primeiro_caractere=cpf[0]
        primeiro_caractere_rep=primeiro_caractere*len(cpf)
        print(cpf,primeiro_caractere_rep)
        if cpf==primeiro_caractere_rep:
            print('CPF inválido')
        else:
            if len(cpf_9d)==9:
                # i = int(range(1,10,-1))
                soma_1=0
                i_1=10
                for n_1 in cpf_9d:
                    res_1=int(n_1)*i_1
                    i_1-=1
                    soma_1+=res_1
                
                mult=soma_1*10
                primeiro_digito=mult%11
                if primeiro_digito>9:
                    primeiro_digito=0
                else:
                    primeiro_digito=primeiro_digito
                
                print(f'O primeiro digito do CPF é {primeiro_digito}') 
                    
            cpf_sd=cpf_9d+str(primeiro_digito)
            print(cpf_sd)
            soma_2=0
            i_2=11
            for n_2 in cpf_sd:
                res_2 = int(n_2)*i_2
                i_2-=1
                soma_2+= res_2

            mult_2=soma_2*10
            segundo_digito= mult_2%11

            segundo_digito=segundo_digito if segundo_digito<=9 else 0

            print(f'O segundo digito é {segundo_digito}')

            cpf_digitado = cpf
            cpf_encontrado=cpf_sd+str(segundo_digito)
            print(cpf_encontrado)

            if cpf_digitado==cpf_encontrado:
                print("CPF válido")
            else:
                print("CPF Inválido")

    except:
        print("Entrada inválida!")
        break