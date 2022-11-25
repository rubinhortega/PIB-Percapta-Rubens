import abc
from json import load
from os import stat
from typing_extensions import Self
import pandas as pd
from abc import ABC, abstractclassmethod, abstractmethod

class Config:
    _base_file  = "data/base.xlsx"
    _region     = "UF_Regiao"



class AbstractCalculatePib(ABC):
    class AbstractCalculatePib(ABC):
        @abstractclassmethod
        def get_instance():
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def load_file(self):
            raise RuntimeError('TODO: Método ainda não implementado')
    
        @abstractclassmethod
        def load_uf_by_region(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def print_all_content(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def get_state_by_region(self):
            raise RuntimeError('TODO: Método ainda não implementado')

        @abstractclassmethod
        def get_region_by_state(self):
            raise RuntimeError('TODO: Método ainda não implementado')
  
class CalculatePibPerCaptaSingleton(AbstractCalculatePib):
    # Atributos da classe
    _instance       = None
    raw_data        = None
    current_content = None

    # Métodos
    # Construtor da classe
    def __init__(self):
       # Lançando uma exceção em tempo de execução para quando há mais de uma instãncia sendo criada
        raise RuntimeError('Singleton!!')

    @classmethod
    def instance__(cls):
        print("Test")
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            return cls._instance
        else:
            print("Instance has already been created")          
            return cls._instance

    
    @classmethod
    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(Config._base_file)
        return self.raw_data

    @classmethod
    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, Config._region )
        return self.current_content

    @classmethod
    def print_all_content(self):
        print(self.current_content)

    @classmethod
    def get_state_by_region(self, state):

        print("------- Atividade 1 -------")
        states = self.current_content[self.current_content['Regiao'] == state]
        print(+ states + " |" )

    
    @classmethod
    def get_region_by_state(self, region):

        print("------- Atividade 1 -------")
        regions = self.current_content[self.current_content['Estado'] == region]
        print(+ regions + " |" )

