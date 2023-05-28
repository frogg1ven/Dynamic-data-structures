import pygame
import thorpy
from binaryHeap import BinHeap
import random
from stack import Stack
from que import Queue
from list import List
from onp import ONP
from justifytext import justify

prev = None
prev1 = None

pygame.init()
pygame.display.set_caption("Dynamiczne struktury danych")
screen = pygame.display.set_mode((1400, 800))
programIcon = pygame.image.load('icon/icon.png')
pygame.display.set_icon(programIcon)


def wyjustuj(text, w):
    final_text = ""
    tab = justify(text, w)
    for j in range(len(tab) - 1):
        final_text += tab[j] + "\n"
    final_text += tab[len(tab) - 1]
    return final_text


# kopiec binarny #################################################################################
insert_val = thorpy.Inserter(name="Wprowadź wartość: ", size=(30, 30))
insert_heap = thorpy.Inserter(size=(150, 30))
insert_min = thorpy.Inserter(name="Min.:", value="0", size=(30, 30))
insert_max = thorpy.Inserter(name="Maks.:",  value="10", size=(30, 30))
insert_size = thorpy.Inserter(name="Rozmiar (maks. 31):",  value="10", size=(30, 30))
speed_text = thorpy.make_text("Wybierz szybkość animacji: ", 12, (0, 0, 0))
prev_step = []
node_blue = pygame.image.load('img/node_img_blue.png').convert_alpha()
node_green = pygame.image.load('img/node_img_green.png').convert_alpha()
node_red = pygame.image.load('img/node_img_red.png'). convert_alpha()
speed_slider = thorpy.SliderX(80, (0, 20), type_=float, initial_value=5.00)
chi = pygame.image.load('img/check_radio.bmp')
restore_checker = thorpy.Checker("Przywróć automatycznie", type_="radio", value=1,
                                 check_img=chi)

# stos ###########################################################################################
lego = pygame.image.load('img/lego.png'). convert_alpha()
insert_val_s = thorpy.Inserter(name="Wprowadź wartość: ", size=(30, 30))
insert_min_s = thorpy.Inserter(name="Min.:", value="0", size=(30, 30))
insert_max_s = thorpy.Inserter(name="Maks.:",  value="10", size=(30, 30))
insert_size_s = thorpy.Inserter(name="Rozmiar (maks. 11):",  value="10", size=(30, 30))
speed_text_s = thorpy.make_text("Wybierz szybkość animacji: ", 12, (0, 0, 0))
speed_slider_s = thorpy.SliderX(80, (0, 10), type_=float, initial_value=1.00)

# kolejka ########################################################################################
queue = pygame.image.load('img/queue.png'). convert_alpha()
queue_red = pygame.image.load('img/queue_red.png'). convert_alpha()
queue_green = pygame.image.load('img/queue_green.png'). convert_alpha()
insert_val_q = thorpy.Inserter(name="Wprowadź wartość: ", size=(30, 30))
insert_min_q = thorpy.Inserter(name="Min.:", value="0", size=(30, 30))
insert_max_q = thorpy.Inserter(name="Maks.:",  value="10", size=(30, 30))
insert_size_q = thorpy.Inserter(name="Rozmiar (maks. 14):",  value="10", size=(30, 30))

# lista ##########################################################################################
square = pygame.image.load('img/square.png'). convert_alpha()
img_list = [node_blue, node_green, node_red, lego, queue, square, queue_red, queue_green]
insert_val_l = thorpy.Inserter(name="Wprowadź wartość: ", size=(30, 30))
insert_min_l = thorpy.Inserter(name="Min.:", value="0", size=(30, 30))
insert_max_l = thorpy.Inserter(name="Maks.:",  value="10", size=(30, 30))
insert_size_l = thorpy.Inserter(name="Rozmiar (maks. 11):",  value="10", size=(30, 30))
insert_remove_l = thorpy.Inserter(name="Wprowadź wartość: ", size=(30, 30))

# ONP ############################################################################################
insert_eq_text = thorpy.make_text("Podaj prawidłowe równanie: ", 12, (0, 0, 0))
insert_eq = thorpy.Inserter(size=(150, 30))
speed_text_onp = thorpy.make_text("Wybierz szybkość animacji: ", 12, (0, 0, 0))
speed_slider_onp = thorpy.SliderX(80, (0, 10), type_=float, initial_value=1.00)


def shift_func(_):
    pressed = pygame.key.get_pressed()
    if insert_eq.get_value():
        if pressed[pygame.K_RSHIFT] and pressed[pygame.K_9]:
            insert_eq.set_value(insert_eq.get_value()[:len(insert_eq.get_value()) - 1] + "(")
        elif pressed[pygame.K_RSHIFT] and pressed[pygame.K_0]:
            insert_eq.set_value(insert_eq.get_value()[:len(insert_eq.get_value()) - 1] + ")")
        elif pressed[pygame.K_RSHIFT] and pressed[pygame.K_8]:
            insert_eq.set_value(insert_eq.get_value()[:len(insert_eq.get_value()) - 1] + "*")
        elif pressed[pygame.K_RSHIFT] and pressed[pygame.K_EQUALS]:
            insert_eq.set_value(insert_eq.get_value()[:len(insert_eq.get_value()) - 1] + "+")
        elif pressed[pygame.K_RSHIFT] and pressed[pygame.K_6]:
            insert_eq.set_value(insert_eq.get_value()[:len(insert_eq.get_value()) - 1] + "^")
        insert_eq.unblit_and_reblit()


inserter_reactionR = thorpy.Reaction(reacts_to=pygame.KEYDOWN, reac_func=shift_func)
insert_eq.add_reaction(inserter_reactionR)


# kopiec binarny #################################################################################
def btn_add_func():
    global prev_step
    prev_step = heap.heapList[:]
    if insert_val.get_value().isdigit() and heap.currentSize < 31:
        heap.heap_push(int(insert_val.get_value()))
    insert_val.set_value("")


def btn_add_random_func():
    global prev_step
    if insert_min.get_value().isdigit() and insert_max.get_value().isdigit() and \
            int(insert_min.get_value()) < int(insert_max.get_value()):
        prev_step = heap.heapList[:]
        if heap.currentSize < 31:
            heap.heap_push(random.randint(int(insert_min.get_value()), int(insert_max.get_value())))


def btn_del_func():
    heap.auto_restore(heap.nodeList)
    if heap.sortedList and heap.nodeList:
        if int(heap.nodeList[0].nodeValue) < int(heap.sortedList[len(heap.sortedList) - 1].nodeValue):
            for node in heap.sortedList:
                node.nodeBG()
            heap.sortedList = []
            heap.displayUpdate()
    global prev_step
    prev_step = heap.heapList[:]
    if heap.currentSize > 0 and len(heap.sortedList) < 31:
        heap.deleteMin()


def is_num(n):
    n = n.replace(',', '.')
    n = n.replace(' ', '')
    if len(n) > 0 and not n[len(n) - 1].isdigit():
        n = n[:len(n) - 1]
    if n.replace('.', '').isdigit():
        return n
    else:
        return ''


def btn_insert_heap_func():
    global prev_step
    val = is_num(insert_heap.get_value())
    if val != '':
        blit_menu(3)
        prev_step = heap.heapList[:]
        lista = val.split('.')
        map_object = map(int, lista)
        int_list = list(map_object)
        heap.build(int_list)
        insert_heap.set_value('')


def btn_undo_func():
    global prev_step
    print(prev_step)
    blit_menu(3)
    heap.build(prev_step)
    heap.displayUpdate()


def btn_random_func():
    global prev_step
    if insert_size.get_value().isdigit() and insert_min.get_value().isdigit() and insert_max.get_value().isdigit() and \
            int(insert_min.get_value()) < int(insert_max.get_value()):
        size = int(insert_size.get_value())
        if insert_min.get_value() != "" and insert_max.get_value() != "" and insert_size.get_value() != "":
            prev_step = heap.heapList[:]
            blit_menu(3)
            int_list = []
            if size > 31:
                size = 31
            for _ in range(0, size):
                int_list.append(random.randint(int(insert_min.get_value()), int(insert_max.get_value())))
            heap.build(int_list)


def btn_restore_func():
    global prev_step
    prev_step = heap.heapList[:]
    if restore_checker.get_value() == 0:
        heap.restore_one(heap.heapList)


def restore_func(_):
    global speed_slider, box_binary_heap, menu
    if restore_checker.get_storer_topleft()[0] < event.pos[0] < restore_checker.get_storer_topleft()[0] + \
            restore_checker.get_storer_size()[0] and restore_checker.get_storer_topleft()[1] < event.pos[1] < \
            restore_checker.get_storer_topleft()[1] + restore_checker.get_storer_size()[1]:
        heap.auto_restore(heap.nodeList)


restore_reaction = thorpy.Reaction(reacts_to=pygame.MOUSEBUTTONDOWN, reac_func=restore_func)
restore_checker.add_reaction(restore_reaction)


def btn_sort_func():
    for node in heap.sortedList:
        node.nodeBG()
    heap.sortedList = []
    heap.displayUpdate()
    global prev_step
    prev_step = heap.heapList[:]
    heap.auto_restore(heap.nodeList)
    while heap.currentSize > 0 and len(heap.sortedList) < 31:
        heap.deleteMin()


def refresh_heap():
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    box_binary_heap.blit()
    heap.displayUpdate()


def btn_add_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj\"", text=wyjustuj("Wprowadź wartość w powyższe pole, a następnie kliknij przycisk \"Dodaj\", a zostanie dodany nowy element o zadanej wartości do kopca binarnego.", 55),
                                 func=refresh_heap, outside_click_quit=True)


def btn_add_random_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj losowo\"", text=wyjustuj("Kliknij przycisk \"Dodaj losowo\", a zostanie dodany nowy element o losowej wartości z przedziału min. - maks. do kopca binarnego.", 55),
                                 func=refresh_heap, outside_click_quit=True)


def btn_del_min_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Usuń min.\"", text=wyjustuj("Kliknij przycisk \"Usuń min.\", aby usunąć element o najmniejszej wartości z kopca binarnego i umieścić go w tablicy przechowującej posortowane elementy.", 50),
                                 func=refresh_heap, outside_click_quit=True)


def btn_add_heap_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj kopiec\"", text=wyjustuj("Wprowadź listę wartości oddzielonych przecinkami w powyższe pole, a następnie kliknij przycisk \"Dodaj kopiec\", a zostanie zbudowany kopiec binarny o zadanych wartościach.", 55),
                                 func=refresh_heap, outside_click_quit=True)


def btn_random_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Losowy kopiec\"", text=wyjustuj("Kliknij przycisk \"Losowy kopiec\", aby stworzyć kopiec binarny o losowych wartościach z przedziału min. - maks. i wielkości zadanej w polu \"Rozmiar\".", 50),
                                 func=refresh_heap, outside_click_quit=True)


def btn_restore_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Przywróć 1 w.\"", text=wyjustuj("Kliknij przycisk \"Przywróć 1 w.\", aby wykonać jeden krok w stronę przywrócenia własności kopca binarnego.", 50),
                                 func=refresh_heap, outside_click_quit=True)


def btn_sort_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Sortuj\"", text=wyjustuj("Kliknij przycisk \"Sortuj\", aby rozpocząć usuwanie minimalnych wartości elementów kopca binarnego i umieszczanie ich w tablicy sortowanych węzłów.", 50),
                                 func=refresh_heap, outside_click_quit=True)


text_add_heap = thorpy.make_text("Wprowadź listę wartości: ", 12, (0, 0, 0))
btn_add = thorpy.make_button("Dodaj", func=btn_add_func)
btn_add.set_size((100, 32))
btn_add_info = thorpy.make_button("?", func=btn_add_info_func)
btn_add_info.set_size((32, 32))

btn_add_random = thorpy.make_button("Dodaj losowo", func=btn_add_random_func)
btn_add_random.set_size((100, 32))
btn_add_random_info = thorpy.make_button("?", func=btn_add_random_info_func)
btn_add_random_info.set_size((32, 32))

btn_del_min = thorpy.make_button("Usuń min.", func=btn_del_func)
btn_del_min.set_size((100, 32))
btn_del_min_info = thorpy.make_button("?", func=btn_del_min_info_func)
btn_del_min_info.set_size((32, 32))

btn_add_heap = thorpy.make_button("Dodaj kopiec", func=btn_insert_heap_func)
btn_add_heap.set_size((100, 32))
btn_add_heap_info = thorpy.make_button("?", func=btn_add_heap_info_func)
btn_add_heap_info.set_size((32, 32))

btn_random_heap = thorpy.make_button("Losowy kopiec", func=btn_random_func)
btn_random_heap.set_size((100, 32))
btn_random_heap_info = thorpy.make_button("?", func=btn_random_info_func)
btn_random_heap_info.set_size((32, 32))

btn_restore = thorpy.make_button("Przywróć 1 w.", func=btn_restore_func)
btn_restore.set_size((100, 32))
btn_restore_info = thorpy.make_button("?", func=btn_restore_info_func)
btn_restore_info.set_size((32, 32))

btn_sort = thorpy.make_button("Sortuj", func=btn_sort_func)
btn_sort.set_size((100, 32))
btn_sort_info = thorpy.make_button("?", func=btn_sort_info_func)
btn_sort_info.set_size((32, 32))

btn_undo = thorpy.make_button("Cofnij", func=btn_undo_func)
btn_undo.set_size((100, 32))

box_add = thorpy.make_group([btn_add, btn_add_info], mode="h")
box_add.fit_children()
box_add_random = thorpy.make_group([btn_add_random, btn_add_random_info], mode="h")
box_add_random.fit_children()
box_del_min = thorpy.make_group([btn_del_min, btn_del_min_info], mode="h")
box_del_min.fit_children()
box_add_heap = thorpy.make_group([btn_add_heap, btn_add_heap_info], mode="h")
box_add_heap.fit_children()
box_range = thorpy.make_group([insert_min, insert_max], mode="h")
box_range.fit_children()
box_random_heap = thorpy.make_group([btn_random_heap, btn_random_heap_info], mode="h")
box_random_heap.fit_children()
box_restore = thorpy.make_group([btn_restore, btn_restore_info], mode="h")
box_restore.fit_children()
box_sort = thorpy.make_group([btn_sort, btn_sort_info], mode="h")
box_sort.fit_children()


# stos ######################################################################################
def btn_push_s_func():
    if insert_val_s.get_value().isdigit() and stack.currentSize < 11:
        stack.push(int(insert_val_s.get_value()))
    insert_val_s.set_value("")


def btn_push_random_s_func():
    if insert_min_s.get_value().isdigit() and insert_max_s.get_value().isdigit() and \
            int(insert_min_s.get_value()) < int(insert_max_s.get_value()):
        if stack.currentSize < 11:
            stack.push(random.randint(int(insert_min_s.get_value()), int(insert_max_s.get_value())))


def btn_pop_s_func():
    if stack.stackList:
        stack.pop()


def btn_random_s_func():
    if insert_size_s.get_value().isdigit() and insert_min_s.get_value().isdigit() and \
            insert_max_s.get_value().isdigit() and int(insert_min_s.get_value()) < int(insert_max_s.get_value()):
        size = int(insert_size_s.get_value())
        if insert_min_s.get_value() != "" and insert_max_s.get_value() != "" and insert_size_s.get_value() != "":
            blit_menu(1)
            if size > 11:
                size = 11
            for _ in range(0, size):
                stack.push(random.randint(int(insert_min_s.get_value()), int(insert_max_s.get_value())))


def btn_sort_s_func():
    if stack.stackList:
        stack.sortStack()


def refresh_stack():
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    box_stack.blit()
    stack.displayUpdate()


def btn_push_info_s_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj\"", text=wyjustuj("Wprowadź wartość w powyższe pole, a następnie kliknij przycisk \"Dodaj\", a zostanie dodany nowy element o zadanej wartości na szczyt stosu.", 55),
                                 func=refresh_stack, outside_click_quit=True)


def btn_push_random_s_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj losowo\"", text=wyjustuj("Kliknij przycisk \"Dodaj losowo\", a zostanie dodany nowy element o losowej wartości z przedziału min. - maks. na szczyt stosu.", 55),
                                 func=refresh_stack, outside_click_quit=True)


def btn_pop_s_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Zdejmij\"", text=wyjustuj("Kliknij przycisk \"Zdejmij\", aby zdjąć element ze szczytu stosu.", 50),
                                 func=refresh_stack, outside_click_quit=True)


def btn_random_s_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Losowy stos\"", text=wyjustuj("Kliknij przycisk \"Losowy stos\", aby stworzyć stos o losowych wartościach z przedziału min. - maks. i wysokości zadanej w polu \"Rozmiar\".", 50),
                                 func=refresh_stack, outside_click_quit=True)


def btn_sort_s_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Sortuj\"", text=wyjustuj("Kliknij przycisk \"Sortuj\", aby rozpocząć sortowanie wartości umieszczonych na stosie za pomocą zmiennej tymczasowej oraz dodatkowego stosu.", 55),
                                 func=refresh_stack, outside_click_quit=True)


btn_push_s = thorpy.make_button("Dodaj", func=btn_push_s_func)
btn_push_s.set_size((100, 32))
btn_push_s_info = thorpy.make_button("?", func=btn_push_info_s_func)
btn_push_s_info.set_size((32, 32))

btn_push_random_s = thorpy.make_button("Dodaj losowo", func=btn_push_random_s_func)
btn_push_random_s.set_size((100, 32))
btn_push_random_s_info = thorpy.make_button("?", func=btn_push_random_s_info_func)
btn_push_random_s_info.set_size((32, 32))

btn_pop_s = thorpy.make_button("Zdejmij", func=btn_pop_s_func)
btn_pop_s.set_size((100, 32))
btn_pop_s_info = thorpy.make_button("?", func=btn_pop_s_info_func)
btn_pop_s_info.set_size((32, 32))

btn_random_stack_s = thorpy.make_button("Losowy stos", func=btn_random_s_func)
btn_random_stack_s.set_size((100, 32))
btn_random_stack_s_info = thorpy.make_button("?", func=btn_random_s_info_func)
btn_random_stack_s_info.set_size((32, 32))

btn_sort_s = thorpy.make_button("Sortuj", func=btn_sort_s_func)
btn_sort_s.set_size((100, 32))
btn_sort_s_info = thorpy.make_button("?", func=btn_sort_s_info_func)
btn_sort_s_info.set_size((32, 32))

box_push_s = thorpy.make_group([btn_push_s, btn_push_s_info], mode="h")
box_push_s.fit_children()
box_push_random_s = thorpy.make_group([btn_push_random_s, btn_push_random_s_info], mode="h")
box_push_random_s.fit_children()
box_pop_s = thorpy.make_group([btn_pop_s, btn_pop_s_info], mode="h")
box_pop_s.fit_children()
box_range_s = thorpy.make_group([insert_min_s, insert_max_s], mode="h")
box_random_stack_s = thorpy.make_group([btn_random_stack_s, btn_random_stack_s_info], mode="h")
box_random_stack_s.fit_children()
box_sort_s = thorpy.make_group([btn_sort_s, btn_sort_s_info], mode="h")
box_sort_s.fit_children()


# kolejka #####################################################################################
def btn_push_q_func():
    if insert_val_q.get_value().isdigit() and queue.currentSize < 22:
        queue.push(int(insert_val_q.get_value()))
    insert_val_q.set_value("")


def btn_push_random_q_func():
    if insert_min_q.get_value().isdigit() and insert_max_q.get_value().isdigit() and \
            int(insert_min_q.get_value()) < int(insert_max_q.get_value()):
        if queue.currentSize < 14:
            queue.push(random.randint(int(insert_min_q.get_value()), int(insert_max_q.get_value())))


def btn_pop_q_func():
    if queue.queueList:
        queue.pop()


def btn_random_q_func():
    if insert_size_q.get_value().isdigit() and insert_min_q.get_value().isdigit() and \
            insert_max_q.get_value().isdigit() and int(insert_min_q.get_value()) < int(insert_max_q.get_value()):
        size = int(insert_size_q.get_value())
        if insert_min_q.get_value() != "" and insert_max_q.get_value() != "" and insert_size_q.get_value() != "":
            blit_menu(0)
            if size > 14:
                size = 14
            for _ in range(0, size):
                queue.push(random.randint(int(insert_min_q.get_value()), int(insert_max_q.get_value())))


def refresh_queue():
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    box_queue.blit()
    queue.displayUpdate()


def btn_push_info_q_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj\"", text=wyjustuj("Wprowadź wartość w powyższe pole, a następnie kliknij przycisk \"Dodaj\", a zostanie dodany nowy element o zadanej wartości na koniec kolejki.", 50),
                                 func=refresh_queue, outside_click_quit=True)


def btn_push_random_q_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj losowo\"", text=wyjustuj("Kliknij przycisk \"Dodaj losowo\", a zostanie dodany nowy element o losowej wartości z przedziału min. - maks. na koniec kolejki.", 50),
                                 func=refresh_queue, outside_click_quit=True)


def btn_pop_q_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Zdejmij\"", text=wyjustuj("Kliknij przycisk \"Zdejmij\", aby zdjąć pierwszy element z kolejki.", 50),
                                 func=refresh_queue, outside_click_quit=True)


def btn_random_q_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Losowa kolejka\"", text=wyjustuj("Kliknij przycisk \"Losowa kolejka\", aby stworzyć kolejkę o losowych wartościach z przedziału min. - maks. i wielkości zadanej w polu \"Rozmiar\".", 50),
                                 func=refresh_queue, outside_click_quit=True)


btn_push_q = thorpy.make_button("Dodaj", func=btn_push_q_func)
btn_push_q.set_size((110, 32))
btn_push_q_info = thorpy.make_button("?", func=btn_push_info_q_func)
btn_push_q_info.set_size((32, 32))

btn_push_random_q = thorpy.make_button("Dodaj losowo", func=btn_push_random_q_func)
btn_push_random_q.set_size((110, 32))
btn_push_random_q_info = thorpy.make_button("?", func=btn_push_random_q_info_func)
btn_push_random_q_info.set_size((32, 32))

btn_pop_q = thorpy.make_button("Zdejmij", func=btn_pop_q_func)
btn_pop_q.set_size((110, 32))
btn_pop_q_info = thorpy.make_button("?", func=btn_pop_q_info_func)
btn_pop_q_info.set_size((32, 32))

btn_random_queue_q = thorpy.make_button("Losowa kolejka", func=btn_random_q_func)
btn_random_queue_q.set_size((110, 32))
btn_random_queue_q_info = thorpy.make_button("?", func=btn_random_q_info_func)
btn_random_queue_q_info.set_size((32, 32))

box_push_q = thorpy.make_group([btn_push_q, btn_push_q_info], mode="h")
box_push_q.fit_children()
box_push_random_q = thorpy.make_group([btn_push_random_q, btn_push_random_q_info], mode="h")
box_push_random_q.fit_children()
box_pop_q = thorpy.make_group([btn_pop_q, btn_pop_q_info], mode="h")
box_pop_q.fit_children()
box_range_q = thorpy.make_group([insert_min_q, insert_max_q], mode="h")
box_random_stack_q = thorpy.make_group([btn_random_queue_q, btn_random_queue_q_info], mode="h")
box_random_stack_q.fit_children()


# lista #######################################################################################
def refresh_list():
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    box_list.blit()
    li.displayUpdate()


def btn_add_l_func():
    if insert_val_l.get_value().isdigit():
        if li.size() < 11:
            li.add(insert_val_l.get_value())
    insert_val_l.set_value('')


def btn_add_random_l_func():
    if insert_min_l.get_value().isdigit() and insert_max_l.get_value().isdigit() and \
            int(insert_min_l.get_value()) < int(insert_max_l.get_value()):
        if li.size() < 11:
            li.add(random.randint(int(insert_min_l.get_value()), int(insert_max_l.get_value())))


def btn_random_l_func():
    if insert_size_l.get_value().isdigit() and insert_min_l.get_value().isdigit() and \
            insert_max_l.get_value().isdigit() and int(insert_min_l.get_value()) < int(insert_max_l.get_value()):
        size = int(insert_size_l.get_value())
        if insert_min_l.get_value() != "" and insert_max_l.get_value() != "" and insert_size_l.get_value() != "":
            blit_menu(2)
            if size > 11:
                size = 11
            for _ in range(0, size):
                li.add(random.randint(int(insert_min_l.get_value()), int(insert_max_l.get_value())))


def btn_remove_l_func():
    if insert_remove_l.get_value().isdigit():
        if li.size() > 0:
            li.remove(insert_remove_l.get_value())
            insert_remove_l.set_value('')


def btn_push_info_l_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj\"", text=wyjustuj("Wprowadź wartość w powyższe pole, a następnie kliknij przycisk \"Dodaj\", a zostanie dodany nowy element o zadanej wartości do listy jednokierunkowej.", 50),
                                 func=refresh_list, outside_click_quit=True)


def btn_push_random_l_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Dodaj losowo\"", text=wyjustuj("Kliknij przycisk \"Dodaj losowo\", a zostanie dodany nowy element o losowej wartości z przedziału min. - maks. do listy jednokierunkowej.", 50),
                                 func=refresh_list, outside_click_quit=True)


def btn_random_l_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Losowa lista\"", text=wyjustuj("Kliknij przycisk \"Losowa lista\", aby stworzyć listę jednokierunkową o losowych wartościach z przedziału min. - maks. i wielkości zadanej w polu \"Rozmiar\".", 50),
                                 func=refresh_list, outside_click_quit=True)


def btn_remove_l_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Usuń wartość\"", text=wyjustuj("Wprowadź wartość w powyższe pole, a następnie kliknij przycisk \"Usuń wartość\", aby usunąć element o podanej wartości z listy jednokierunkowej.", 50),
                                 func=refresh_list, outside_click_quit=True)


btn_add_l = thorpy.make_button("Dodaj", func=btn_add_l_func)
btn_add_l.set_size((110, 32))
btn_add_l_info = thorpy.make_button("?", func=btn_push_info_l_func)
btn_add_l_info.set_size((32, 32))

btn_add_random_l = thorpy.make_button("Dodaj losowo", func=btn_add_random_l_func)
btn_add_random_l.set_size((110, 32))
btn_add_random_l_info = thorpy.make_button("?", func=btn_push_random_l_info_func)
btn_add_random_l_info.set_size((32, 32))

btn_random_l = thorpy.make_button("Losowa lista", func=btn_random_l_func)
btn_random_l.set_size((110, 32))
btn_random_l_info = thorpy.make_button("?", func=btn_random_l_info_func)
btn_random_l_info.set_size((32, 32))

btn_remove_l = thorpy.make_button("Usuń wartość", func=btn_remove_l_func)
btn_remove_l.set_size((110, 32))
btn_remove_l_info = thorpy.make_button("?", func=btn_remove_l_info_func)
btn_remove_l_info.set_size((32, 32))

box_push_l = thorpy.make_group([btn_add_l, btn_add_l_info], mode="h")
box_push_l.fit_children()
box_push_random_l = thorpy.make_group([btn_add_random_l, btn_add_random_l_info], mode="h")
box_push_random_l.fit_children()
box_random_l = thorpy.make_group([btn_random_l, btn_random_l_info], mode="h")
box_random_l.fit_children()
box_range_l = thorpy.make_group([insert_min_l, insert_max_l], mode="h")
box_remove_l = thorpy.make_group([btn_remove_l, btn_remove_l_info], mode="h")
box_remove_l.fit_children()


# ONP #########################################################################################
def refresh_onp():
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    box_onp.blit()
    toggs_box.blit()
    if onp.whole_eq:
        onp.displayUpdate(onp.whole_eq)
    else:
        screen.blit(onp.txt_stos, (onp.oStack_pos[0] - 20, onp.oStack_pos[1] + 70))
        screen.blit(onp.txt_oper, (onp.oStack_pos[0] - 70, onp.oStack_pos[1] + 100))


def btn_show_eq_func():
    if insert_eq.get_value():
        onp.show_equation(insert_eq.get_value())
        insert_eq.set_value('')
    # else:
    #     f = open(filepath, "r")
    #     lines = f.readlines()
    #     r = random.randint(0, 19)
    #     onp.show_equation(lines[r][:len(lines[r]) - 1])


def btn_show_onp_func():
    onp.show_onp()


def btn_show_eq_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Pokaż wyrażenie\"", text=wyjustuj("Wprowadź poprawne wyrażenie arytmetyczne w powyższe pole tekstowe, a następnie kliknij przycisk \"Pokaż wyrażenie\", a zostanie wyświetlone ono na środku okna aplikacji.", 50),
                                 func=refresh_onp, outside_click_quit=True)


def btn_show_onp_info_func():
    thorpy.launch_blocking_alert(title="Informacja o przycisku \"Oblicz ONP\"", text=wyjustuj("Kliknij przycisk \"Oblicz ONP\", a rozpocznie się algorytm zapisujący wyrażenie w postaci odwrotnej notacji polskiej.", 50),
                                 func=refresh_onp, outside_click_quit=True)


btn_show_eq = thorpy.make_button("Pokaż wyrażenie", func=btn_show_eq_func)
btn_show_eq.set_size((110, 32))
btn_show_eq_info = thorpy.make_button("?", func=btn_show_eq_info_func)
btn_show_eq_info.set_size((32, 32))

btn_show_onp = thorpy.make_button("Oblicz ONP", func=btn_show_onp_func)
btn_show_onp.set_size((110, 32))
btn_show_onp_info = thorpy.make_button("?", func=btn_show_onp_info_func)
btn_show_onp_info.set_size((32, 32))

box_show_eq = thorpy.make_group([btn_show_eq, btn_show_eq_info], mode="h")
box_show_eq.fit_children()
box_show_onp = thorpy.make_group([btn_show_onp, btn_show_onp_info], mode="h")
box_show_onp.fit_children()

toggs = [
    thorpy.Togglable("a + b * c"),
    thorpy.Togglable("m * g * h"), thorpy.Togglable("m * c  ^ 2"), thorpy.Togglable("k * x ^ 2 / 2"),
    thorpy.Togglable("1 / x + 1 / y"), thorpy.Togglable("n * x ^ (n - 1)"), thorpy.Togglable("(a + b) * (a - b)"),
    thorpy.Togglable("1 / 2 * m * v ^ 2"), thorpy.Togglable("z + y * x ^ 2 - w"),
    thorpy.Togglable("k * Q * q / (r ^ 2)"), thorpy.Togglable("k / m * (t - a) ^ j"),
    thorpy.Togglable("W + ( m * v ^ 2 / 2)"), thorpy.Togglable("(G * M * m) / (r ^ 2)"),
    thorpy.Togglable("v * t + a * t ^ 2 / 2"), thorpy.Togglable("K * (1 + p / 100) ^ n"),
    thorpy.Togglable("a ^ 2 - 2 * a * b + b ^ 2"), thorpy.Togglable("(x - a) ^ 2 + (y - b) ^ 2"),
    thorpy.Togglable("p - (v + t * k) ^ 2 / (c ^ j - p)"), thorpy.Togglable("j - (h * t ^ (t + p)) / j * (p - a)"),
    thorpy.Togglable("v / n ^ (m + j) - (t + y) * (a - v ^ g)"),
    thorpy.Togglable("a ^ 3 - 3 * a ^ 2 * b + 3 * a * b ^ 2 - b ^ 3")]


for e in toggs:
    e.set_size((300, 32))

box_toggs1 = thorpy.make_group([toggs[0], toggs[3], toggs[6], toggs[9], toggs[12], toggs[15], toggs[18]], mode="v")
box_toggs1.fit_children()
box_toggs2 = thorpy.make_group([toggs[1], toggs[4], toggs[7], toggs[10], toggs[13], toggs[16], toggs[19]], mode="v")
box_toggs2.fit_children()
box_toggs3 = thorpy.make_group([toggs[2], toggs[5], toggs[8], toggs[11], toggs[14], toggs[17], toggs[20]], mode="v")
box_toggs3.fit_children()

box_toggs_all = thorpy.make_group([box_toggs1, box_toggs2, box_toggs3], mode="h")


def toggs_func(**x):
    for j in range(len(toggs)):
        if j is not x['text'] and toggs[j].current_state_key == 1:
            toggs[j].active = True
            toggs[j]._force_unpress()
            toggs[j]._hovered = False
            toggs[j]._unhover()
    toggs[x['text']].current_state_key = 1
    onp.show_equation(toggs[x['text']].get_text())


for i in range(len(toggs)):
    toggs[i].user_func = toggs_func
    toggs[i].user_params = {'text': i}
###############################################################################################


def buttons_set_active(a):
    btn_add.set_active(a)
    btn_add_info.set_active(a)
    btn_add_random.set_active(a)
    btn_add_random_info.set_active(a)
    btn_del_min.set_active(a)
    btn_del_min_info.set_active(a)
    btn_add_heap.set_active(a)
    btn_add_heap_info.set_active(a)
    btn_random_heap.set_active(a)
    btn_random_heap_info.set_active(a)
    btn_restore.set_active(a)
    btn_restore_info.set_active(a)
    btn_sort.set_active(a)
    btn_sort_info.set_active(a)
    btn_undo.set_active(a)

    btn_push_s.set_active(a)
    btn_push_s_info.set_active(a)
    btn_push_random_s.set_active(a)
    btn_push_random_s_info.set_active(a)
    btn_pop_s.set_active(a)
    btn_pop_s_info.set_active(a)
    btn_random_stack_s.set_active(a)
    btn_random_stack_s_info.set_active(a)
    btn_sort_s.set_active(a)
    btn_sort_s_info.set_active(a)

    btn_push_q.set_active(a)
    btn_push_q_info.set_active(a)
    btn_push_random_q.set_active(a)
    btn_push_random_q_info.set_active(a)
    btn_pop_q.set_active(a)
    btn_pop_q_info.set_active(a)
    btn_random_queue_q.set_active(a)
    btn_random_queue_q_info.set_active(a)

    btn_add_l.set_active(a)
    btn_add_l_info.set_active(a)
    btn_add_random_l.set_active(a)
    btn_add_random_l_info.set_active(a)
    btn_random_l.set_active(a)
    btn_random_l_info.set_active(a)
    btn_remove_l.set_active(a)
    btn_remove_l_info.set_active(a)

    btn_show_eq.set_active(a)
    btn_show_eq_info.set_active(a)
    btn_show_onp.set_active(a)
    btn_show_onp_info.set_active(a)

    for j in range(len(toggs) - 1):
        toggs[j].set_active(a)

    buttons[0].set_active(a)
    buttons[1].set_active(a)
    buttons[2].set_active(a)
    buttons[3].set_active(a)
    buttons[4].set_active(a)


box_binary_heap = thorpy.Box([insert_val, box_add, box_add_random, box_del_min, text_add_heap, insert_heap,
                              box_add_heap, box_range, insert_size, box_random_heap, speed_text, speed_slider,
                              box_restore, restore_checker, box_sort, btn_undo])
box_stack = thorpy.Box([insert_val_s, box_push_s, box_push_random_s, box_pop_s, box_range_s, insert_size_s,
                        box_random_stack_s, speed_text_s, speed_slider_s, box_sort_s])
box_queue = thorpy.Box([insert_val_q, box_push_q, box_push_random_q, box_pop_q, box_range_q, insert_size_q,
                        box_random_stack_q])
box_list = thorpy.Box([insert_val_l, box_push_l, box_push_random_l, box_range_l, insert_size_l, box_random_l,
                       insert_remove_l, box_remove_l])
box_onp = thorpy.Box([insert_eq_text, insert_eq, box_show_eq, box_show_onp, speed_text_onp, speed_slider_onp])


def blit_menu(struct):
    for togg in toggs:
        if togg.current_state_key == 1:
            togg.active = True
            togg._force_unpress()
            togg._hovered = False
            togg._unhover()
            break

    if struct == 5:
        thorpy.launch_blocking_alert(title="Informacja o aplikacji", text="Praca inżynierska na kierunku Informatyka,\n"
                                                                          "WEiI PRz, Luty 2021 r.\n"
                                                                          "Aplikacja ilustrująca działanie dynamicznych\n"
                                                                          "struktur danych.\n"
                                                                          "Wykonał: Bartosz Wikiera.",
                                     func=refresh, outside_click_quit=True)
        buttons[5].active = True
        buttons[5]._force_unpress()
        buttons[5]._hovered = False
        buttons[5]._unhover()
        return
    global menu, heap, stack, queue, li, onp
    heap.nodeList = []
    heap.heapList = []
    stack.nodeList = []
    stack.stackList = []
    li.head = None
    onp.oStack = []
    onp.nodeList = []
    onp.output = []
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    if struct == 0:
        menu = thorpy.Menu([select_struct_box, box_queue])
        queue = Queue(screen, img_list, menu, buttons_set_active)
    if struct == 1:
        menu = thorpy.Menu([select_struct_box, box_stack])
        stack = Stack(screen, img_list, menu, speed_slider_s, buttons_set_active)
    if struct == 2:
        menu = thorpy.Menu([select_struct_box, box_list])
        li = List(screen, img_list, menu, buttons_set_active)
    if struct == 3:
        menu = thorpy.Menu([select_struct_box, box_binary_heap])
        heap = BinHeap(screen, speed_slider, img_list, menu, buttons_set_active, restore_checker)
    if struct == 4:
        menu = thorpy.Menu([select_struct_box, box_onp, toggs_box])
        onp = ONP(screen, menu, buttons_set_active, speed_slider_onp)
    if struct == 9:
        menu = thorpy.Menu([select_struct_box])
    menu.blit_and_update()
    pygame.display.update()


buttons = [thorpy.Togglable("Kolejka FIFO"), thorpy.Togglable("Stos"), thorpy.Togglable("Lista jednokierunkowa"),
           thorpy.Togglable("Kopiec binarny"), thorpy.Togglable("ONP"), thorpy.Togglable("Informacje")]
for i in range(len(buttons)):
    buttons[i].set_size(((len(buttons[i].get_text()) * 8 + 20), 32))

buttons_poll_group = thorpy.make_group(elements=buttons, mode="h")


def refresh():
    global prev
    screen.fill((0, 0, 0))
    select_struct_box.blit()
    if prev == 3:
        box_binary_heap.blit()
        if heap.heapList:
            heap.displayUpdate()
    elif prev == 1:
        box_stack.blit()
        if stack.stackList:
            stack.displayUpdate()
    elif prev == 0:
        box_queue.blit()
        if queue.queueList:
            queue.displayUpdate()
    elif prev == 2:
        box_list.blit()
        if li.head is not None:
            li.displayUpdate()
    elif prev == 4:
        box_onp.blit()
        toggs_box.blit()
        if onp.nodeList:
            onp.displayUpdate(onp.save_eq)
    pygame.display.update()


select_struct_box = thorpy.Box(elements=[buttons_poll_group])
select_struct_box.fit_children()
select_struct_box.set_topleft((0, 0))

select_struct_box.blit()

box_binary_heap.fit_children()
box_binary_heap.set_topleft((0, select_struct_box.get_rect().bottomright[1]))
box_stack.fit_children()
box_stack.set_topleft((0, select_struct_box.get_rect().bottomright[1]))
box_queue.fit_children()
box_queue.set_topleft((0, select_struct_box.get_rect().bottomright[1]))
box_list.fit_children()
box_list.set_topleft((0, select_struct_box.get_rect().bottomright[1]))
box_onp.fit_children()
box_onp.set_topleft((0, select_struct_box.get_rect().bottomright[1]))

toggs_box = thorpy.Box(elements=[box_toggs_all])
toggs_box.fit_children()
toggs_box.set_topleft(box_onp.get_rect().topright)

menu = thorpy.Menu([select_struct_box])
heap = BinHeap(screen, speed_slider, img_list, menu, buttons_set_active, restore_checker)
stack = Stack(screen, img_list, menu, speed_slider_s, buttons_set_active)
queue = Queue(screen, img_list, menu, buttons_set_active)
li = List(screen, img_list, menu, buttons_set_active)
onp = ONP(screen, menu, buttons_set_active, speed_slider_onp)


def select_struct(**x):
    global prev
    for j in range(len(buttons)):
        if j is not x['nr'] and buttons[j].current_state_key == 1:
            buttons[j].active = True
            buttons[j]._force_unpress()
            buttons[j]._hovered = False
            buttons[j]._unhover()
            prev = j
    buttons[x['nr']].current_state_key = 1
    blit_menu(x['nr'])


for i in range(len(buttons)):
    buttons[i].user_func = select_struct
    buttons[i].user_params = {'nr': i}


for element in menu.get_population():
    element.surface = screen

blit_menu(9)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.react(event)
