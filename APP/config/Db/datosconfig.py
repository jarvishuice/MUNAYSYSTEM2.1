
 
class CredentialDb():
    user=None
    db=None
    password=None
    host=None
    port=None
    def __init__(self):
        self.user='operaciones'
        self.db='munay'
        self.password='V3n3zu3l42023**'
        self.host='0.0.0.0'
        self.port='5432'
    def getDatos(self):
        conection=('dbname='+self.db+' ' +'user='+self.user+' '+'password='+self.password+' '+'host='+self.host+' '+'port='+self.port) 
        return conection
