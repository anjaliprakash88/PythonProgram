# # STACK
#
# # Push
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# stack.append(60)
# print(stack)
#
# # Pop
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
#
# # isEmpty
# # Using len()
# print(len(stack) == 0)
# print(not stack) # if empty it print true
#
#
# # peek/Top
# print(stack[-1])


# EXAMPLE
# stack = []
#
#
# def push():
#     element = input("enter the elements:")
#     stack.append(element)
#     print(stack)
#
#
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         c = stack.pop()
#         print("removed element", c)
#         print(stack)
#
#
# while True:
#     print("select the operation 1.push 2.pop 3.quit")
#     choice = int(input("enter the number"))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("enter the correct operation")
#
# Example-2
# stack = []
#
#
# def push():
#     if len(stack) == n:
#         print("list is full")
#     else:
#         element = input("enter the elements:")
#         stack.append(element)
#         print(stack)
#
#
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         c = stack.pop()
#         print("removed element", c)
#         print(stack)
#
#
# n = int(input("enter the limits"))
# while True:
#     print("select the operation 1.push 2.pop 3.quit")
#     choice = int(input("enter the number"))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("enter the correct operation")


# import collections
# stack = collections.deque()
# print(stack) # create a empty stack
# stack.append(12)
# stack.append(13)
# stack.append(14)
# stack.append(15)
# print(stack)
# stack.pop()
# print(stack)
# print(not stack)
# print(stack[-1])
#
# import queue
# stack = queue.LifoQueue()
# stack.put(12)
# stack.put(13)
# stack.put(14)
# stack.put(15)
# stack.put(16)
# print(stack.get())
# # while not stack.empty():
# #     print(stack.get())


# QUEUE


