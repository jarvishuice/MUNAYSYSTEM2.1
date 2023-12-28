from core.Implements.pedidos.pedidosDAO import PedidosDAO
from core.Entities.pedidos.pedidosEntity import PedidosEntity
from core.Interface.pedidos.Ipedidos import IPedidos
from core.config.ResponseInternal import ResponseInternal
from config.Logs.LogsActivity import Logs
from config.helpers.override import override
class PedidosEspaciosDAO(PedidosDAO,IPedidos):
   
    def __init__(self):
        super().__init__()
    
    
    @override
    def crearPedido(self, pedido: PedidosEntity) -> PedidosEntity:
        """
        Creates a new  main the  order in the database.

        Args:
            pedido (PedidosEntity): An instance of the PedidosEntity class representing the order to be created.

        Returns:
            PedidosEntity: The created order.

        Raises:
            INTEGRIDAD_ERROR: If there is an integrity error in the database.
            INTERFACE_ERROR: If there is an interface error.
            DATABASE_ERROR: If there is a database error.
        """
        try:
            conexion = self.connect()
            validacionTotal = self.validacion.validarTotal(pedido.total)
            validacionCantidad = self.validacion.validarCantidad(pedido.cantidad)
            if conexion['status'] == True:
                if validacionCantidad == True and validacionTotal == True:
                    with self.conn.cursor() as cur:
                        cur.execute(f"""insert into pedidos_espacios(idorden,idproducto,cantidad,total)
                                        values('{pedido.idOrden}','{pedido.idProducto}','{pedido.cantidad}','{pedido.total}')
                                    """)
                        self.conn.commit()
                    return ResponseInternal.responseInternal(True, f"Pedido creado de manera exitosa :[{pedido}]", pedido)
                else:
                    return ResponseInternal.responseInternal(False, "Esta insertando un cantida o total erronesa valiede sus datos por pavor ", None)
            else:
                return ResponseInternal.responseInternal(False, "ERROR DE CONEXION A LA BASE DE DATOS...", None)
        except self.INTEGRIDAD_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False, f"error de bido a que ya existe un pedido con eses datos  {pedido} ", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally:
            self.disconnect()
    @override
    def regVariosPedido(self, pedidos: list[PedidosEntity], sede: str):
        """
        Registers multiple orders in the database.

        Args:
            pedidos (list[PedidosEntity]): A list of PedidosEntity instances representing the orders to be registered.
            sede (str): The location of the orders.

        Returns:
            dict: A response indicating the success or failure of the operation.

        Raises:
            INTEGRIDAD_ERROR: If there is an integrity error in the database.
            INTERFACE_ERROR: If there is an interface error.
            DATABASE_ERROR: If there is a database error.
        """
        try:
            validation = self.validacion.validarListPedidos(pedidos)
            response = []
            if validation == True:
                for i in pedidos:
                    creacion = self.crearPedido(i)
                    if creacion['status'] == False:
                        return ResponseInternal.responseInternal(False, creacion['mesagge'], None)
                    else:
                        response.append(i)
                        continue
                return ResponseInternal.responseInternal(True, "pedidos registrado con exito ", response)
            else:
                return ResponseInternal.responseInternal(False, f"{self.NOTE} ERROR en la validacion de los datos de los pedidos ", None)
        finally:
            Logs.WirterTask("finalizada el registro de multiples pedidos ")