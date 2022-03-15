from webapp.utils import Utils
class Tarefa:
    def __init__(self,id=0,descricao="",estado=0,url=""):
        self.Id=id
        self.Descricao = descricao
        self.Estado = estado
        self.Url = url
    
    def Imprimir(self):
        print(self.Id, self.Descricao,self.Estado)
    
    def Inserir(self):
        sql="INSERT INTO Tarefa (TarefaId,Descricao,Estado,Url) VALUES ({0},'{1}',{2},'{3}')"
        sql = sql.format(self.Id,self.Descricao,self.Estado, self.Url)
       
        return Utils.ExecutaComandoSQL(sql)
    
    def Update(self):
        sql="UPDATE Tarefa set Descricao='{1}',Estado={2},Url='{3}' WHERE TarefaId={0}"
        sql = sql.format(self.Id,self.Descricao,self.Estado,self.Url)
      
        return Utils.ExecutaComandoSQL(sql)
    @staticmethod
    def Delete(id):
        sql="DELETE FROM Tarefa WHERE TarefaId={0}"
        sql = sql.format(id)
      
        return Utils.ExecutaComandoSQL(sql)
        
    @staticmethod
    def GetAll():
        lst = []
        sql="SELECT * FROM Tarefa"
        
        #for id,desc,estado,url in Utils.ExecutaConsultaSQL(sql):
        for id,desc,estado,url in Utils.ExecutaConsultaMySQL(sql):
            tarefa = Tarefa(id,desc,estado,url)
            lst.append(tarefa)
        
        return lst
    
    def Get(self,id):
        
        sql="SELECT * FROM Tarefa WHERE TarefaId={0}"
        sql = sql.format(id)
        
        try:
        
            for id,desc,estado,url in Utils.ExecutaConsultaSQL(sql):
                self.Id = id
                self.Descricao= desc
                self.Estado = estado
                self.Url = url
        except:
            print("not found")
 