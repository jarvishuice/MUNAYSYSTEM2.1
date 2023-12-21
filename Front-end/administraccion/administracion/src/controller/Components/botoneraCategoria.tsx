import { useState } from "react"


export function BotoneraCategoria(props:any){

  
  const[categoria,setCategoria]= useState('')
  
  const insertarCategoria = (cate:string)=>{
    setCategoria(cate);
    props.Categoria(cate);

    localStorage.setItem('categoria',categoria)

  }

 
 

    return (<div className="btn-group  mt-2" role="group" aria-label="Basic outlined example">
    <button type="button" className="btn btn-outline-secondary" key='1' onClick={()=>{insertarCategoria('cafe')}}>Cafe</button>
    <button type="button" className="btn btn-outline-secondary" key='2' onClick={()=>{insertarCategoria('bebidas')}}>Bebidas</button>
    <button type="button" className="btn btn-outline-secondary" key='3' onClick={()=>{insertarCategoria('snack')}}>Postres</button>
    <button type="button" className="btn btn-outline-secondary" key='4' onClick={()=>{insertarCategoria('alimentos')}}>Alimentos</button>
  </div>)
}