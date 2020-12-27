import os
import time
import PySimpleGUI as sg
import math
import random


def get_random_color():
    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())


def hanoiController():
    num = int(input())
    obs = Observer()
    model = HanoiModelNonRecursive(num, obs)
    view = HanoiViewPySimpleGuy(model)
    obs.subscribe(view.display)
    obs.dispatch()
    model.solve()
    input()


class Observer:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def dispatch(self):
        for handler in self.observers:
            handler()


class HanoiModelBase:
    def __init__(self, num, obs):
        self.num = num
        self.arena = list(range(num)), [], []
        self.obs = obs

    def move_piece(self, current, dest):
        self.arena[dest].append(self.arena[current][-1])
        self.arena[current].pop()
        self.obs.dispatch()

    def not_solved(self):
        return not (len(self.arena[0]) == 0 and len(self.arena[1]) == 0)


class HanoiModelRecursive(HanoiModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moves = [
            (0, 2, 0)
        ]  # list of tuple of current and dest and index of the element

    def solve(self):

        while self.not_solved():
            if self.moves:
                last_move = self.moves[-1]
                current, dest, index = last_move
                if self.is_valid_move(current, dest, index):
                    self.moves.pop()
                    self.move_piece(current, dest)
                elif self.arena[current][index] == self.arena[current][-1]:
                    dic_from_dest = [
                        i
                        for i, e in enumerate(self.arena[dest])
                        if e > self.arena[current][index]
                    ][0]
                    self.moves.append(
                        (dest, self.get_new_dest(current, dest), dic_from_dest)
                    )
                else:
                    new_dest = self.get_new_dest(current, dest)
                    self.moves.append((current, new_dest, index + 1))
            else:
                current, dest, index = last_move
                self.moves.append((self.get_new_dest(current, dest), 2, 0))

    def get_new_dest(self, current, dest):
        return next(iter(({0, 1, 2} - {current, dest})))

    def is_valid_move(self, current, dest, index):
        return self.arena[current][index] == self.arena[current][-1] and (
            not self.arena[dest] or self.arena[dest][-1] < self.arena[current][index]
        )


class HanoiModelNonRecursive(HanoiModelBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.step = 1 if self.num % 2 == 0 else 2

    def solve(self):
        i = 0

        while self.not_solved():
            top_discs = sorted(
                [
                    (pile[-1], i) if pile else (-1, i)
                    for i, pile in enumerate(self.arena)
                ],
                reverse=True,
            )
            if i % 2 == 0:
                min_disc_poz = top_discs[0][1]
                self.move_piece(min_disc_poz, (min_disc_poz + self.step) % 3)
            else:
                second_min_disc_poz = top_discs[1][1]
                biggest_disc_poz = top_discs[2][1]
                self.move_piece(second_min_disc_poz, biggest_disc_poz)

            i += 1


class HanoiViewBase:
    def __init__(self, model):
        self.model = model


class HanoiViewPySimpleGuy(HanoiViewBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width, self.height = 1800, 900
        self.BAR_HEIGHT = 10
        self.MAX_LENGTH = self.width // 4
        self.V_DISTANCE = 10

        layout = [
            [
                sg.Graph(
                    canvas_size=(self.width, self.height),
                    graph_bottom_left=(0, 0),
                    graph_top_right=(self.width, self.height),
                    key="graph",
                )
            ]
        ]

        self.window = sg.Window("Hanoi", layout)
        self.window.Finalize()

        self.graph = self.window.Element("graph")
        self.piles = {}
        num = self.model.num

        for disc in range(num):
            rect_id = self.graph.DrawRectangle(
                (0, 0),
                (int(self.MAX_LENGTH * (num - disc) / num), self.BAR_HEIGHT),
                fill_color=get_random_color(),
            )
            self.piles[disc] = rect_id

    def display(self):
        num = self.model.num
        for i, pile in enumerate(self.model.arena):
            for j, disc in enumerate(pile):
                center_delta = (
                    self.MAX_LENGTH - int(self.MAX_LENGTH * (num - disc) / num)
                ) // 2
                self.graph.RelocateFigure(
                    self.piles[disc],
                    (self.MAX_LENGTH * i) + center_delta,
                    self.V_DISTANCE * 2 * (j + 1),
                )
        self.window.Refresh()
        time.sleep(0.3)


class HanoiViewConsole(HanoiViewBase):
    def display(self):
        os.system("clear")

        arena = [
            ["|"] * (self.model.num - len(pile)) + list(reversed(pile))
            for pile in self.model.arena
        ]
        for e1, e2, e3 in zip(*arena):
            print(f"{e1} {e2} {e3}")
        time.sleep(0.3)


hanoiController()
