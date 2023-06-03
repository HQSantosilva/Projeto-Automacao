import pyodbc

class Connection:
  def __init__(self, server, database, username, password):
    self.server = server
    self.database = database
    self.username = username
    self.password = password
    self.connection = None

#O(1)
  def conectar(self):
    self.connection = pyodbc.connect(
    "DRIVER={SQL Server};"
    f"SERVER={self.server};"
    f"DATABASE={self.database};"
    f"UID={self.username};"
    f"PWD={self.password};"
    )
    
#O(1)
  def desconectar(self):
    if self.connection is not None:
      self.connection.close()
      
#O(n)
  def inserir_comando(self, titulo, comando, executaprint):
    self.conectar()
    cursor = self.connection.cursor()
    query = """INSERT INTO COMANDOS (TITULO, COMANDO, 
    EXECUTAPRINT) VALUES (?, ?, ?)"""
    values = (titulo, comando, executaprint)
    cursor.execute(query, values)
    self.connection.commit()
    cursor.close()
    self.desconectar()
    
#O(n)
  def listar_comandos(self):
    self.conectar()
    cursor = self.connection.cursor()
    query ="""SELECT * FROM COMANDOS"""
    cursor.execute(query)
    comandos = cursor.fetchall()
    cursor.close()
    self.desconectar()
    return comandos

#O(n)
  def editar_comando(self, id, titulo, comando, executaprint):
    self.conectar()
    cursor = self.connection.cursor()
    query = """UPDATE COMANDOS SET 
        TITULO = ?, 
        COMANDO = ?,
        EXECUTAPRINT = ?
        WHERE ID = ?"""
    values = (titulo, comando, executaprint, id)
    cursor.execute(query, values)
    self.connection.commit()
    cursor.close()
    self.desconectar()
    
#O(n)
  def excluir_comando(self, id):
    self.conectar()
    cursor = self.connection.cursor()
    query = """DELETE FROM COMANDOS WHERE ID = ?"""
    values = (id)
    cursor.execute(query, values)
    self.connection.commit()
    cursor.close()
    self.desconectar()
    
#O(n)
  def consultar_por_titulo(self, titulo):
    self.conectar()
    cursor = self.connection.cursor()
    query = """SELECT * FROM COMANDOS WHERE TITULO = LIKE '%?%'"""
    values = (titulo)
    cursor.execute(query, values)
    comandos = cursor.fetchall()
    cursor.close()
    self.desconectar()
    return comandos
