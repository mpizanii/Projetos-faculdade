import mysql.connector


def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                         password='ceub123456',
                                         host='127.0.0.1')

    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists db_loja_3"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')


def create_connection():
    con = mysql.connector.connect(user='root',
                                  password='ceub123456',
                                  host='127.0.0.1',
                                  database='db_loja_3')
    print('Conexão:', con)
    return con


def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')


def create_table():
    sql = """ CREATE TABLE if not exists tb_produto(
    idt INT NOT NULL AUTO_INCREMENT,   # Cria a chava primária automatica 
    nome VARCHAR(45) NOT NULL UNIQUE,  # Valores sem repetição obrigatório
    preco DECIMAL(9,2) NOT NULL,       # NOT NULL para valor obrigatório
    dta_validade DATE NULL,            # NULL para valor opcional
    PRIMARY KEY (idt)                  # Chave primária, not null é default
    )   """
    cursor.execute(sql)

    tb2 = """CREATE TABLE if not exists tb_cliente(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL UNIQUE,
    dta_compra DATE NULL,
    valor_gasto DECIMAL (9,2) NULL,
    PRIMARY KEY (id)
    )"""
    cursor.execute(tb2)


def insert_produto():
    a_nome = input('Insert - Nome do produto: ')
    a_preco = float(input('Preço: '))
    a_data = input('Data: aaaa-mm-dd: ')
    sql = f""" insert into tb_produto (nome, preco, dta_validade)
                      values ('{a_nome}', {a_preco}, '{a_data}')  """
    cursor.execute(sql)
    conexao.commit()


def insert_cliente():
    b_nome = input('Insert - Nome do cliente: ')
    b_data = input('Data: aaaa-mm-dd: ')
    b_valor = input('Valor gasto:')
    tb_2 = f""" INSERT INTO tb_cliente (nome, dta_compra, valor_gasto)
                            VALUES ('{b_nome}', '{b_data}', '{b_valor}')"""
    cursor.execute(tb_2)
    conexao.commit()


def uptade_produto():
    lista = [1, 2, 3, 4]
    while True:
        print('[1] Para mudar o nome do produto\n'
              '[2] Para mudar o preço do produto\n'
              '[3] Para mudar a data de validade do produto\n'
              '[4] Para sair')
        try:
            escolha = int(input('Digite o valor desejado [1, 2, 3 ou 4]:'))
            if escolha not in lista:
                raise ValueError
            match escolha:
                case 1:
                    produto_id = int(
                        input('Digite o ID do produto que deseja trocar o nome:'))
                    novo_nome = input('Digite o novo nome do produto:')
                    sql = f"""UPDATE tb_produto SET nome = {
                        novo_nome} where idt = {produto_id} """
                    cursor.execute(sql)
                    conexao.commit()
                case 2:
                    produto_id = int(
                        input('Digite o ID do produto que deseja trocar o preço:'))
                    novo_preco = input('Digite o novo preço do produto:')
                    sql = f"""UPDATE tb_produto SET preco = {
                        novo_preco} where idt = {produto_id}"""
                    cursor.execute(sql)
                    conexao.commit()
                case 3:
                    produto_id = int(
                        input('Digite o ID do produto que deseja trocar a data de validade:'))
                    nova_data = input(
                        'Digite a nova data de validade do produto [aaaa-mm-dd]:')
                    sql = f"""UPDATE tb_produto SET dta_validade = {
                        nova_data} where idt = {produto_id} """
                    cursor.execute(sql)
                    conexao.commit()
                case 4:
                    break
        except ValueError:
            print('Por favor, digite uma das opções válidas!')


def update_cliente():
    lista = [1, 2, 3, 4]
    while True:
        print('[1] Para mudar o nome do cliente\n'
              '[2] Para mudar a data de compra do cliente\n'
              '[3] Para mudar o valor gasto pelo cliente\n'
              '[4] Para sair')
        try:
            escolha = int(input('Digite o valor desejado [1, 2, 3 ou 4]:'))
            if escolha not in lista:
                raise ValueError
            match escolha:
                case 1:
                    cliente_id = int(
                        input('Digite o ID do cliente que deseja trocar o nome:'))
                    novo_nome = input('Digite o novo nome do cliente:')
                    sql = f"""UPDATE tb_cliente SET nome = {
                        novo_nome} where idt = {cliente_id} """
                    cursor.execute(sql)
                    conexao.commit()
                case 2:
                    cliente_id = int(
                        input('Digite o ID do cliente que deseja trocar a data de compra dele:'))
                    nova_data = input(
                        'Digite a data de compra que o cliente realizou [aaaa-mm-dd]:')
                    sql = f"""UPDATE tb_cliente SET dta_compra = {
                        nova_data} where idt = {cliente_id}"""
                    cursor.execute(sql)
                    conexao.commit()
                case 3:
                    cliente_id = int(
                        input('Digite o ID do cliente que deseja trocar o valor gasto pelo cliente:'))
                    novo_valor = input('Digite o valor gasto pelo cliente:')
                    sql = f"""UPDATE tb_cliente SET valor_gasto = {
                        novo_valor} where idt = {cliente_id} """
                    cursor.execute(sql)
                    conexao.commit()
                case 4:
                    break
        except ValueError:
            print('Por favor, digite uma das opções válidas!')


def delete_tb_produto():
    produto_id = int(
        input('Digite o ID do produto que deseja excluir a tupla:'))
    sql = f"""DELETE FROM tb_produto WHERE idt = {produto_id}"""
    cursor.execute(sql)


def delete_tb_cliente():
    cliente_id = int(
        input('Digite o ID do cliente que deseja excluir a tupla:'))
    sql = f"""DELETE FROM tb_cliente WHERE idt = {cliente_id}"""
    cursor.execute(sql)


def select_all_produto():
    cursor.execute(f"""SELECT * FROM tb_produto;""")
    consulta = cursor.fetchall()
    for linha in consulta:
        print(linha)
    conexao.commit


def select_all_cliente():
    cursor.execute(f"""SELECT * FROM tb_cliente;""")
    consulta = cursor.fetchall()
    for linha in consulta:
        print(linha)
    conexao.commit


if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()

    while True:
        print('[1] Para inserir produto\n'
              '[2] Para inserir cliente\n'
              '[3] Para mostrar tabela produto\n'
              '[4] Para mostrar tabela cliente\n'
              '[5] Para atualizar tabela produto\n'
              '[6] Para atualizar tabela cliente\n'
              '[7] Para sair')
        try:
            escolha = int(input('Digite o comando escolhido:'))
            if escolha not in [1, 2, 3, 4, 5, 6, 7]:
                raise ValueError

            match escolha:
                case 1:
                    insert_produto()
                case 2:
                    insert_cliente()
                case 3:
                    select_all_produto()
                case 4:
                    select_all_cliente()
                case 5:
                    uptade_produto()
                case 6:
                    update_cliente()
                case 7:
                    break
        except ValueError:
            print('Por favor, digite uma das opções válidas')

    close_connection()
