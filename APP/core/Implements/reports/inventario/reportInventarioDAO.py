import datetime
from core.Interface.reports.inventarrio.IInventario import IInventario,ItemsInventarioEntity
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from core.test.pedidosDataTest.pedidosValidationData import validationPedidosData
from core.utils.plantillaHTMLReportInevtario import PlantillaHTMLReportInventario
import pdfkit

import time

from config.Logs.LogsActivity import Logs
class ReportInventarioDAO(ConectionsPsqlInterface,IInventario):
    validacion=validationPedidosData()
    plantilla=PlantillaHTMLReportInventario()
    OPTIONS = {
                      'page-size': 'Letter', 
      'margin-top': '0.75in',
      'margin-right': '0.75in',
      'margin-bottom': '0.75in', 
      'margin-left': '0.75in'
                    }
    def __init__(self):
        super().__init__()
    def __extraerInventario__(self,sede: str) -> list[ItemsInventarioEntity]:
      
        data=[]
        try:
            conexion=self.connect()
       
            if conexion['status'] == True:
              with self.conn.cursor() as cur :
                  
                    cur.execute(f"""
                           SELECT id,nombre, precio, cantidad, tipo as categoria
FROM inventario{sede} i
WHERE nombre NOT ILIKE '%cafe%' and tipo NOT ILIKE '%cafe%'  order by tipo ;
                                """);
              
             
                    self.conn.commit()
                    count= cur.rowcount
                    if count > 0 :
                        for i in cur :
                         data.append(ItemsInventarioEntity(id=int(i[0]),nombre=str(i[1]),precio=float(i[2]),cantidad=float(i[3]),tipo=str(i[4])))     
                        return  ResponseInternal.responseInternal(True,f"inventario extraido con exito",data)
                    else:
                        Logs.WirterTask(f"{self.ERROR } Error al leer el inventario ")
                        return ResponseInternal.responseInternal(False, "error al intentar registrar el producto ",None)
            else:
                   return ResponseInternal.responseInternal(False,"ERROR DE CONEXION A LA BASE DE DATOS...",None)
        
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
        finally:
            Logs.WirterTask("Finalizada la ejecucion de registros de productos ")
            self.disconnect()
    def generarReporte(self,sede: str):
        try:
            html=''
            output_path =f"assets/reports/inventario/inventario{sede}{datetime.datetime.today()}.pdf"
            datos=self.__extraerInventario__(sede)
            if datos['status'] ==True:
                html=self.plantilla.getHTML(datos['response'],sede)
                pdf=pdfkit.from_string(html,output_path,options=self.OPTIONS)
                return ResponseInternal.responseInternal(True,"reporte de inventario generado con exito",output_path)
            else:
                Logs.WirterTask(f'{self.ERROR} error al extraer los datos del inventario')
                return ResponseInternal.responseInternal(False,"error al extraer los datos del inventario",None)
                
                
            
            
        finally:        
                Logs.WirterTask(f"finalizado el reporte de inventario de la sede {sede}")