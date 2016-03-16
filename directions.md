# Relephant Links:

## Visitor Design Patter:
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Visitor.html

## Multiple Dispatching:
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/MultipleDispatching.html?highlight=PaperScissorsRock

# Execise Process
## Step 1:
- Create a business-modeling environment with three types of Inhabitant: 
    - Dwarf (for engineers), 
    - Elf (for marketers) 
    - Troll (for managers). 
- Now create a class called Project 
    - creates the different inhabitants 
    - causes them to interact() 
        - using multiple dispatching.

## Step 2:
- Modify the above example to make the interactions more detailed. 
- Each Inhabitant can randomly produce a Weapon using getWeapon() 
    - Dwarf 
        - Jargon
        - Play
    - Elf 
        - InventFeature
        - SellImaginaryProduct
    - Troll
        - Edict
        - Schedule
- You must decide which weapons “win” and “lose” in each interaction
    - As in PaperScissorsRock.py Add a battle() member function to Project
        - takes two Inhabitants and matches them against each other
    - Now create a meeting() member function for Project 
        - creates groups of Dwarf, Elf and Troll
        - battles the groups against each other until only members of one group are left standing. 
            - These are the “winners.”

## Step 3:
- Modify PaperScissorsRock.py to replace the double dispatching with a table lookup. 
- The easiest way to do this is to create a Map of Maps, with the key of each Map the class of each object. Then you can do the lookup by saying: ((Map)map.get(o1.getClass())).get(o2.getClass())
    - Notice how much easier it is to reconfigure the system.
    - When is it more appropriate to use this approach vs. hard-coding the dynamic dispatches?
    - Can you create a system that has the syntactic simplicity of use of the dynamic dispatch but uses a table lookup?