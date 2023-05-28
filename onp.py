import pygame
import sys
import math
import time


class NodeONP:
    def __init__(self, nodeX, nodeY, nodeValue, screen):
        self.nodeFont = pygame.font.Font("font/arial.ttf", 64)
        self.nodeX = nodeX
        self.nodeY = nodeY
        self.nodeValue = nodeValue
        self.val = self.nodeFont.render(self.nodeValue, True, (255, 255, 255))
        self.screen = screen
        self.right = self.val.get_rect().right
        self.bottom_right = self.val.get_rect().bottomright
        self.color = (0, 0, 0)

    def nodeDisplay(self):
        rect = pygame.Rect((self.nodeX, self.nodeY), self.bottom_right)
        pygame.draw.rect(self.screen, self.color, rect)
        self.screen.blit(self.val, (self.nodeX, self.nodeY))

    def nodeBGB(self):
        rect = pygame.Rect((self.nodeX - 15, self.nodeY - 3), (self.bottom_right[0] + 15, self.bottom_right[1] + 6))
        pygame.draw.rect(self.screen, (0, 0, 0), rect)


def p(c):
    if c == '+':
        return 1
    elif c == '-':
        return 1
    elif c == '*':
        return 2
    elif c == '/':
        return 2
    elif c == '^':
        return 3
    else:
        return 0


class ONP:
    def __init__(self, screen, menu, buttons_set_active, speed_slider):
        self.screen = screen
        self.menu = menu
        self.left = self.screen.get_rect().left
        self.center = self.screen.get_rect().center
        self.node_pos = [self.left, self.center[1]]
        self.oStack = []
        self.whole_eq = None
        self.buttons_set_active = buttons_set_active
        self.nodeList = []
        self.output = []
        self.oStack_pos = [self.screen.get_rect().right - 100, self.screen.get_rect().center[1] + 200]
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.speed_slider = speed_slider
        self.save_eq = None
        self.nodeFont = pygame.font.Font("font/arial.ttf", 32)
        self.txt_stos = self.nodeFont.render("Stos", True, (255, 255, 255))
        self.txt_oper = self.nodeFont.render("operatorów", True, (255, 255, 255))
        self.bottom_right = self.txt_stos.get_rect().bottomright
        self.bottom_right1 = self.txt_oper.get_rect().bottomright
        self.rect = pygame.Rect((self.oStack_pos[0] - 20, self.oStack_pos[1] + 70), self.bottom_right)
        self.rect1 = pygame.Rect((self.oStack_pos[0] - 70, self.oStack_pos[1] + 100), self.bottom_right1)
        self.screen.blit(self.txt_stos, (self.oStack_pos[0] - 20, self.oStack_pos[1] + 70))
        self.screen.blit(self.txt_oper, (self.oStack_pos[0] - 70, self.oStack_pos[1] + 100))

    def displayUpdate(self, node):
        self.buttons_set_active(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.menu.react(event)
        #   odświeżenie screena
        for i in range(len(self.nodeList)):
            if self.nodeList[i] == node:
                self.nodeList[i].nodeBGB()
        self.whole_eq.nodeDisplay()
        for i in range(len(self.nodeList)):
            if self.nodeList[i] == node:
                self.nodeList[i].nodeDisplay()
        for el in self.output:
            el.nodeDisplay()
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect1)
        self.screen.blit(self.txt_stos, (self.oStack_pos[0] - 20, self.oStack_pos[1] + 70))
        self.screen.blit(self.txt_oper, (self.oStack_pos[0] - 70, self.oStack_pos[1] + 100))
        self.menu.blit_and_update()
        pygame.display.update()
        self.buttons_set_active(1)

    def show_equation(self, equation):
        if self.whole_eq:
            self.whole_eq.nodeBGB()
        self.save_eq = equation
        if self.nodeList:
            for e in self.nodeList:
                e.nodeBGB()
            self.oStack = []
            self.nodeList = []
            self.output = []
        if equation[len(equation) - 1] != '=':
            equation += "="
        self.whole_eq = NodeONP(0, self.node_pos[1] - 64, equation, self.screen)
        startX = self.whole_eq.val.get_rect().right
        for e in range(len(equation)):
            if e < 1:
                n = NodeONP(self.center[0] - startX / 2, self.node_pos[1] - 64, equation[e], self.screen)
                self.nodeList.append(n)
            else:
                n = NodeONP(self.nodeList[e - 1].nodeX + self.nodeList[e - 1].right, self.nodeList[e - 1].nodeY,
                            equation[e], self.screen)
                self.nodeList.append(n)
        self.whole_eq.nodeX = self.center[0] - startX / 2
        self.displayUpdate(self.whole_eq)

    def moveNode(self, n1, n2):
        diffX = math.fabs(n1.nodeX - n2[0])
        diffY = math.fabs(n1.nodeY - n2[1])
        if n1.nodeX == n2[0] and n1.nodeY < n2[1]:
            while n1.nodeY <= n2[1]:
                n1.color = self.black
                n1.nodeBGB()
                n1.nodeY += diffY / 1000 * self.speed_slider.get_value() * 1.5
                n1.color = self.red
                self.displayUpdate(n1)
        if n1.nodeX > n2[0] and n1.nodeY < n2[1]:
            while n1.nodeX >= n2[0] or n1.nodeY <= n2[1]:
                n1.color = self.black
                n1.nodeBGB()
                n1.nodeX -= diffX / 1000 * self.speed_slider.get_value() * 1.5
                n1.nodeY += diffY / 1000 * self.speed_slider.get_value() * 1.5
                n1.color = self.red
                self.displayUpdate(n1)
        if n1.nodeX < n2[0] and n1.nodeY < n2[1]:
            while n1.nodeX <= n2[0] or n1.nodeY <= n2[1]:
                n1.color = self.black
                n1.nodeBGB()
                n1.nodeX += diffX / 1000 * self.speed_slider.get_value() * 1.5
                n1.nodeY += diffY / 1000 * self.speed_slider.get_value() * 1.5
                n1.color = self.red
                self.displayUpdate(n1)
        if n1.nodeX > n2[0] and n1.nodeY >= n2[1]:
            while n1.nodeX >= n2[0] or n1.nodeY >= n2[1]:
                n1.color = self.black
                n1.nodeBGB()
                n1.nodeX -= diffX / 1000 * self.speed_slider.get_value() * 1.5
                n1.nodeY -= diffY / 1000 * self.speed_slider.get_value() * 1.5
                n1.color = self.red
                self.displayUpdate(n1)
        n1.nodeX = n2[0]
        n1.nodeY = n2[1]
        n1.color = self.black
        self.displayUpdate(n1)

    def show_onp(self):
        if self.save_eq:
            self.screen.fill((0, 0, 0))
            self.menu.blit_and_update()
            self.show_equation(self.save_eq)
            i = 0
            ni = None
            for element in list(self.nodeList):
                element.color = self.red
                self.displayUpdate(element)
                if element.nodeValue != ' ':
                    if self.speed_slider.get_value() >= 1:
                        time.sleep(1 / self.speed_slider.get_value())
                    if 0 < self.speed_slider.get_value() < 1:
                        time.sleep(2)
                if element.nodeValue == "=":
                    element.color = self.black
                    self.displayUpdate(element)
                    while self.oStack:
                        cordX = self.output[len(self.output) - 1].nodeX + self.output[len(self.output) - 1].right
                        self.moveNode(self.oStack[len(self.oStack) - 1], (cordX, self.output[len(self.output) - 1].nodeY))
                        self.output.append(self.oStack.pop())
                elif element.nodeValue == " ":
                    element.color = self.black
                    pass
                elif element.nodeValue == "(":
                    if self.oStack:
                        cordY = self.oStack[len(self.oStack) - 1].nodeY - element.val.get_rect().bottom
                        self.moveNode(element, (self.oStack_pos[0], cordY))
                    else:
                        self.moveNode(element, (self.oStack_pos[0], self.oStack_pos[1]))
                    self.oStack.append(element)
                    ni = i
                elif element.nodeValue == ")":
                    element.color = self.black
                    self.displayUpdate(element)
                    while self.oStack[len(self.oStack) - 1].nodeValue != "(":
                        cordX = self.output[len(self.output) - 1].nodeX + self.output[len(self.output) - 1].right
                        self.moveNode(self.oStack[len(self.oStack) - 1], (cordX, self.output[len(self.output) - 1].nodeY))
                        self.output.append(self.oStack.pop())
                    self.oStack[len(self.oStack) - 1].nodeBGB()
                    del self.oStack[len(self.oStack) - 1]
                    self.nodeList[ni].color = self.black
                    self.nodeList[ni].nodeBGB()
                    del self.nodeList[ni]
                    self.displayUpdate(element)
                    i -= 1
                elif element.nodeValue == '+' or element.nodeValue == '-' or element.nodeValue \
                        == '*' or element.nodeValue == '/' or element.nodeValue == '^':
                    while self.oStack:
                        if p(element.nodeValue) == 3 or \
                                p(element.nodeValue) > p(self.oStack[len(self.oStack) - 1].nodeValue):
                            break
                        cordX = self.output[len(self.output) - 1].nodeX + self.output[len(self.output) - 1].right
                        self.moveNode(self.oStack[len(self.oStack) - 1], (cordX, self.output[len(self.output) - 1].nodeY))
                        self.output.append(self.oStack.pop())
                    if self.oStack:
                        cordY = self.oStack[len(self.oStack) - 1].nodeY - element.val.get_rect().bottom
                        self.moveNode(element, (self.oStack_pos[0], cordY))
                    else:
                        self.moveNode(element, (self.oStack_pos[0], self.oStack_pos[1]))
                    self.oStack.append(element)
                else:
                    if self.output:
                        cordX = self.output[len(self.output) - 1].nodeX + self.output[len(self.output) - 1].right
                        self.moveNode(element, (cordX, self.output[len(self.output) - 1].nodeY))
                    else:
                        cordX = self.whole_eq.nodeX
                        cordY = self.whole_eq.nodeY + 100
                        self.moveNode(element, (cordX, cordY))
                    self.output.append(element)
                i += 1
