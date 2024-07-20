from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('postgresql://postgres:112325@localhost/atividade_db')

metadata = MetaData()
metadata.reflect(bind=engine)

tabela_projeto = Table('projeto', metadata, autoload_with=engine)
tabela_atividade = Table('atividade', metadata, autoload_with=engine)

stmt1 = tabela_atividade.insert().values(descricao='ORM - BD', projeto=3, data_inicio='2024-04-22', data_fim='2024-04-23')

stmt2 = tabela_projeto.update().\
            where(tabela_projeto.c.codigo == 1).\
            values(responsavel=3)

with engine.connect() as connection:
    result = connection.execute(stmt1)

    result = connection.execute(stmt2)

    result = connection.execute(tabela_projeto.select())
    for row in result:
        print(row)

    result = connection.execute(tabela_atividade.select())
    for row in result:
        print(row)