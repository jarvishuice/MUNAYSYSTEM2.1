export interface ClientesEntity {
    id:             number;
    nombre:         string;
    apellido:       string;
    correo:         string;
    tlf:            string;
    fechaingreso:   string;
    fechacambio:    string|null;
    codigo:         number|null;
    credito:         number|null;
    ci:             string|null;
    identificacion: string|null;
    direccion:      string;
    deuda:          number|null;
}