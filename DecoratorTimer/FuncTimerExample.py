from utils.FuncTimer import FuncTimer

def function_1():
    """
    Example using FuncTimer as a with statement
    """
    with FuncTimer('function_1') as timer:
        for _ in range(20000000):
            pass
        print('test function 1')

@FuncTimer('function_2')
def function_2():
    """
    Example using FuncTimer with decorator
    """
    for _ in range(10000000):
        pass
    print('test function 2')

if __name__ == '__main__':
    for _ in range(30):
        function_2()
    for _ in range(10):
        function_1()

    FuncTimer.printStat()