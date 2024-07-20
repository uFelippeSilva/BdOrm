import psycopg2

conn = psycopg2.connect(
    dbname="atividade_db",
    user="postgres",
    password="112325",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

sql = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)"
val = ("Tarefa de BD", 3, "2024-04-21", "2024-04-22")
cur.execute(sql, val)

conn.commit()

sql = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
val = (2, 3)
cur.execute(sql, val)

conn.commit()

cur.execute("SELECT * FROM projeto ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT * FROM atividade ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()