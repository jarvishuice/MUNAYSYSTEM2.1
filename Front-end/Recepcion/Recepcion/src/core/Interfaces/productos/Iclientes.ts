import { ProductosEntity } from "../../Entities/productos/productos";


export abstract class IProductos {
    
    abstract BuscarProductos(nombre: string|any): Promise<ProductosEntity[]>;
    abstract ProductosByCategoriaandSede(Categoria:string,sede:string):Promise<ProductosEntity[]>
    
  }
  