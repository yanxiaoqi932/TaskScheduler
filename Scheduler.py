import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # if __file__ not exist, use 'file'
sys.path.append(os.path.dirname(SCRIPT_DIR))
from abc import ABCMeta, abstractmethod
from typing import List

class Scheduler(metaclass=ABCMeta):
    @abstractmethod
    def init(self, driver_num: int) -> None:
        pass

    @abstractmethod
    def schedule(self, logical_clock: int, request_list: list, driver_statues: list) -> list:
        pass

class FinalScheduler(Scheduler):
    def __init__(self):
        pass
        
    def init(self, driver_num: int) -> None:
        pass
        
    def schedule(self, logical_clock: int, request_list: List, driver_statues: List) -> List:
        pass