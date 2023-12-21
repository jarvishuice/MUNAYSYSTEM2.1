import { MetricCoffeshopEntity } from "../../../Entities/metric/coffeshop/MetricCoffeshopEntity";

export abstract class IMetricCoffeshop {
    abstract ExtraerMetricasBySede(sede:string):Promise<MetricCoffeshopEntity|null>;
    abstract ExtraerMetricasGlobales():Promise<MetricCoffeshopEntity|null>
  }