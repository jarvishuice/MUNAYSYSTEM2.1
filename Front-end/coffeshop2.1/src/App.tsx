import { useState } from 'react'
import './App.css'
import { BarraNavegacion } from './controller/Components/barraNavegacion'
import {POS} from './views/POS'


function App() {

 const [componente,setComponente] = useState(<POS/>)
  let activarComponente=(vista:any)=>{
  setComponente(vista);
 };
  return (

    <>
  <BarraNavegacion setComponente={activarComponente}/>
  <div className='container-fluid'>
{componente}
  </div>
     
    </>
  )
}

export default App
