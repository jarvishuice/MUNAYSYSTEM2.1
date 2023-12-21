/**
 * @author: Jarvis huice 
 * @description: este componente genera una tarjeta con grafico de linea sirve para previsualizar como va la venta del dia 
 * @param props.valor: valor actual 
 * @param props.meta: valor al que debemos llegar
 * @param props.indicadorName: nombre de la metrica 
 */


import Card from '@mui/joy/Card';
import CardContent from '@mui/joy/CardContent';

import CircularProgress from '@mui/joy/CircularProgress';
import Typography from '@mui/joy/Typography';
import SvgIcon from '@mui/joy/SvgIcon';

export  function CardIndicador(props:any) {
  return (
    <Card size="sm" sx={{ width: 200,height:100 }} variant="outlined" color="primary" invertedColors>
      <CardContent orientation="horizontal">
        <CircularProgress size="lg" determinate value={(props.valor * 100)/props.meta}>
          <SvgIcon>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941"
              />
            </svg>
          </SvgIcon>
        </CircularProgress>
        <CardContent>
          <Typography level="body-md">{props.indicadorName}</Typography>
          <Typography level="h3">$ {props.valor}</Typography>
        </CardContent>
      </CardContent>
     
    </Card>
  );
}