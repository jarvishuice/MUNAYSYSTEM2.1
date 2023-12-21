

class ValidacionWalletData():
    def __init__(self) -> None:
        pass
    def validarMonto(self,monto):
        if monto > 0:
            return monto * -1
        else:
            return monto
