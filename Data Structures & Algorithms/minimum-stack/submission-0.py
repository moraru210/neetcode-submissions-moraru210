class MinStack:

    def __init__(self):
        self.stack_list = []
        self.min_stack_list = []
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        
        if not self.min_stack_list:
             self.min_stack_list.append(val)
        else:
            min_val = min(val, self.min_stack_list[-1])
            self.min_stack_list.append(min_val)

    def pop(self) -> None:
        self.stack_list.pop()
        self.min_stack_list.pop()

    def top(self) -> int:
        if not self.stack_list:
            return 0
        else:
            return self.stack_list[-1] 

    def getMin(self) -> int:
        if not self.min_stack_list:
            return 0
        else:
            return self.min_stack_list[-1] 
        
