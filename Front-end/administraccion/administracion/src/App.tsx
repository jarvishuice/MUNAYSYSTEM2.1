import { useState } from 'react'
import './App.css'
//import { BarraNavegacion } from './controller/Components/barraNavegacion'
import { POS } from './views/POS'
import { Navegacion } from './controller/Components/navegacion'

function App() {
  const [componente,setComponente] = useState(<POS/>)
  let activarComponente=(vista:any)=>{
  setComponente(vista);
 };
  return (

    <>
 {/**  <BarraNavegacion setComponente={activarComponente}/>*/}
 <Navegacion setComponente={activarComponente}></Navegacion>
  <div className='container-fluid'>
{componente}
  </div>
     
    </>
  )

}

export default App
