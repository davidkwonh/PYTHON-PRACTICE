import time

def causeError():
    return 1/0

#   File "ERROR.py", line 2, in causeError
#     return 1/0
# ZeroDivisionError: division by zero

def callCauseError():
    return causeError()

print(callCauseError())

#   This is called stack trace where the stack is added to one another for erros

# Input In [4], in <module>
#       4 def callCauseError():
#       5     return causeError()
# ----> 7 callCauseError()
#
# Input In [4], in callCauseError()
#       4 def callCauseError():
# ----> 5     return causeError()
#
# Input In [4], in causeError()
#       1 def causeError():
# ----> 2     return 1/0

try:
    1/0
except Exception as e:
    print(type(e))

#   Exceptions and Errors are just clasess, using try and except to catch the error


#   Handling Exceptions and Errors

def causeError():
    try:
        return 1 / 1
    except Exception:
        print('There was some sort of error!')

    #   finally will always return what is in it no matter if the try is called or not
    finally:
        print('This will always execute!')

causeError()


#   common use of try and finally is to catch timing of runtime

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1 / 0
    except Exception:
        print('There was some sort of error!')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

#   different types of errors
#   order of except statements matter
def causeError():
    try:
        return 1 + 'a'

    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception:
        print('There was some sort of error!')

#   Creating a custom decorator to handle all different types of fucntions and their potential errors

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sort of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()

#   Raising Exceptions

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)


raiseError(1)

 