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
