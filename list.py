from node import Node
import pygame
import sys
import time


class NodeL(Node):
    def __init__(self, nodeX, nodeY, nodeValue, screen, nodeImg):
        super().__init__(nodeX, nodeY, nodeValue, screen, nodeImg)
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.nodeValue

    def set_data(self, value):
        self.nodeValue = value


class List:
    def __init__(self, screen, img_list, menu, buttons_set_active):
        self.head = None
        self.screen = screen
        self.center = self.screen.get_rect().center
        self.img_list = img_list
        self.menu = menu
        self.blue = (44, 118, 219)
        self.buttons_set_active = buttons_set_active

    def displayUpdate(self):
        self.buttons_set_active(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.menu.react(event)

        current_node = self.head
        while current_node is not None:
            if current_node.get_next() is not None and self.head.nodeSize == self.head.oriSize[0]:
                scords = [current_node.nodeX + 64, current_node.nodeY + 32]
                ecords = [current_node.get_next().nodeX - 12, current_node.get_next().nodeY + 32]
                if scords[1] == ecords[1]:
                    current_node.arrowBG([scords[0], scords[1] - 32], [64, 128])
                else:
                    current_node.arrowBG([scords[0] - 10, current_node.get_next().nodeY - 64], [74, 220])

                current_node.arrow(self.blue, self.blue, scords, ecords, 5)
            current_node.nodeBG()
            current_node.grow()
            current_node = current_node.get_next()
        pygame.display.update()
        self.buttons_set_active(1)

    def shift_nodes(self, value, node):
        current_node = node
        while current_node is not None:
            current_node.nodeBG()
            current_node.nodeX += value
            current_node = current_node.get_next()
            self.displayUpdate()

    def add(self, value):
        if self.size() == 0:
            n = NodeL(self.center[0] - 32, self.center[1], str(value), self.screen, self.img_list[5])
        else:
            n = NodeL(self.head.nodeX - 128, self.center[1], str(value), self.screen, self.img_list[5])
        n.set_next(self.head)
        self.head = n
        while self.head.nodeSize < self.head.oriSize[0]:
            self.displayUpdate()
        if self.size() > 1:
            self.shift_nodes(64, self.head)

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def moveNode(self, n):
        diffY = n.nodeY + 128
        while n.nodeY <= diffY:
            n.nodeY += diffY / 1000
            self.displayUpdate()
        n.nodeY = diffY

    def remove(self, n):
        current_node = self.head
        if current_node.get_next() is None and current_node.get_data() == n:
            remove_node = current_node
            self.head = None
            time.sleep(1)
            remove_node.nodeBG()
            self.displayUpdate()
            return remove_node

        while current_node.get_next() is not None:
            if current_node.get_data() == n:
                remove_node = current_node
                self.head = current_node.get_next()
                remove_node.arrowBG([remove_node.nodeX + 64, remove_node.nodeY], [64, 64])
                self.displayUpdate()
                time.sleep(2)
                remove_node.nodeBG()
                self.displayUpdate()
                self.shift_nodes(-64, self.head)
                return remove_node
            elif current_node.get_next().get_data() != n:
                current_node = current_node.get_next()
            elif current_node.get_next().get_data() == n and current_node.get_next().get_next() is not None:
                self.moveNode(current_node.get_next())
                remove_node = current_node.get_next()
                current_node.set_next(current_node.get_next().get_next())
                time.sleep(2)
                pygame.display.update()
                current_node.arrowBG([current_node.nodeX + 64, current_node.nodeY], [64, 192])
                pygame.display.update()
                self.displayUpdate()
                time.sleep(2)
                remove_node.nodeBG()
                remove_node.arrowBG([remove_node.nodeX + 64, current_node.get_next().nodeY],
                                    [128, remove_node.nodeY + 64 - current_node.get_next().nodeY])
                self.displayUpdate()
                self.shift_nodes(-128, current_node.get_next())
                self.shift_nodes(64, self.head)
                return remove_node
            elif current_node.get_next().get_data() == n and current_node.get_next().get_next() is None:
                remove_node = current_node.get_next()
                current_node.arrowBG([current_node.nodeX + 64, current_node.nodeY], [64, 64])
                pygame.display.update()
                time.sleep(2)
                remove_node.nodeBG()
                current_node.set_next(None)
                self.displayUpdate()
                self.shift_nodes(64, self.head)
                return remove_node
