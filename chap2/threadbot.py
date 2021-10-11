import threading
from attr import attrs,attrib
from queue import Queue
import sys

@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


kitchen = Cutlery(knives=100, forks=100)


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table())
        self.cutlery = Cutlery()
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare_table":
                kitchen.give(
                    to=self.cutlery,
                    knives=4,
                    forks=4
                )
            elif task == "clear_table":
                self.cutlery.give(
                    to=kitchen,
                    knives=4,
                    forks=4,
                )
            elif task == "shut_down":
                return

bots = [
    ThreadBot() for i in range(10)
]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put("prepare_table")
        bot.tasks.put("clear_table")

    bot.tasks.put("shut_down")

print("kitchen inventory before services : ", kitchen)

for bot in bots:
    bot.join()


print("kitchen inventory after services : ", kitchen)
