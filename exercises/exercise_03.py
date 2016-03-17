# MultipleDispatching/PaperScissorsRock.py
# Demonstration of multiple dispatching.
from __future__ import generators
import random


# An enumeration type:
class Outcome:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

Outcome.WIN = Outcome("win")
Outcome.LOSE = Outcome("lose")
Outcome.DRAW = Outcome("draw")


class Item(object):

    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def visit(self, object_to_visit):
        return self.accept_dispatch(self, object_to_visit)

    def accept_dispatch(self, object1, object2):
        object1_class_name = object1.__class__.__name__
        object2_class_name = object2.__class__.__name__
        print "starting in: {}".format(object1_class_name)
        print "visiting to: {}".format(object2_class_name)
        return getattr(object1, "visit{}".format(object2_class_name))(object1)


class Paper(Item):

    def visitPaper(self, item_to_visit):
        return Outcome.DRAW

    def visitScissors(self, item_to_visit):
        return Outcome.LOSE

    def visitRock(self, item_to_visit):
        return Outcome.WIN


class Scissors(Item):

    def visitPaper(self, item_to_visit):
        return Outcome.WIN

    def visitScissors(self, item_to_visit):
        return Outcome.DRAW

    def visitRock(self, item_to_visit):
        return Outcome.LOSE


class Rock(Item):

    def visitPaper(self, item_to_visit):
        return Outcome.LOSE

    def visitScissors(self, item_to_visit):
        return Outcome.WIN

    def visitRock(self, item_to_visit):
        return Outcome.DRAW


def match(item1, item2):
    print("%s <--> %s : %s" % (item1, item2, item1.compete(item2)))


# Generate the items:
def itemPairGen(n):
    # Create a list of instances of all Items:
    Items = Item.__subclasses__()
    for i in range(n):
        first_item = random.choice(Items)
        second_item = random.choice(Items)
        yield (first_item, second_item)


# print "Rock vs Paper: {}".format(accept_dispatch(Rock(), Paper()))
rock = Rock()
paper = Paper()
scissor = Scissors()

# outcome = rock.visit(rock)
# print outcome
# outcome = paper.visit(rock)
# print outcome
# outcome = scissor.visit(rock)
# print outcome

outcome = rock.visit(paper)
print outcome
outcome = paper.visit(paper)
print outcome
outcome = scissor.visit(paper)
print outcome

# visit_table = {}
# for start_subclass in Item.__subclasses__():
#     visit_table[start_subclass] = {}
#     for end_subclass in Item.__subclasses__():
#         visit_table[start_subclass][end_subclass] = getattr(start_subclass,
#                                                                  "visit{}".format(end_subclass.__name__))(start_subclass(), start_subclass())

# for key, value in visit_table.iteritems():
#     print "-" * 20
#     print key
#     print "-" * 10
#     for k, v in value.iteritems():
#         print k

# for first_item, second_item in itemPairGen(10):
#     outcome = visit_table[first_item][second_item]
#     print "-" * 20
#     print "Item 1: {}".format(first_item.__name__)
#     print "Item 2: {}".format(second_item.__name__)
#     print outcome
