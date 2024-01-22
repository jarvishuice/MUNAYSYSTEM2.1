import { Tabs, TabList, Tab, TabPanel } from "@mui/joy";
import {POSESPACIOS} from "./POS_ESPACIOS";
//import { ORDENESESPACIOS } from "./OrdenesEspacios";
import { DeudasEspaciosTable } from "../controller/Components/DeudasEspaciosTable";
import { GestorPayEspacios } from "../controller/Components/gestorPayEspacios";
import { TableOrderEspacios } from "../controller/Components/tableOrderEspacios";
import { PDFViewer } from "../controller/Components/ReportesEspacios";

export function ESPACIOS(){
return(<Tabs aria-label="Basic tabs" defaultValue={0}>
<TabList>
  <Tab>POS</Tab>

  <Tab>DEUDAS ESPACIOS</Tab>
  <Tab> PAGOS</Tab>

<Tab> ORDENES</Tab>
<Tab> REPORTES</Tab>

</TabList>
<TabPanel value={0}>
<POSESPACIOS></POSESPACIOS>
</TabPanel>
{/* <TabPanel value={1}>
<ORDENESESPACIOS></ORDENESESPACIOS>
</TabPanel>*/}
<TabPanel value={1}>
<DeudasEspaciosTable></DeudasEspaciosTable>
</TabPanel>
<TabPanel value ={2}> 
<GestorPayEspacios.TABLEPAY></GestorPayEspacios.TABLEPAY>
 </TabPanel>
<TabPanel value={3}> 
<TableOrderEspacios></TableOrderEspacios>
</TabPanel>
<TabPanel value={4}>
<PDFViewer></PDFViewer>
</TabPanel>


</Tabs>)


}