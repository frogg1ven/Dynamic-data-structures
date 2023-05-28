import pygame
import math


class Node:
    def __init__(self, nodeX, nodeY, nodeValue, screen, nodeImg):
        self.oriNodeImg = nodeImg
        self.nodeImg = self.oriNodeImg
        self.nodeFont = pygame.font.Font("font/arial.ttf", 30)
        self.oriSize = self.nodeImg.get_size()
        self.nodeX = nodeX
        self.nodeY = nodeY
        self.nodeValue = nodeValue
        self.val = self.nodeFont.render(self.nodeValue, True, (255, 255, 255))
        self.val_yellow = self.nodeFont.render(self.nodeValue, True, (255, 0, 0))
        self.nodeSize = 1
        self.screen = screen

    def nodeBG(self):
        rect = pygame.Rect((self.nodeX - 6, self.nodeY - 6, self.oriSize[0] + 12, self.oriSize[1] + 12))
        pygame.draw.rect(self.screen, (0, 0, 0), rect)

    def grow(self):
        if self.nodeSize < self.oriSize[0]:
            self.nodeSize = self.nodeSize + 1
        self.nodeImg = pygame.transform.scale(self.oriNodeImg, (self.nodeSize, self.nodeSize))
        self.screen.blit(self.nodeImg, (self.nodeX + int(self.oriSize[0] / 2) - int(self.nodeSize / 2),
                                        self.nodeY + int(self.oriSize[0] / 2) - int(self.nodeSize / 2)))
        if self.nodeSize == self.oriSize[0]:
            val_rect = self.val.get_rect()
            self.screen.blit(self.val, (self.nodeX + int(self.oriSize[0] / 2) - val_rect.center[0],
                                        self.nodeY + int(self.oriSize[0] / 2) - val_rect.center[1]))

    def grow_cvp(self, x, y):
        if self.nodeSize < self.oriSize[0]:
            self.nodeSize = self.nodeSize + 1
        self.nodeImg = pygame.transform.scale(self.oriNodeImg, (self.nodeSize, self.nodeSize))
        self.screen.blit(self.nodeImg, (self.nodeX + int(self.oriSize[0] / 2) - int(self.nodeSize / 2),
                                        self.nodeY + int(self.oriSize[0] / 2) - int(self.nodeSize / 2)))
        if self.nodeSize == self.oriSize[0]:
            val_rect = self.val_yellow.get_rect()
            self.screen.blit(self.val_yellow, (self.nodeX + int(self.oriSize[0] / 2) - val_rect.center[0] + x,
                                               self.nodeY + int(self.oriSize[0] / 2) - val_rect.center[1] + y))

    def arrow(self, lcolor, tricolor, start, end, trirad):
        pygame.draw.line(self.screen, lcolor, start, end, 5)
        rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
        pygame.draw.polygon(self.screen, tricolor, ((end[0] + trirad * math.sin(math.radians(rotation)), end[1] +
                                                     trirad * math.cos(math.radians(rotation))),
                                                    (end[0] + trirad * math.sin(math.radians(
                                                        rotation - 120)),
                                                     end[1] + trirad * math.cos(math.radians(rotation - 120))),
                                                    (end[0] +
                                                     trirad * math.sin(math.radians(rotation + 120)),
                                                     end[1] + trirad * math.cos(math.radians(
                                                         rotation + 120)))))

    def arrowBG(self, start, end):
        rect = pygame.Rect((start[0], start[1] - 2, end[0], end[1]))
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
