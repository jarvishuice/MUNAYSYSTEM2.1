from core.Entities.ordenes.ordenesEntity import OrdenesEntity

class validationOrdenesData():
    def __init__(self) -> None:
        pass
    def validarStatus(self,status):
        if status=='por pagar' or status == 'eliminada' or status == 'pagado':
            return True
        else:
            return False
    def validarSede(self,sede):
        if sede == 'jalisco' or sede == 'cfm' or  sede==None:
            return True
        else:
            return False
    