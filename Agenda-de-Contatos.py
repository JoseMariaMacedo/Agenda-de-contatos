def exibir_menu():
    '''Exibe o menu de opções do sistema'''
    print('Agenda de Contatos')
    print('|==|' * 4)
    print('\n(1) Criar novo contato')
    print('\n(2) Listar todos os contatos')
    print('\n(3) Buscar contato')
    
    
def cadastrar_contato(nome, telefone, email, arquivo_agenda):
    """
        Recebe dados para cadastrar um novo contato.
        nome: string contendo o nome do contato.
        telefone: strng contendo o telefone do contato.
        email: string contendo o e-mail do contato.
        arquivo_agenda: string contendo o caminho do arquivo da agenda.
    """
    

    agenda = open(arquivo_agenda, 'a')
    agenda.write(f'{nome},{telefone},{email}\r')
    agenda.close()


def listar_contatos(arquivo_agenda):
    ''' Lista nome, telefone e e-mail do contato na agenda definida no caminho arquivo_agenda '''
    # Abrir a agenda para leitura:
    agenda = open(arquivo_agenda, 'r')
    # Lê todo conteúdo do arquivo:
    contatos = agenda.read() # Contato é uma string contendo todos os dados da agenda
    # Cria uma lista onde cada elemento da lista é uma das linhas da agenda
    contatos = contatos.splitlines(True) # Contatos é uma lista onde cada elemento é um dos contatos.
    agenda.close()

    # Percorrer a lista de contatos
    print(f"{'Contato':<25}\t{'Telefone':>20}\t{'E-mail':>30} ")
    for contato in contatos:
        # Queremos imprimir nome, telefone, e e-mail com alguma formatação
        # Para isso, vamos quebrar a linha que contém esses dados, usando a vírgula como separador
        # Isto transformará o contato em uma lista contendo 3 elementos: nome, telefone, e-mail.
        contato = contato.split(',') # Neste momento contato é uma lista contendo 3 elementos -> nome, telefone, e-mail.
        #Contato é igual à contato[0] indice zero, contato[1] é o telefone , contato[2] é o email.
        nome = contato[0]
        telefone = contato[1]
        email = contato[2]
        print(f"{nome:<25}\t{telefone:>20}\t{email:>30}") # Para centralizar à esquerda "<" à direita ">" e centro "^" | \t serve para tabular 
            

def buscar_contato(busca, arquivo_agenda):
    ''' Busca em uma agenda denifida por arquivo_agenda, todos os contatos da string busca. '''
    agenda = open(arquivo_agenda, 'r')
    contatos = agenda.read()
    contatos = contatos.splitlines()
    agenda.close()
    resultados = 0
    for contato in contatos:
        contato = contato.split(',')
        nome, telefone, email = contato[0], contato[1], contato[2]
        if busca in nome or busca in telefone or busca in email:
            print(f"{nome:<25}\t{telefone:>20}\t{email:>30}")
            resultados += 1
    print(f"\n{resultados} resultado(s) encontrado(s).")


arquivo_agenda = input("Informe o arquivo de agenda: ")
while True:
    exibir_menu()
    print('|=|' * 9)
    opcao = int(input("\nSelecione a opção desejada(digite 9 oara sair): "))
    print('|=|' * 9)
    if opcao == 1:
        print("Cadastro de novo contato.")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        cadastrar_contato(nome, telefone, email, arquivo_agenda)
        print(f"\nContato {nome} cadastrado com sucesso.")
        print('|=|' * 9)
    elif opcao == 2:
        print("Listar todos os contatos.")
        listar_contatos(arquivo_agenda)
        print('|=|' * 9)
    elif opcao == 3:
        print("Buscar contato.")
        busca = input("Informe o nome do contato: ")
        buscar_contato(busca, arquivo_agenda)
        print('|=|' * 9)
    elif opcao == 9:
        break
    else:
        print("Opçao inválida.")
 
