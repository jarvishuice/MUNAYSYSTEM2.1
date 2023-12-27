# Consultas de postgresql para la operativa de coffeshop

## Deudas clientes 

1. esta consulta extare toda las deudas  del  cliente recibinedo como parametro de sede  

```sql
select sum (o.total) as deuda,count(o.total) as cantidad_ordenes,c.nombre,c.id,c.ci from  ordenes o
inner join clientes c on c.nombre=c.nombre and c.id=c.id and c.ci =c.ci
where o.status ='por pagar' and o.sede='jalisco' and c.id=o.idcliente  
group by c.nombre ,c.id
```


2.  genera el detalle de las ordenes no han sido pagadas segun la sede este recibe dos parametro (sede , idcliente)
```sql 
select o.id,o.sede,o.fechapedido ,p.nombre,p.precio,pe.cantidad,pe.total
from pedidos pe 
inner join ordenes o on o.id=o.id and o.sede = o.sede and o.fechapedido =o.fechapedido 
inner join productos p  on p.nombre =p.nombre  and p.precio = p.precio
 where  o.status = 'por pagar' and p.id = pe.idproducto and o.id= pe.idorden and sede = 'jalisco' and o.idcliente =2007
 order by o.id desc 
```
3.  ingreso de nuevos productos en el cafetin 
```sql 
INSERT INTO public.inventariocfm (id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES(66, 'promo 2x5 ROLLO DE JAMON' , 'https://images-gmi-pmc.edge-generalmills.com/3c42d4c4-17bb-4729-9c3e-983b569c3243.jpg', 5, 20, 'alimentos', NULL);
INSERT INTO public.inventariojalisco (id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES(66, 'promo 2x5 ROLLO DE JAMON' , 'https://images-gmi-pmc.edge-generalmills.com/3c42d4c4-17bb-4729-9c3e-983b569c3243.jpg', 5, 20, 'alimentos', NULL);
INSERT INTO public.productos(id, nombre, urlimagen, precio, cantidad, tipo, almacen) VALUES(66, 'promo 2x5 ROLLO DE JAMON', 'https://images-gmi-pmc.edge-generalmills.com/3c42d4c4-17bb-4729-9c3e-983b569c3243.jpg', 5, 20, 'alimentos', NULL);
```
4. detalle de deuda de  un cliente por pagar
```sql 
select c.nombre as cliente ,p.idorden,i.nombre,p.cantidad,p.total,o.fechaPedido as deudaTotal from pedidos p
inner join productos i on i.nombre=i.nombre
inner join ordenes o on o.fechapedido = o.fechapedido
inner join clientes c on c.nombre =c.nombre

where o.idcliente ='1142' and sede='cfm' and i.id=p.idproducto and o.id = p.idorden and o.status='por pagar' and o.idcliente = c.id
group by c.nombre ,p.idorden,i.nombre,p.cantidad,p.total,o.fechapedido;
```
5. obtener la ultima cotizacion del dollar BCV registrada en el sistema 
```sql
select precio from tazadollar t  order by id desc limit 1 
```
6. Obtener acumulado de ordenes pagaadas en el mes actual 
```sql 
SELECT SUM(total) AS total 
FROM ordenes 
WHERE status = 'pagado' 
AND sede = 'jalisco'  
AND EXTRACT(MONTH FROM fechapago) = EXTRACT(MONTH FROM CURRENT_DATE)
AND EXTRACT(YEAR FROM fechapago) = EXTRACT(YEAR FROM CURRENT_DATE);
```

7. obtener detalles de la ordenes por id 
```sql select o.fechaPedido,i.nombre ,p.cantidad,i.precio,p.total from pedidos p 
inner join productos i on i.precio=i.precio and i.nombre=i.nombre
inner join ordenes o on o.fechapedido =o.fechapedido 
where o.id = '1699107240' and i.id=p.idproducto and p.idorden ='1699107240'
``` 
8. eliminar ordenes 
``` sql 
delete from pedidos where idorden='{idOrden}';

delete from ordenes where id='{idOrden}'
```
9. ordenes detalladas entity
```sql
                        select o.id,c.nombre,total,date(o.fechapedido) as fecha , to_char(o.fechapedido ,'hh12:MI:SS AM') as hora  , o.status from ordenes o
inner join clientes c on c.nombre =c.nombre
where c.id=o.idcliente and o.sede='{sede}' and o.status = 'por pagar'  order  by o.fechapedido desc 
```