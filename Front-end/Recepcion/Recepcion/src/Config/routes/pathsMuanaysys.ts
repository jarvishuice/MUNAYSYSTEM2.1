export class PATHMUNAYSYSY {
  // datos de conexion del API 
  private ipAPI = '191.97.17.26'; //Ip primaria 
  private ipAPIRespaldo = '190.94.248.62'; //IP de respaldo
  private PortAPI = '8010'; //puerto de escucha del  api 

  private CompanyName = 'nest';

  constructor() {
      console.log("Iniciando el path munaysysy");
  }

  public PathAPI(): string {
      
      const apiValidator= this.checkApiResponse()
      if (apiValidator ===true){
        return `http://${this.ipAPI}:${this.PortAPI}/MUNAY/${this.CompanyName}/`
      }
      else{
        return `http://${this.ipAPIRespaldo}:${this.PortAPI}/MUNAY/${this.CompanyName}/`
      }
  }
  private checkApiResponse():boolean{
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `http://${this.ipAPI}:${this.PortAPI}/MUNAY/${this.CompanyName}/test`, false); // Configura la solicitud como síncrona
    xhr.send();
   if (xhr.status === 200){
    return true
   }
   else {
    console.log("error en la api ")
    return false
  };
  }

  
}
