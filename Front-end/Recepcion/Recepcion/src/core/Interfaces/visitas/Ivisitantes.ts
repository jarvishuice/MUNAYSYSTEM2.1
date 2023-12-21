import { ClientesEntity } from "../../Entities/clients/clients";

 export abstract class  IVisitantes{

abstract crearVisitante(visitante:ClientesEntity):Promise<ClientesEntity|null>
abstract buscarVisitante(ci:string):Promise<ClientesEntity[]|[]>;
abstract getAllVisitante():Promise<ClientesEntity[]|[]>
}