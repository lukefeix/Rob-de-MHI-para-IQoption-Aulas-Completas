from iqoptionapi.stable_api import IQ_Option


email = 'SEU EMAIL AQUI'
senha = 'SUA SENHA'

API = IQ_Option(email,senha)

check, reason = API.connect()

if check:
    print('Vonectado com sucesso')
else:
    if reason == '{"code":"invalid_credentials","message":"You entered the wrong credentials. Please ensure that your login/password is correct."}':
        print('Email ou senha incorreta')
    else:
        print('Houve um problema na conexão')

        print(reason)


while True:
    escolha = input('Selecione a conta em que deseja conectar: demo ou real  - ')
    if escolha == 'demo':
        conta = 'PRACTICE'
        print('Conta demo selecionada')
        break
    if escolha == 'real':
        conta = 'REAL'
        print('Conta real selecionada')
        break
    else:
        print('Escolha incorreta! Digite demo ou real')
        
API.change_balance(conta)
