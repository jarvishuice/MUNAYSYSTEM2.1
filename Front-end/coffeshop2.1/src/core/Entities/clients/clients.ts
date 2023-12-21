export interface ClientesEntity {
    id:             number;
    nombre:         string;
    apellido:       string;
    correo:         string;
    tlf:            string;
    fechaingreso:   string;
    fechacambio:    string|null;
    codigo:         string|null;
    credito:         string|null;
    ci:             string|null;
    identificacion: string|null;
    direccion:      string;
    deuda:          string|null;
}