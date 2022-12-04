# Practice while loops
from datetime import datetime

datetime.now().second

wait_until = datetime.now().second + 2


#   wasting computation power
# while datetime.now().second != wait_until:
#     print("still waiting")
#
# print(f'we are at {wait_until} seconds')

# practice using pass statements
while datetime.now().second != wait_until:
    pass
    #  nothing to see, move along and preserve indentation and place holder
print(f'we are at {wait_until} seconds')

while datetime.now().second != wait_until:

while True:
    if datetime.now().second == wait_until:
        print(f"we are at {wait_until} seconds")
        break
        #   break statements only get you out of a single while loop

while datetime.now().second != wait_until:
    continue
    #   usually used if statement to prevent code from looping while executing if the condition is met
    print("still waiting")

print(f'we are at {wait_until} seconds')


while True:
    if datetime.now().second < wait_until:
        continue
    break

# rearrange and write code to help other programmers read