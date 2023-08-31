class Stack:
    def __init__(self) -> None:
        self.__stack = list()

    def is_empty(self) -> bool: # is_empty — проверка стека на пустоту. Метод возвращает True или False
        if len(self.__stack) == 0:
            return True
        else:
            return False
        
    def push(self, elem) -> None: # push — добавляет новый элемент на вершину стека. Метод ничего не возвращает
        self.__stack.append(elem)
        
    def pop(self): # pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.__stack.pop()
    
    def peek(self): # peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.__stack[-1]
    
    def size(self) -> int: # size — возвращает количество элементов в стеке
        return len(self.__stack)