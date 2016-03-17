import random


class Weapon(object):

    def __init__(self, weapon_type):
        self.weapon_type = weapon_type.lower()

    def __str__(self, weapon_type):
        return "{}.{}".format(self.__class__.__name__, self.weapon_type)

    def __eq__(self, other_weapon):
        if isinstance(other_weapon, self.__class__):
            return self.weapon_type == other_weapon.weapon_type
        else:
            error_output = ("Unanticipated value passed to weapon for"
                            " comparison. This  can only take Weapon type.")
            raise AttributeError(error_output)


class Outcome(object):

    def __init__(self, outcome_type):
        self.outcome_type = outcome_type.lower()

    def __str__(self):
        return "{}.{}".format(self.__class__.__name__, self.outcome_type)

    def __eq__(self, other_outcome):
        return self.outcome_type == other_outcome.outcome_type

Outcome.WIN = Outcome("Win")
Outcome.LOSE = Outcome("Lose")
Outcome.DRAW = Outcome("Draw")

Weapon.JARGON = Weapon("Jargon")
Weapon.PLAY = Weapon("Play")
Weapon.INVENTFEATURE = Weapon("InventFeature")
Weapon.SELLIMAGINARYPRODUCT = Weapon("SellImaginaryProduct")
Weapon.EDICT = Weapon("Edict")
Weapon.SCHEDULE = Weapon("Schedule")

# This is not scalable...
WeaponOutcomes = {
    # JARGON
    # Dwarf
    (Weapon.JARGON, Weapon.JARGON): Outcome.DRAW,
    (Weapon.JARGON, Weapon.PLAY): Outcome.DRAW,
    # Elf
    (Weapon.JARGON, Weapon.INVENTFEATURE): Outcome.WIN,
    (Weapon.JARGON, Weapon.SELLIMAGINARYPRODUCT): Outcome.LOSE,
    # Troll
    (Weapon.JARGON, Weapon.EDICT): Outcome.WIN,
    (Weapon.JARGON, Weapon.SCHEDULE): Outcome.LOSE,

    # PLAY
    # Dwarf
    (Weapon.PLAY, Weapon.JARGON): Outcome.DRAW,
    (Weapon.PLAY, Weapon.PLAY): Outcome.DRAW,
    # Elf
    (Weapon.PLAY, Weapon.INVENTFEATURE): Outcome.WIN,
    (Weapon.PLAY, Weapon.SELLIMAGINARYPRODUCT): Outcome.LOSE,
    # Troll
    (Weapon.PLAY, Weapon.EDICT): Outcome.WIN,
    (Weapon.PLAY, Weapon.SCHEDULE): Outcome.LOSE,

    # INVENTINGFEATURE
    # Dwarf
    (Weapon.INVENTFEATURE, Weapon.JARGON): Outcome.WIN,
    (Weapon.INVENTFEATURE, Weapon.PLAY): Outcome.LOSE,
    # Elf
    (Weapon.INVENTFEATURE, Weapon.INVENTFEATURE): Outcome.DRAW,
    (Weapon.INVENTFEATURE, Weapon.SELLIMAGINARYPRODUCT): Outcome.DRAW,
    # Troll
    (Weapon.INVENTFEATURE, Weapon.EDICT): Outcome.WIN,
    (Weapon.INVENTFEATURE, Weapon.SCHEDULE): Outcome.LOSE,

    # SELLIMAGINARYPRODUCT
    # Dwarf
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.JARGON): Outcome.WIN,
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.PLAY): Outcome.LOSE,
    # Elf
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.INVENTFEATURE): Outcome.DRAW,
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.SELLIMAGINARYPRODUCT): Outcome.DRAW,
    # Troll
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.EDICT): Outcome.WIN,
    (Weapon.SELLIMAGINARYPRODUCT, Weapon.SCHEDULE): Outcome.LOSE,

    # EDICT
    # Dwarf
    (Weapon.EDICT, Weapon.JARGON): Outcome.WIN,
    (Weapon.EDICT, Weapon.PLAY): Outcome.LOSE,
    # Elf
    (Weapon.EDICT, Weapon.INVENTFEATURE): Outcome.WIN,
    (Weapon.EDICT, Weapon.SELLIMAGINARYPRODUCT): Outcome.LOSE,
    # Troll
    (Weapon.EDICT, Weapon.EDICT): Outcome.DRAW,
    (Weapon.EDICT, Weapon.SCHEDULE): Outcome.DRAW,

    # SCHEDULE
    # Dwarf
    (Weapon.SCHEDULE, Weapon.JARGON): Outcome.WIN,
    (Weapon.SCHEDULE, Weapon.PLAY): Outcome.LOSE,
    # Elf
    (Weapon.SCHEDULE, Weapon.INVENTFEATURE): Outcome.WIN,
    (Weapon.SCHEDULE, Weapon.SELLIMAGINARYPRODUCT): Outcome.LOSE,
    # Troll
    (Weapon.SCHEDULE, Weapon.EDICT): Outcome.DRAW,
    (Weapon.SCHEDULE, Weapon.SCHEDULE): Outcome.DRAW,
}


class Inhabitant(object):

    def greet(self, inhabitant):
        print "Hello there {}! I'm a {}".format(inhabitant.get_race(), self.get_race())

    # Basically the visit dispatch function
    def interact(self, inhabitant):
        error_output = "Bruh this method doesn't exist for the base class."
        raise NotImplementedError(error_output)

    def get_weapon(self):
        error_output = "Bruh this method doesn't exist for the base class."
        raise NotImplementedError(error_output)

    def get_race(self):
        return self.__class__.__name__


# Engineer
class Dwarf(Inhabitant):

    def interact(self, inhabitant):
        if isinstance(inhabitant, Inhabitant):
            inhabitant.interact_dwarf(self)
        else:
            error_output = ("Unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def get_weapon(self):
        # 0 or 1
        weapon_choice = random.randint(0, 1)
        if weapon_choice == 0:
            return Weapon.JARGON
        else:
            return Weapon.PLAY

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
            error_output = ("Unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def get_weapon(self):
        # 0 or 1
        weapon_choice = random.randint(0, 1)
        if weapon_choice == 0:
            return Weapon.INVENTFEATURE
        else:
            return Weapon.SELLIMAGINARYPRODUCT

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
            error_output = ("Unanticipated value passed as an inhabitant. This"
                            " method only expects the objects that are the"
                            " inhabitant class type.")
            raise AttributeError(error_output)

    def get_weapon(self):
        # 0 or 1
        weapon_choice = random.randint(0, 1)
        if weapon_choice == 0:
            return Weapon.EDICT
        else:
            return Weapon.SCHEDULE

    def interact_dwarf(self, inhabitant):
        self.greet(inhabitant)

    def interact_elf(self, inhabitant):
        self.greet(inhabitant)

    def interact_troll(self, inhabitant):
        self.greet(inhabitant)


class Project():

    def __init__(self):
        pass

    # This isn't a good algorithm....
    def meeting(self):
        dwarves = [Dwarf()
                   for count
                   in xrange(10)]

        elves = [Elf()
                 for count
                 in xrange(10)]

        trolls = [Troll()
                  for count
                  in xrange(10)]

        teams = [dwarves, elves, trolls]

        team_has_won = False
        while team_has_won == False:
            # Before Change
            first_team_selected = random.choice(teams)
            second_team_selected = random.choice(teams)

            # Battle Logic
            if(len(first_team_selected) > 0 and
                    len(second_team_selected) > 0):
                first_team_inhabitant = random.choice(first_team_selected)
                second_team_inhabitant = random.choice(second_team_selected)

                outcome = self.battle(first_team_inhabitant,
                                      second_team_inhabitant)
                # print outcome

                # team_one_selected_member won
                if outcome == Outcome.WIN:
                    first_team_selected.remove(first_team_inhabitant)
                    # print "Removed team one"
                # team_two_selected_member won
                elif outcome == Outcome.LOSE:
                    second_team_selected.remove(second_team_inhabitant)
                    # print "Removed team two"

                # do nothing
                else:
                    # Yo dawg I heard it was a draw, that's aight
                    # try again next time
                    # print "Draw"
                    pass

            # Exit condition - A team has won when the other teams are defeated
            empty_count = 0
            for team in teams:
                empty_count = (empty_count + 1
                               if len(team) == 0
                               else empty_count)

            if empty_count >= (len(teams) - 1):
                team_has_won = True

        winners = filter(lambda team: len(team) > 0, teams)
        losers = [team
                  for team
                  in teams
                  if len(team) == 0]

        print "#" * 30
        print "# Teams"
        print "#" * 30
        print "Dwarves: {}".format(dwarves)
        print "Elves: {}".format(elves)
        print "Trolls: {}".format(trolls)

        print
        print "#" * 30
        print "# Results"
        print "#" * 30
        print "Winning Team: {}".format(winners)
        print "Losing Team(s):  {}".format(losers)

    def battle(self, inhabitant_one, inhabitant_two):
        weapon_tuple = (inhabitant_one.get_weapon(),
                        inhabitant_two.get_weapon())
        outcome = WeaponOutcomes[weapon_tuple]
        return outcome

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
# project.perform_interactions()
project.meeting()
