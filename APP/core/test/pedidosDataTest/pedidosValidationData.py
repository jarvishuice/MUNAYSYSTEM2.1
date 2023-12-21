from core.Entities.pedidos.pedidosEntity import PedidosEntity

class validationPedidosData():
    def __init__(self) -> None:
        pass
    def validarCantidad(self,cantidad):
        if cantidad > 0:
            return True
        else:
            return False
    def validarTotal(self,total):
        if total > 0:
            return True
        else:
            return False
    def validarListPedidos(self,pedidos:PedidosEntity):
    
        for i in pedidos:
            cantidad= self.validarCantidad(i.cantidad)
            total=self.validarTotal(i.total)
            if cantidad ==False and total ==False:
                return False
            else:
                continue    
        return True