from core.Entities.metric.coffeshop.CoffeshopMetrictEntity import CoffeshopMetrictEntity
from core.Interface.metric.coffeshop.ICoffeshopMetric import ImMtericsCoffeshop
from core.config.ResponseInternal import ResponseInternal
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
import time
import datetime
from config.Logs.LogsActivity import Logs
class CoffeshopMetricDAO(ConectionsPsqlInterface,ImMtericsCoffeshop):
  
    def __init__(self):
        super().__init__()
    
    
    def __extraerAcumuladoVentasMesBySede__(self,sede:str)->float:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'pagado' 
AND sede = '{sede}' 
AND EXTRACT(MONTH FROM fechapago) = EXTRACT(MONTH FROM CURRENT_DATE)
AND EXTRACT(YEAR FROM fechapago) = EXTRACT(YEAR FROM CURRENT_DATE);""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()
            
    def  __extraerAcumuladoVentasMesGlobal__(self)->float:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'pagado' 

AND EXTRACT(MONTH FROM fechapago) = EXTRACT(MONTH FROM CURRENT_DATE)
AND EXTRACT(YEAR FROM fechapago) = EXTRACT(YEAR FROM CURRENT_DATE);""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()
    def  __extraerDeudasBySede__(self,sede:str)->float:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'por pagar' and sede ='{sede}' 

""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()    
    def __extraerDeudasGloabl__(self)->float:
        
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'por pagar' 

""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()    
            
    def __extraerAcumuladoVentasDiaBySede__(self,sede:str)->float:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'pagado' 
AND sede = '{sede}' 
and date(fechapago)= ' {datetime.date.today()} '""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                            
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()
            
    def  __extraerAcumuladoVentasDiaGlobal__(self)->float:
        try:
            cantidad=0
            conexion=self.connect()
            if conexion['status']== True:
                with self.conn.cursor() as cur:
                    cur.execute(f"""SELECT COALESCE(SUM(total),0) AS total 
FROM ordenes 
WHERE status = 'pagado' 

and date(fechapago)= ' {datetime.date.today()} '""")
                    count=cur.rowcount
                    if  count > 0 :
                        for i in cur:
                            cantidad=i[0]
                        return ResponseInternal.responseInternal(True,f"Exxito a contar los id{cantidad}",cantidad)
                    else :
                        return ResponseInternal.responseInternal(True,f"error al contar los c;ientes",0)
        except self.INTEGRIDAD_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de integridad en la base de datos {e}")
            return ResponseInternal.responseInternal(False,"ERROR de integridad en la base de datos ",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False,"ERROR de interface en la base de datos ",None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False,"ERROR EN LA BASE DE DATOS",None)
                        
        finally:
            self.disconnect()
    def ExtraerMetricasBysede(self,sede: str) -> CoffeshopMetrictEntity:
        extractorDeudas=self.__extraerDeudasBySede__(sede)
        extractorVentasMes=self.__extraerAcumuladoVentasMesBySede__(sede)
        extractorVentasDias=self.__extraerAcumuladoVentasDiaBySede__(sede)
        extractorVentasMes=self.__extraerAcumuladoVentasMesBySede__(sede)
        error=CoffeshopMetrictEntity(ventasDiarias=0.0,ventasMensual=0.0,deudas=0.0)
        if extractorVentasMes['status'] ==True:
            extractorDeudas=self.__extraerDeudasBySede__(sede)
        
            if extractorDeudas['status'] ==True:
                extractorVentasDias=self.__extraerAcumuladoVentasDiaBySede__(sede)
                if extractorVentasDias['status']==True:
                    return ResponseInternal.responseInternal(True,'metricas extraidas con exito',response=CoffeshopMetrictEntity(ventasDiarias=float(extractorVentasDias['response']),ventasMensual=float(extractorVentasMes['response']),deudas=float(extractorDeudas['response'])))    
                else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)
            else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)    
        else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)        
    def ExtraerMetricasGlobal(self)->CoffeshopMetrictEntity:
        extractorDeudas=self. __extraerDeudasGloabl__()
        extractorVentasMes=self.__extraerAcumuladoVentasMesGlobal__()
        extractorVentasDias=self. __extraerAcumuladoVentasDiaGlobal__()
        extractorVentasMes=self.__extraerAcumuladoVentasMesGlobal__()
        error=CoffeshopMetrictEntity(ventasDiarias=0.0,ventasMensual=0.0,deudas=0.0)
        if extractorVentasMes['status'] ==True:
            extractorDeudas=self. __extraerDeudasGloabl__()
        
            if extractorDeudas['status'] ==True:
                extractorVentasDias=self. __extraerAcumuladoVentasDiaGlobal__()
                if extractorVentasDias['status']==True:
                    return ResponseInternal.responseInternal(True,'metricas extraidas con exito',response=CoffeshopMetrictEntity(ventasDiarias=float(extractorVentasDias['response']),ventasMensual=float(extractorVentasMes['response']),deudas=float(extractorDeudas['response'])))    
                else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)
            else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)    
        else:
                    return ResponseInternal.responseInternal(True,f"{self.ERROR} el core generador de metricas a recibido un status false ",error)                    