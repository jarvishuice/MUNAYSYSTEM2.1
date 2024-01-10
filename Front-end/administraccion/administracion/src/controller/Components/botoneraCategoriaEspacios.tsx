import { useState } from "react"


export function BotoneraCategoriaEspacios(props:any){

  
  const[categoria,setCategoria]= useState('')
  
  const insertarCategoria = (cate:string)=>{
    setCategoria(cate);
    props.Categoria(cate);

    localStorage.setItem('categoria',categoria)

  }

 
 

    return (<div className="btn-group  mt-2" role="group" aria-label="Basic outlined example">
    <button type="button" className="btn btn-outline-secondary" key='1' onClick={()=>{insertarCategoria('oficinas')}}>Oficinas</button>
    <button type="button" className="btn btn-outline-secondary" key='2' onClick={()=>{insertarCategoria('escritorios')}}>Escritorios</button>
    <button type="button" className="btn btn-outline-secondary" key='3' onClick={()=>{insertarCategoria('daypass')}}>Daypass</button>
    <button type="button" className="btn btn-outline-secondary" key='4' onClick={()=>{insertarCategoria('espaciosCompartidos')}}>EspaciosCompartido</button>
  </div>)
}