from core.Entities.productos.productosEntity import ProductosEntity
from core.Interface.productos.Iproductos import IProductos
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
import time
from config.Logs.LogsActivity import Logs
class ProductosDAO(ConectionsPsqlInterface,IProductos):
    validacion=validationPedidosData()
    def __init__(self):
        super().__init__()
    def registrarProducto(self,productoData: ProductosEntity) -> ProductosEntity:
        
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""INSERT INTO public.inventariojalisco (id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES((select id from productos p order by p.id  desc limit 1 ), 
                                '{productoData.nombre}', 'https://d1279ybbfotmtl.cloudfront.net/public/img/nofound.png', {productoData.precio}, {productoData.cantidad}, '{productoData.tipo}', NULL);
               INSERT INTO public.inventariocfm(id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES((select id from productos p order by p.id  desc limit 1 ), 
                                '{productoData.nombre}', 'https://d1279ybbfotmtl.cloudfront.net/public/img/nofound.png', {productoData.precio}, {productoData.cantidad}, '{productoData.tipo}', NULL);
               INSERT INTO public.productos (id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES((select id from productos p order by p.id  desc limit 1 ), 
                                '{productoData.nombre}', 'https://d1279ybbfotmtl.cloudfront.net/public/img/nofound.png', {productoData.precio}, {productoData.cantidad}, '{productoData.tipo}', NULL); 
                """)
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 : 
                        return  ResponseInternal.ResponseInternal(True,f"producto registrado con exito{productoData}",productoData)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Erro al intentar registrar un nuevo producto ")
                        return ResponseInternal.responseInternal(False, "error al intentar registrar el producto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,f"error al registrar un producto con eso datos es probabl que ya exista uno similar   {productoData} ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()

    def BuscarProducto(self,name: str) -> list[ProductosEntity]:
        try:
            data=[]
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                                select * from productos where nombre ilike '%{name}%'
                """)
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 : 
                        for i in cur :
                          data.append(ProductosEntity(id=int(i[0]),nombre=str(i[1]),urlimagen=str(i[2]),precio=float(i[3]),cantidad=int(i[4]),tipo=str(i[5]),almacen=str(i[6])))
                        return  ResponseInternal.responseInternal(True,f"Busqueda de producto ({name}) se encontraron ({count}) coincidencias",data)
                    else:
                        
                        return ResponseInternal.responseInternal(True, f"{self.NOTE} no se encontraron coincidencas para el producto ({name}) ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
      
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
    def ProductosByCategoriaandSede(self,categoria: str, sede: str) -> list[ProductosEntity]:
        try:  
            data=[]
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                                select * from inventario{sede} where tipo='{categoria}' and cantidad > 0;
                """)
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 : 
                        for i in cur :
                          data.append(ProductosEntity(id=int(i[0]),nombre=str(i[1]),urlimagen=str(i[2]),precio=float(i[3]),cantidad=int(i[4]),tipo=str(i[5])))
                        return  ResponseInternal.responseInternal(True,f"Busqueda de producto de la categoria  ({categoria}) se encontraron ({count}) coincidencias",data)
                    else:
                        
                        return ResponseInternal.responseInternal(True, f"{self.NOTE} no se encontraron coincidencas para el producto enla categoria ({categoria}) ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
      
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            self.disconnect()
            Logs.WirterTask("Finalizada la busqueda de productos por categoria ")
                  
    
     