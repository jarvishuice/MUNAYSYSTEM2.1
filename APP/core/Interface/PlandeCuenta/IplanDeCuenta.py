from core.Entities.PlanDeCuentas.PlanDeCuentas import PlanDeCuentaEntity
from abc import ABC,abstractmethod
from config.Logs.LogsActivity import Logs
class IPlanDeCuenta(ABC):
    def __init__(self):
        Logs.WirterTask("new implement IPagos")
    @abstractmethod
    def getFormPayBySede(sede)->list[PlanDeCuentaEntity]:
        pass
  