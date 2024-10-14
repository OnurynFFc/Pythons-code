from twilio.rest import Client
import subprocess

# Definir as informações da conta do Twilio
account_sid = 'AC7dec5b59ffa43110c6f146c25d477119'
auth_token =  'ca27515b493a79cc7f6b200f6f198f46'
client = Client(account_sid, auth_token)

# Definir a mensagem de ativação da live
ativar_mensagem = 'Iniciar transmissão ao vivo'

# Verificar se a mensagem recebida contém a mensagem de ativação
def verificar_mensagem(mensagem):
    return ativar_mensagem in mensagem

# Definir a função que inicia a transmissão ao vivo
def iniciar_live():
    # Substituir o comando abaixo com o comando necessário para iniciar a transmissão ao vivo na Twitch
    comando = 'comando_para_iniciar_a_transmissao_na_Twitch'
    subprocess.call(comando, shell=True)

# Definir a função que escuta as mensagens do WhatsApp
def escutar_mensagens():
    # Substituir o número abaixo com o número de telefone do seu WhatsApp
    numero_whatsapp = '+5512996345778'
    print('Escutando mensagens...')
    while True:
        mensagens = client.messages.list(to=numero_whatsapp)
        for mensagem in mensagens:
            if verificar_mensagem(mensagem.body):
                print('Iniciando transmissão ao vivo...')
                iniciar_live()
                client.messages(mensagem.sid).delete()
        time.sleep(5)

# Chamar a função que escuta as mensagens do WhatsApp
escutar_mensagens()
