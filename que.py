import node
import pygame
import sys
import time


class Queue:
    def __init__(self, screen, img_list, menu, buttons_set_active):
        self.nodeList = []
        self.queueList = []
        self.screen = screen
        self.center = self.screen.get_rect().center
        self.img_list = img_list
        self.menu = menu
        self.currentSize = 0
        self.buttons_set_active = buttons_set_active

    def displayUpdate(self):
        # pygame.event.pump()
        self.buttons_set_active(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.menu.react(event)
        #   odświeżenie screena
        for i in range(len(self.nodeList)):
            self.nodeList[i].nodeBG()
        for i in range(len(self.nodeList)):
            self.nodeList[i].grow_cvp(-5, -40)
        pygame.display.update()
        self.buttons_set_active(1)

    def shift_nodes(self):
        for i in range(self.currentSize):
            self.nodeList[i].nodeX += 50
            self.displayUpdate()

    def push(self, value):
        if not self.nodeList:
            n = node.Node(self.center[0] - 128, self.center[1], str(value), self.screen, self.img_list[7])
        else:
            n = node.Node(self.nodeList[0].nodeX - 100, self.nodeList[0].nodeY, str(value), self.screen,
                          self.img_list[7])
        self.currentSize += 1
        self.nodeList.insert(0, n)
        self.queueList.insert(0, value)
        while self.nodeList[0].nodeSize < self.nodeList[0].oriSize[0]:
            self.displayUpdate()
        if self.currentSize > 1:
            self.shift_nodes()
        time.sleep(0.5)
        self.nodeList[0].nodeSize = self.nodeList[0].oriSize[0]
        if self.nodeList[0].nodeSize == self.nodeList[0].oriSize[0]:
            self.nodeList[0].oriNodeImg = self.img_list[4]
            self.displayUpdate()

    def pop(self):
        self.nodeList[len(self.nodeList) - 1].oriNodeImg = self.img_list[6]
        self.displayUpdate()
        time.sleep(0.5)
        if self.currentSize > 1:
            del self.nodeList[len(self.nodeList) - 1]
            self.queueList.pop()
            self.currentSize -= 1
            self.shift_nodes()
            return
        if self.currentSize == 1:
            self.nodeList[0].nodeBG()
            del self.nodeList[0]
            self.queueList.pop()
            self.currentSize -= 1
            pygame.display.update()

