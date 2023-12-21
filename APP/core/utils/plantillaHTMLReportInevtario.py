import datetime
from core.Entities.reports.inventario.ItemsInventarioEntity import ItemsInventarioEntity


class PlantillaHTMLReportInventario():
    def __init__(self):
        pass
    def getHTML(self,datos:ItemsInventarioEntity,sede) :
     self.productos=''
     self.TotalProductos=0
     for i in datos:
        #self.productos +=f"""<tr><th>{i.tipo}</th><td>{i.nombre[0:13]}</td><td>{i.precio}</td> <td>{i.cantidad}</td><td>{round((i.cantidad*i.precio),2)}</td><td></td><td></td><td></td> <td></td></tr>"""
         self.productos +=f"""<tr><th class="categorias">{i.tipo}</th><td class="categorias">{i.nombre[0:13]}</td><td>{i.precio}</td> <td>{i.cantidad}</td><td></td><td></td><td></td> <td></td></tr>"""
         self.TotalProductos +=i.cantidad*i.precio
     
     self.style="""<style>
    body {
      font-family: Arial, sans-serif;
    }

table {
  border-collapse: collapse;
  width: 90%;
  margin-left:5%;
}

th, td {
  border: 1px solid black;
  padding: 1px 1px 1px;
  text-align: center;
}

th {
  background-color: #4682b4;
}

.total {
  font-weight: bold;
  
}
.categorias{
  font-size:12px;
}

</style>"""
     html =f"""
        <!DOCTYPE html>
<html>
<head>
  <title>reporte de inventario</title>
  
</head>
{self.style}
<body>
<div>
<p> fecha de emicion: {datetime.datetime.today()}</p>
 <center> <h1> INVENTARIO ACTUAL {sede.upper()}</h1> 
  <h3> {datetime.date.today()}</h3><br/>
  <h2> Productos </h2></center>
   <table>
    <tr>
     <center> <th >Categoria</th></center>
     <center> <th>Nombre</th></center>
     <center> <th>Precio</th></center>
     <center> <th>Cantidad </th>
  
     <center> <th> Semana 1  </th> </center>
     <center> <th> Semana 2</th></center>
     <center> <th> Semana 3</th></center>
     <center> <th> Semana 4</th></center>
    </tr>
    {self.productos}

  </table>
</div>
</body>
</html>
        """   
     return html     