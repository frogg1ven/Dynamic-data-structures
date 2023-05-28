import pygame
import time
import node
import math
import sys


class BinHeap:
    def __init__(self, screen, slider, img_list, menu, buttons_set_active, restore_checker):
        self.nodeList = []
        self.heapList = []
        self.currentSize = 0
        self.screen = screen
        self.time = 1
        self.center = self.screen.get_rect().center
        self.node_pos = {
            0: [self.center[0], 50],

            1: [self.center[0] - 260, 50 + 120],
            2: [self.center[0] + 260, 50 + 120],

            3: [self.center[0] - 260 - 130, 50 + 240],
            4: [self.center[0] - 260 + 130, 50 + 240],
            5: [self.center[0] + 260 - 130, 50 + 240],
            6: [self.center[0] + 260 + 130, 50 + 240],

            7: [self.center[0] - 260 - 130 - 65, 50 + 360],
            8: [self.center[0] - 260 - 130 + 65, 50 + 360],
            9: [self.center[0] - 260 + 130 - 65, 50 + 360],
            10: [self.center[0] - 260 + 130 + 65, 50 + 360],
            11: [self.center[0] + 260 - 130 - 65, 50 + 360],
            12: [self.center[0] + 260 - 130 + 65, 50 + 360],
            13: [self.center[0] + 260 + 130 - 65, 50 + 360],
            14: [self.center[0] + 260 + 130 + 65, 50 + 360],

            15: [self.center[0] - 260 - 130 - 65 - 32.5, 50 + 480],
            16: [self.center[0] - 260 - 130 - 65 + 32.5, 50 + 480],
            17: [self.center[0] - 260 - 130 + 65 - 32.5, 50 + 480],
            18: [self.center[0] - 260 - 130 + 65 + 32.5, 50 + 480],
            19: [self.center[0] - 260 + 130 - 65 - 32.5, 50 + 480],
            20: [self.center[0] - 260 + 130 - 65 + 32.5, 50 + 480],
            21: [self.center[0] - 260 + 130 + 65 - 32.5, 50 + 480],
            22: [self.center[0] - 260 + 130 + 65 + 32.5, 50 + 480],
            23: [self.center[0] + 260 - 130 - 65 - 32.5, 50 + 480],
            24: [self.center[0] + 260 - 130 - 65 + 32.5, 50 + 480],
            25: [self.center[0] + 260 - 130 + 65 - 32.5, 50 + 480],
            26: [self.center[0] + 260 - 130 + 65 + 32.5, 50 + 480],
            27: [self.center[0] + 260 + 130 - 65 - 32.5, 50 + 480],
            28: [self.center[0] + 260 + 130 - 65 + 32.5, 50 + 480],
            29: [self.center[0] + 260 + 130 + 65 - 32.5, 50 + 480],
            30: [self.center[0] + 260 + 130 + 65 + 32.5, 50 + 480]
        }
        self.speed_slider = slider
        self.img_list = img_list
        self.blue = (44, 118, 219)
        self.arrowCords = [(), ()]
        self.menu = menu
        self.buttons_set_active = buttons_set_active
        self.restore_checker = restore_checker
        self.sortedList = []
        self.sorted_pos = {
            0: self.center[0] - 487.5,
            1: self.center[0] - 487.5 + 65,
            2: self.center[0] - 487.5 + 65 * 2,
            3: self.center[0] - 487.5 + 65 * 3,
            4: self.center[0] - 487.5 + 65 * 4,
            5: self.center[0] - 487.5 + 65 * 5,
            6: self.center[0] - 487.5 + 65 * 6,
            7: self.center[0] - 487.5 + 65 * 7,
            8: self.center[0] - 487.5 + 65 * 8,
            9: self.center[0] - 487.5 + 65 * 9,
            10: self.center[0] - 487.5 + 65 * 10,
            11: self.center[0] - 487.5 + 65 * 11,
            12: self.center[0] - 487.5 + 65 * 12,
            13: self.center[0] - 487.5 + 65 * 13,
            14: self.center[0] - 487.5 + 65 * 14,
            15: self.center[0] - 487.5 + 65 * 15
        }

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
        for i in range(len(self.sortedList)):
            self.sortedList[i].nodeBG()
        if self.currentSize > 0:
            for i in range(len(self.nodeList)):
                self.arrows(i)
        for i in range(len(self.nodeList)):
            self.nodeList[i].grow()
        for i in range(len(self.sortedList)):
            self.sortedList[i].grow()
        pygame.display.update()
        self.buttons_set_active(1)

    def switch_nodes(self, n1, n2):
        #   graficzna zamiana dwóch węzłów
        diffX = math.fabs(self.nodeList[n1].nodeX - self.nodeList[n2].nodeX)
        diffY = math.fabs(self.nodeList[n1].nodeY - self.nodeList[n2].nodeY)
        diffZ = diffX + diffY

        while round(self.nodeList[n1].nodeX) != self.node_pos[n2][0] and \
                round(self.nodeList[n1].nodeY) <= self.node_pos[n2][1]:
            if self.nodeList[n2].nodeX < self.node_pos[n1][0]:
                if self.speed_slider.get_value():
                    self.nodeList[n1].nodeX -= diffX / diffZ / (4 / self.speed_slider.get_value())
                    self.nodeList[n2].nodeX += diffX / diffZ / (4 / self.speed_slider.get_value())
                else:
                    self.nodeList[n1].nodeX -= 0
                    self.nodeList[n2].nodeX += 0
            else:
                if self.speed_slider.get_value():
                    self.nodeList[n1].nodeX += diffX / diffZ / (4 / self.speed_slider.get_value())
                    self.nodeList[n2].nodeX -= diffX / diffZ / (4 / self.speed_slider.get_value())
                else:
                    self.nodeList[n1].nodeX += 0
                    self.nodeList[n2].nodeX -= 0
            if self.speed_slider.get_value():
                self.nodeList[n1].nodeY += diffY / diffZ / (4 / self.speed_slider.get_value())
                self.nodeList[n2].nodeY -= diffY / diffZ / (4 / self.speed_slider.get_value())
            else:
                self.nodeList[n1].nodeY += 0
                self.nodeList[n2].nodeY -= 0
            self.displayUpdate()
        self.nodeList[n1].nodeX = self.node_pos[n2][0]
        self.nodeList[n1].nodeY = self.node_pos[n2][1]
        self.nodeList[n1].oriNodeImg = self.img_list[0]
        self.nodeList[n2].oriNodeImg = self.img_list[0]
        self.displayUpdate()
        tmp = self.nodeList[n1]
        self.nodeList[n1] = self.nodeList[n2]
        self.nodeList[n2] = tmp

    def switchUp(self, i):
        while (i - 1) // 2 >= 0:
            if self.heapList[i] < self.heapList[(i - 1) // 2]:
                self.nodeList[i].oriNodeImg = self.img_list[1]
                self.nodeList[(i - 1) // 2].oriNodeImg = self.img_list[1]
                self.displayUpdate()
                if self.speed_slider.get_value():
                    time.sleep((1 / self.speed_slider.get_value()))
                self.switch_nodes((i - 1) // 2, i)
                tmp = self.heapList[(i - 1) // 2]
                self.heapList[(i - 1) // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = (i - 1) // 2

    def auto_restore(self, tab):
        i = (len(tab) - 2) // 2
        while i >= 0:
            self.switchDown(i)
            i -= 1

    def restore_one(self, tab):
        i = (len(tab) - 2) // 2
        while tab[self.minChild(i)] >= tab[i] and self.currentSize > 1:
            i -= 1
        if i >= 0:
            self.switchDown(i)

    def heap_push(self, k):
        #   dodanie nowego elementu do kopca
        n = node.Node(self.node_pos[len(self.nodeList)][0], self.node_pos[len(self.nodeList)][1], str(k),
                      self.screen, self.img_list[0])
        self.nodeList.append(n)
        self.heapList.append(k)
        self.currentSize += 1
        while self.nodeList[len(self.nodeList) - 1].nodeSize < self.nodeList[len(self.nodeList) - 1].oriSize[0]:
            self.displayUpdate()
        #   sprawdzenie czy zachowane są własności kopca
        if self.currentSize > 1 and self.restore_checker.get_value() == 1:
            self.switchUp(self.currentSize - 1)

    def switchDown(self, i):
        while (2 * i) + 1 <= self.currentSize - 1:
            min_child = self.minChild(i)
            if self.heapList[i] > self.heapList[min_child]:
                self.nodeList[i].oriNodeImg = self.img_list[1]
                self.nodeList[min_child].oriNodeImg = self.img_list[1]
                self.displayUpdate()
                if self.speed_slider.get_value():
                    time.sleep((1 / self.speed_slider.get_value()))
                self.switch_nodes(i, min_child)
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[min_child]
                self.heapList[min_child] = tmp
            i = min_child

    def minChild(self, i):
        min_child_index = (2 * i) + 1
        if (2 * i) + 2 <= self.currentSize - 1:
            if self.heapList[(2 * i) + 2] < self.heapList[(2 * i) + 1]:
                min_child_index = (2 * i) + 2
        return min_child_index

    def deleteMin(self):
        #   zmiana koloru usuwanego węzła na cerwony
        self.nodeList[0].oriNodeImg = self.img_list[2]
        self.displayUpdate()
        if self.speed_slider.get_value():
            time.sleep((1 / self.speed_slider.get_value()))

        #   graficzne usunięcie korzenia i przeniesienie ostatniego węzła w jego miejsce
        diffX = math.fabs(self.nodeList[0].nodeX - self.nodeList[self.currentSize - 1].nodeX)
        diffY = math.fabs(self.nodeList[0].nodeY - self.nodeList[self.currentSize - 1].nodeY)

        self.sortedList.append(self.nodeList[0])

        diffX1 = math.fabs(self.sortedList[len(self.sortedList) - 1].nodeX -
                           self.sorted_pos[(len(self.sortedList) - 1) % 15])
        diffY1 = math.fabs(self.sortedList[len(self.sortedList) - 1].nodeY - 650)
        diffZ = diffX1 + diffY1

        self.nodeList[0] = self.nodeList[self.currentSize - 1]
        del self.nodeList[len(self.nodeList) - 1]

        if len(self.sortedList) - 1 < 15:
            b = 650
        else:
            b = 720

        while self.sortedList[len(self.sortedList) - 1].nodeY <= b:
            if self.nodeList and self.nodeList[0].nodeX < self.center[0]:
                if self.speed_slider.get_value():
                    self.nodeList[0].nodeX += diffX / diffZ / (4 / self.speed_slider.get_value())
                else:
                    self.nodeList[0].nodeX += 0
            elif self.nodeList and self.nodeList[0].nodeX >= self.center[0]:
                if self.speed_slider.get_value():
                    self.nodeList[0].nodeX -= diffX / diffZ / (4 / self.speed_slider.get_value())
                else:
                    self.nodeList[0].nodeX -= 0
            if len(self.sortedList) <= 8 or 16 <= len(self.sortedList) < 24:
                if self.speed_slider.get_value():
                    self.sortedList[len(self.sortedList) - 1].nodeX -= diffX1 / diffZ / (
                            4 / self.speed_slider.get_value())
                else:
                    self.sortedList[len(self.sortedList) - 1].nodeX -= 0
            elif len(self.sortedList) == 31:
                if self.speed_slider.get_value():
                    self.sortedList[len(self.sortedList) - 1].nodeX += diffX1 / diffZ / (
                            4 / self.speed_slider.get_value())
                else:
                    self.sortedList[len(self.sortedList) - 1].nodeX += 0
            else:
                if self.speed_slider.get_value():
                    self.sortedList[len(self.sortedList) - 1].nodeX += diffX1 / diffZ / (
                        4 / self.speed_slider.get_value())
                else:
                    self.sortedList[len(self.sortedList) - 1].nodeX += 0
            if self.nodeList:
                if self.speed_slider.get_value():
                    self.nodeList[0].nodeY -= diffY / diffZ / (4 / self.speed_slider.get_value())
                else:
                    self.nodeList[0].nodeY -= 0
            if len(self.sortedList) < 16:
                if self.speed_slider.get_value():
                    self.sortedList[len(self.sortedList) - 1].nodeY += diffY1 / diffZ / (
                            4 / self.speed_slider.get_value())
                else:
                    self.sortedList[len(self.sortedList) - 1].nodeY += 0
            else:
                if self.speed_slider.get_value():
                    self.sortedList[len(self.sortedList) - 1].nodeY += (diffY1 + 70) / diffZ / (
                            4 / self.speed_slider.get_value())
                else:
                    self.sortedList[len(self.sortedList) - 1].nodeY += 0
            self.displayUpdate()
        try:
            self.nodeList[0].nodeBG()
            self.nodeList[0].nodeX = self.node_pos[0][0]
            self.nodeList[0].nodeY = self.node_pos[0][1]
            self.displayUpdate()
        except IndexError:
            pass

        #  usunięcie korzenia i przeniesienie ostatniego węzła w jego miejsce
        r = self.heapList[0]
        self.heapList[0] = self.heapList[self.currentSize - 1]
        self.heapList.pop()
        if self.nodeList and (self.currentSize - 2) // 2 >= 0:
            self.del_arrow((self.currentSize - 2) // 2)
        self.currentSize -= 1
        self.displayUpdate()
        self.switchDown(0)
        return r

    def build(self, tab):
        #   zbudowanie kopca z listy wartości
        self.currentSize = len(tab)
        self.heapList = tab
        for j in range(len(tab)):
            n = node.Node(self.node_pos[j][0], self.node_pos[j][1], str(tab[j]), self.screen, self.img_list[0])
            self.nodeList.append(n)
            while self.nodeList[j].nodeSize < self.nodeList[j].oriSize[0]:
                self.displayUpdate()
        if self.restore_checker.get_value() == 1:
            self.auto_restore(tab)

    def arrows(self, i):
        if self.currentSize - 1 >= i * 2 + 1:
            x1 = self.node_pos[i][0] + self.nodeList[i].oriSize[0] / 2
            y1 = self.node_pos[i][1] + self.nodeList[i].oriSize[1]
            if i < 7:
                x2 = self.node_pos[i * 2 + 1][0] + self.nodeList[i].oriSize[1]
            elif i >= 7:
                x2 = self.node_pos[i * 2 + 1][0] + self.nodeList[i].oriSize[1] / 2
            y2 = self.node_pos[i * 2 + 1][1] - 10
            self.nodeList[i].arrow(self.blue, self.blue, (x1, y1), (x2, y2), 10)

        if self.currentSize - 1 >= i * 2 + 2:
            x1 = self.node_pos[i][0] + self.nodeList[i].oriSize[0] / 2
            y1 = self.node_pos[i][1] + self.nodeList[i].oriSize[1]
            if i < 7:
                x2 = self.node_pos[i * 2 + 2][0]
            elif i >= 7:
                x2 = self.node_pos[i * 2 + 2][0] + self.nodeList[i].oriSize[0] / 2
            y2 = self.node_pos[i * 2 + 2][1] - 10
            self.nodeList[i].arrow(self.blue, self.blue, (x1, y1), (x2, y2), 10)

    def del_arrow(self, i):
        if self.currentSize - 1 == i * 2 + 1:
            x1 = self.node_pos[i][0] + self.nodeList[i].oriSize[0] / 2
            y1 = self.node_pos[i][1] + self.nodeList[i].oriSize[1]
            if i < 7:
                x2 = self.node_pos[i * 2 + 1][0] + self.nodeList[i].oriSize[1]
            elif i >= 7:
                x2 = self.node_pos[i * 2 + 1][0] + self.nodeList[i].oriSize[1] / 2
            y2 = self.node_pos[i * 2 + 1][1] - 10
            d1 = x1 - x2
            d2 = y2 - y1
            self.nodeList[i].arrowBG((x2 - 10, y1), (d1 + 20, d2 + 20))

        if self.currentSize - 1 == i * 2 + 2:
            x1 = self.node_pos[i][0] + self.nodeList[i].oriSize[0] / 2
            y1 = self.node_pos[i][1] + self.nodeList[i].oriSize[1]
            if i < 7:
                x2 = self.node_pos[i * 2 + 2][0]
            elif i >= 7:
                x2 = self.node_pos[i * 2 + 2][0] + self.nodeList[i].oriSize[0] / 2
            y2 = self.node_pos[i * 2 + 2][1] - 10
            d1 = x2 - x1
            d2 = y2 - y1
            self.nodeList[i].arrowBG((x1, y1), (d1 + 20, d2 + 20))
