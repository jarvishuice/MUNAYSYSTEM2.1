
import { DetailVisitasEntity, VisitasEntity } from "../../Entities/visistas/visitasEntity";


export abstract class Ivisitas {
    /**
     * Creates a new visita with the given entity.
     * @param visita The visita entity to create.
     * @returns A promise that resolves with the created visita or null if unsuccessful.
     */
    abstract crearVisita(visita: VisitasEntity): Promise<VisitasEntity | null>;

    /**
     * Marks the visita with the specified ID as salida (exit).
     * @param idVisita The ID of the visita to mark as salida.
     * @returns A promise that resolves with true if successful, false otherwise.
     */
    abstract salidaVisita(idVisita: string): Promise<boolean>;

    /**
     * Retrieves all visitas for the specified sede (location).
     * @param sede The sede (location) to retrieve visitas for.
     * @returns A promise that resolves with an array of VisitasEntity objects or an empty array if no visitas are found.
     */
    abstract getAllVisitasDay(sede: string): Promise<VisitasEntity[] | []>;

    /**
     * Filters visitas by the specified motivo (reason) and sede (location).
     * @param motivo The motivo (reason) to filter visitas by.
     * @param sede The sede (location) to filter visitas by.
     * @returns A promise that resolves with an array of VisitasEntity objects or an empty array if no visitas match the criteria.
     */
    abstract getFilterByMotivoAndSede(motivo: string, sede: string): Promise<VisitasEntity[] | []>;

    /**
     * Retrieves visitas with the specified status for the specified sede (location).
     * @param sede The sede (location) to retrieve visitas for.
     * @param status The status to filter visitas by.
     * @returns A promise that resolves with an array of VisitasEntity objects or an empty array if no visitas are found.
     */
    abstract getVisitasByStatus(sede: string, status: string): Promise<VisitasEntity[] | []>;

    /**
     * Retrieves detailed information about visitas for today for the specified sede (location).
     * @param sede The sede (location) to retrieve visitas for.
     * @returns A promise that resolves with an array of DetailVisitasEntity objects or an empty array if no visitas are found.
     */
    abstract getVisitasDetailToday(sede: string): Promise<DetailVisitasEntity[] | []>;
}
  