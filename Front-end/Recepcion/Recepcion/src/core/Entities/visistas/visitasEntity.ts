export interface VisitasEntity {
    id:          string;
    idVisitante: number;
    idCliente:   string;
    fIngreso:    string;
    fSalida:     string;
    status:      string;
    sede:        string;
    motivo:      string;
}
export interface DetailVisitasEntity {
    id:        string;
    visitante: string;
    correo:    string;
    ci:        string;
    cliente:   string;
    fIngreso:  Date;
    fSalida:   string;
    status:    string;
    sede:      string;
    motivo:    string;
}
