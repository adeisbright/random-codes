
class NegativeNumberException(Exception):
    def __init__(self,message):
        pass
        self.message = message 

def readpostint():
    ''' Prompts the user to enter a non-negative number from terminal'''
    try:
        print("Please, enter a non-negative number")
        input_num = input() 
        if(input_num >= 0):
            print("{} is a positive number".format(input_num))
            return 
        else:
            raise NegativeNumberException("This is not a positive integer") 
    except  NegativeNumberException as error : 
        print(error.message)
    except Exception as error :
        print("An error  occured, please check the number you entered")
    finally:
        print("We are done here. We go again another day")
if __name__ == "__main__":
    readpostint()