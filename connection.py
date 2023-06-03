import pyodbc

class Connection:
  def __init__(self, server, database, username, password):
    self.server = server
    self.database = database
    self.username = username
    self.password = password
    self.connection = None
    self.cursor = None

#O(1)
  def Conectar(self):
    self.connection = pyodbc.connect(
    "DRIVER={SQL Server};"
    f"SERVER={self.server};"
    f"DATABASE={self.database};"
    f"UID={self.username};"
    f"PWD={self.password};"
    )
    
#O(1)
  def Desconectar(self):
    if self.connection is not None:
      self.connection.close()
      self.cursor.close()
      
#O(n)
  def InserirComando(self, titulo, comando, executaprint):
    self.conectar()
    self.cursor = self.connection.cursor()
    query = """INSERT INTO COMANDOS (TITULO, COMANDO, 
    EXECUTAPRINT) VALUES (?, ?, ?)"""
    values = (titulo, comando, executaprint)
    self.cursor.execute(query, values)
    self.connection.commit()
    self.desconectar()
    
#O(n)
  def ListarComandos(self):
    self.conectar()
    self.cursor = self.connection.cursor()
    query ="""SELECT * FROM COMANDOS"""
    self.cursor.execute(query)
    comandos = self.cursor.fetchall()
    self.desconectar()
    return comandos

#O(n)
  def EditarComando(self, id, titulo, comando, executaprint):
    self.conectar()
    self.cursor = self.connection.cursor()
    query = """UPDATE COMANDOS SET 
        TITULO = ?, 
        COMANDO = ?,
        EXECUTAPRINT = ?
        WHERE ID = ?"""
    values = (titulo, comando, executaprint, id)
    self.cursor.execute(query, values)
    self.connection.commit()
    self.desconectar()
    
#O(n)
  def ExcluirComando(self, id):
    self.conectar()
    self.cursor = self.connection.cursor()
    query = """DELETE FROM COMANDOS WHERE ID = ?"""
    values = (id)
    self.cursor.execute(query, values)
    self.connection.commit()
    self.desconectar()
    
#O(n)
  def ConsultarPorTitulo(self, titulo):
    self.conectar()
    self.cursor = self.connection.cursor()
    query = """SELECT * FROM COMANDOS WHERE TITULO = LIKE '%?%'"""
    values = (titulo)
    self.cursor.execute(query, values)
    comandos = self.cursor.fetchall()
    self.desconectar()
    return comandos
#O(1)
  def LimparComandosAntigos(self):
     self.conectar()
     self.cursor = self.connection.cursor()
     query = "EXEC SP_EXCLUIRREGISTROSANTIGOS()"
     self.desconectar()
