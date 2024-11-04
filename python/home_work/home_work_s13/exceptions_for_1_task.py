
class MyExceptions(Exception):
    def __init__(self,data = None):
        self.data = data
    def __str__(self):
        return f'{self.data}'
class KillError(MyExceptions):
    def __init__(self):
        super().__init__('Error: user died')

class DrunkError(MyExceptions):
    def __init__(self):
        super().__init__('Error: user drink soda too much')

class CarCrashError(MyExceptions):
    def __init__(self):
        super().__init__('Error: user was hit by a car')

class GluttonyError(MyExceptions):
    def __init__(self):
        super().__init__('Error: user eat too much food')
        
class DepressionError(MyExceptions):
    def __init__(self):
        super().__init__("Error: user's psyche could not stand it")

