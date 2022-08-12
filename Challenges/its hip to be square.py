# Objectives
#
# 1. Create a function that draws a square on the terminal
# 2. Pass in arguements the size of square


# Brainstorm
#
# How does one draw on terminal?
# curses, sys, numpy (matrix?)
# How will we make a square?
#
# User Input?


import time
import sys
import numpy
import curses
import tkinter


# scr = curses.initscr()


def move_left():
    y, x = curses.getyx()
    curses.move(y, x - 1)


# import curses
#
window = curses.initscr()


# Creating an object of Square with length and width as parameters

class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width


# def main():
#     width = int(input("what is the width of the box: "))
#     height = int(input("what is the length of the box: "))
#
#     box = Square(height, width)

# function that draws the square utilizing the turtle library

# def drawsquare(w, h):
#     for i in range(w):
#         time.sleep(.5)
#         sys.stdout.write(". ")
#     for k in range(h - 1):
#         time.sleep(.5)
#         sys.stdout.write("\n" + " " * 2 * (h - 1) + ".")
#     for b in range(w - 1):
#         time.sleep(.5)
#         move_left()
#         (sys.stdout.write("\b" + " ."))
#
#
# #
# drawsquare(5, 5)
#
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width = 100, height = 100, bd = 0, highlightthickness = 0)
# canvas.create_text(1,1)