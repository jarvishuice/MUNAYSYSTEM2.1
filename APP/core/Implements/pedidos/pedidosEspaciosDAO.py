from typing import override
from core.Implements.pedidos.pedidosDAO import PedidosDAO
from core.Entities.pedidos.pedidosEntity import PedidosEntity
from core.Interface.pedidos.Ipedidos import IPedidos
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
from config.Logs.LogsActivity import Logs
class PedidosEspaciosDAO(PedidosDAO,IPedidos):
    def __init__(self):
        super().__init__()
    
    @override
    def crearPedido(self, pedido: PedidosEntity, sede: str) -> PedidosEntity:
        try:
            conexion=self.connect()
            validacionTotal=self.validacion.validarTotal(pedido.total)
            validacionCantidad=self.validacion.validarCantidad(pedido.cantidad)
            if conexion['status'] == True:
              if validacionCantidad ==True and validacionTotal ==True:
                  with self.conn.cursor() as cur :
                  
                    cur.execute(f"""insert into pedidos_espacios(idorden,idproducto,cantidad,total)
               values('{pedido.idOrden}','{pedido.idProducto}','{pedido.cantidad}','{pedido.total}'
               )
                """)
                    self.conn.commit()
                    self.descontarInventario(pedido,sede)
                  return ResponseInternal.responseInternal(True,f"Pedido creado de manera exitosa :[{pedido}]",pedido)
              else: 
                  return ResponseInternal.responseInternal(False,"Esta insertando un cantida o total erronesa valiede sus datos por pavor ",None)
                  
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error de bido a que ya existe un pedido con eses datos  {pedido} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
    
    