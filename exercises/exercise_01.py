class Inhabitant(object):

    def greet(self, inhabitant):
        print "Hello there {}! I'm a {}".format(str(inhabitant), str(self))

    # Basically the visit dispatch function
    def interact(self, inhabitant):
        error_output = "Bruh this method doesn't exist for the base class."
        raise NotImplementedError(error_output)

    def get_weapon(self, inhabitant):
        error_output = "Bruh this method doesn't exist for the base class."
        raise NotImplementedError(error_output)

    def __str__(self):
        return self.__class__.__name__


# Engineer
class Dwarf(Inhabitant):

    def interact(self, inhabitant):
        if isinstance(inhabitant, Inhabitant):
            inhabitant.interact_dwarf(self)
        else:
            error_output = ("unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def interact_dwarf(self, inhabitant):
        self.greet(inhabitant)

    def interact_elf(self, inhabitant):
        self.greet(inhabitant)

    def interact_troll(self, inhabitant):
        self.greet(inhabitant)


# Marketers
class Elf(Inhabitant):

    def interact(self, inhabitant):
        if isinstance(inhabitant, Inhabitant):
            inhabitant.interact_elf(self)
        else:
            error_output = ("unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def interact_dwarf(self, inhabitant):
        self.greet(inhabitant)

    def interact_elf(self, inhabitant):
        self.greet(inhabitant)

    def interact_troll(self, inhabitant):
        self.greet(inhabitant)


# Managers
class Troll(Inhabitant):

    def interact(self, inhabitant):
        if isinstance(inhabitant, Inhabitant):
            inhabitant.interact_troll(self)
        else:
            error_output = ("unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def interact_dwarf(self, inhabitant):
        self.greet(inhabitant)

    def interact_elf(self, inhabitant):
        self.greet(inhabitant)

    def interact_troll(self, inhabitant):
        self.greet(inhabitant)


class Project():

    def __init__(self):
        pass

    def meeting(self):
        pass

    def battle(self):
        pass

    def perform_interactions(self):
        dwarf = Dwarf()
        elf = Elf()
        troll = Troll()

        dwarf.interact(elf)
        dwarf.interact(troll)
        print "--------"
        elf.interact(dwarf)
        elf.interact(troll)
        print "--------"
        troll.interact(elf)
        troll.interact(dwarf)

project = Project()
project.perform_interactions()
