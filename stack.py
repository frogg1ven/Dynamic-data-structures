import pygame
import node
import math
import sys
import time


def isEmpty(stack):
    if not len(stack):
        return True
    else:
        return False


def top(stack):
    if stack:
        return stack[len(stack) - 1]
    else:
        return None


def push_node(stack, item):
    stack.append(item)


def pop_node(stack):
    if isEmpty(stack):
        print("Stack Underflow ")
        exit(1)
    return stack.pop()


class Stack:
    def __init__(self, screen, img_list, menu, speed_slider, buttons_set_active):
        self.nodeList = []
        self.stackList = []
        self.screen = screen
        self.center = self.screen.get_rect().center
        self.bottom = self.screen.get_rect().bottom
        self.node_pos = {
            0: [self.center[0], self.bottom - 70],
            1: [self.center[0], self.bottom - 140],
            2: [self.center[0], self.bottom - 210],
            3: [self.center[0], self.bottom - 280],
            4: [self.center[0], self.bottom - 350],
            5: [self.center[0], self.bottom - 420],
            6: [self.center[0], self.bottom - 490],
            7: [self.center[0], self.bottom - 560],
            8: [self.center[0], self.bottom - 630],
            9: [self.center[0], self.bottom - 700],
            10: [self.center[0], self.bottom - 770]
        }
        self.img_list = img_list
        self.currentSize = 0
        self.menu = menu
        self.sortedList = []
        self.tmp = None
        self.speed_slider = speed_slider
        self.sign_font = pygame.font.Font("font/arial.ttf", 64)
        self.buttons_set_active = buttons_set_active

    def displayUpdate(self):
        self.buttons_set_active(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.menu.react(event)
        #   odświeżenie screena
        for i in range(len(self.nodeList)):
            self.nodeList[i].nodeBG()
        if self.tmp is not None:
            self.tmp.nodeBG()
        for i in range(len(self.sortedList)):
            self.sortedList[i].nodeBG()
        for i in range(len(self.nodeList)):
            self.nodeList[i].grow()
        for i in range(len(self.sortedList)):
            self.sortedList[i].grow()
        if self.tmp is not None:
            self.tmp.grow()
        pygame.display.update()
        self.buttons_set_active(1)

    def push(self, value):
        n = node.Node(self.node_pos[len(self.stackList)][0], self.node_pos[len(self.stackList)][1], str(value),
                      self.screen, self.img_list[3])
        self.nodeList.append(n)
        self.stackList.append(value)
        self.currentSize += 1
        while self.nodeList[len(self.nodeList) - 1].nodeSize < self.nodeList[len(self.nodeList) - 1].oriSize[0]:
            self.displayUpdate()

    def pop(self):
        if self.stackList:
            self.nodeList[len(self.nodeList) - 1].nodeBG()
            del self.nodeList[len(self.nodeList) - 1]
            self.displayUpdate()
            ret = self.stackList.pop()
            self.currentSize -= 1
            return ret
        else:
            return None

    def moveNode(self, n, nd):
        diffX = math.fabs(n.nodeX - nd[0])
        diffY = math.fabs(n.nodeY - nd[1])
        if n.nodeX <= nd[0] and n.nodeY < nd[1]:
            while n.nodeX <= nd[0] or n.nodeY <= nd[1]:
                n.nodeX += diffX / 1000 * self.speed_slider.get_value()
                n.nodeY += diffY / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        elif n.nodeX <= nd[0] and n.nodeY > nd[1]:
            while n.nodeX <= nd[0] or n.nodeY >= nd[1]:
                n.nodeX += diffX / 1000 * self.speed_slider.get_value()
                n.nodeY -= diffY / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        elif n.nodeX > nd[0] and n.nodeY < nd[1]:
            while n.nodeX >= nd[0] or n.nodeY < nd[1]:
                n.nodeX -= diffX / 1000 * self.speed_slider.get_value()
                n.nodeY += diffY / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        elif n.nodeX > nd[0] and n.nodeY > nd[1]:
            while n.nodeX >= nd[0] or n.nodeY >= nd[1]:
                n.nodeX -= diffX / 1000 * self.speed_slider.get_value()
                n.nodeY -= diffY / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        elif n.nodeX > nd[0] and n.nodeY == nd[1]:
            while n.nodeX >= nd[0]:
                n.nodeX -= diffX / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        elif n.nodeX <= nd[0] and n.nodeY == nd[1]:
            while n.nodeX <= nd[0]:
                n.nodeX += diffX / 1000 * self.speed_slider.get_value()
                self.displayUpdate()
        n.nodeX = nd[0]
        n.nodeY = nd[1]

    def sign_text(self, sign, x, y):
        sign_text = self.sign_font.render(sign, True, (255, 255, 255))
        self.screen.blit(sign_text, (x, y))
        pygame.display.update()

    def sign_bg(self, x, y):
        time.sleep(1 / self.speed_slider.get_value())
        rect = pygame.Rect((x, y, x + 64, y + 64))
        pygame.draw.rect(self.screen, (0, 0, 0), rect)

    # https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
    def sortStack(self):
        if self.sortedList:
            for i in range(len(self.sortedList)):
                self.sortedList[i].nodeBG()
        self.currentSize = 0
        self.sortedList = []
        self.tmp = None
        self.displayUpdate()
        while not isEmpty(self.nodeList):
            self.tmp = pop_node(self.nodeList)
            self.stackList.pop()
            if self.sortedList:
                self.moveNode(self.tmp, [self.node_pos[len(self.sortedList) - 1][0] + 200,
                                         self.node_pos[len(self.sortedList) - 1][1]])
                if int(top(self.sortedList).nodeValue) <= int(self.tmp.nodeValue):
                    self.sign_text("≥", self.tmp.nodeX + 110, self.tmp.nodeY)
                    self.sign_bg(self.tmp.nodeX + 110, self.tmp.nodeY)
            else:
                self.moveNode(self.tmp, [self.node_pos[0][0] + 200, self.node_pos[0][1]])

            while not isEmpty(self.sortedList) and int(top(self.sortedList).nodeValue) > int(self.tmp.nodeValue):
                if self.tmp.nodeY != self.node_pos[len(self.sortedList) - 1][1]:
                    diffY = math.fabs(self.tmp.nodeY - self.node_pos[len(self.sortedList) - 1][1])
                    while self.tmp.nodeY <= self.node_pos[len(self.sortedList) - 1][1]:
                        self.tmp.nodeY += diffY / 1000 * self.speed_slider.get_value()
                        self.displayUpdate()
                    self.tmp.nodeY = self.node_pos[len(self.sortedList) - 1][1]
                self.sign_text("<", self.tmp.nodeX + 110, self.tmp.nodeY)
                self.sign_bg(self.tmp.nodeX + 110, self.tmp.nodeY)

                push_node(self.nodeList, top(self.sortedList))
                self.stackList.append(int(top(self.sortedList).nodeValue))
                self.moveNode(top(self.sortedList), [self.node_pos[len(self.nodeList) - 1][0],
                                                     self.node_pos[len(self.nodeList) - 1][1]])
                self.sortedList.pop()
            self.sortedList.append(self.tmp)
            self.moveNode(self.tmp, [self.node_pos[len(self.sortedList) - 1][0] + 400,
                                     self.node_pos[len(self.sortedList) - 1][1]])

