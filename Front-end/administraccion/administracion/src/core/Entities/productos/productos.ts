export interface ProductosEntity {
    id:        number;
    nombre:    string;
    urlimagen: string;
    precio:    number;
    cantidad:  number;
    tipo:      string;
    almacen:   string|null;
}
