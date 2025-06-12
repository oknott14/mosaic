from typing import List, TypeVar, Generic, Callable

T = TypeVar('T')

class Event(Generic[T]):
  
  listeners: List[Callable[[T], None]]

  def __init__(self):
    self.listeners = []

  def subscribe(self,func: Callable[[T], None]):
    if func in self.listeners: return
    
    self.listeners.append(func)

  def remove(self, func: Callable[[T], None]):
    if not func in self.listeners: return

    self.listeners.remove(func)

  def emit(self, data: T):
    for listener in self.listeners:
      listener(data)
