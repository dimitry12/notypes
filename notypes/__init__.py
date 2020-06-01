from typing import (
    Protocol,
    NewType,
    Mapping,
    List
)
from abc import (
    abstractclassmethod,
    abstractstaticmethod,
    abstractmethod,
    abstractproperty
)
# https://www.python.org/dev/peps/pep-0544/

class StructuralEquation(Protocol):
    @abstractproperty
    alias: str

class Variable

class Value(Protocol):
    pass

Observation = NewType('Observation', Mapping[Variable, Value])
Intervention = NewType('Intervention', Mapping[Variable, Value])

class FitReport(Protocol):
    @abstractproperty
    likelihoodBefore: float

    @abstractproperty
    likelihoodAfter: float

    @abstractproperty
    updatedEquations: List[StructuralEquation]


class Model(Protocol):
    @abstractmethod
    def fit(self, obs: Observation, act: Intervention) -> FitReport:
        raise NotImplementedError