import re

DEBUG = True

# TODO: make sure there are no loops in the graph lol

class Connection:
    def __init__(self, tail):
        self.tail = tail
        self.resistance = 0

class Solver:
    # Initialize the circuit and state
    def __init__(self):
        self.graph = {}
        self.state = "menu"

    # Display the main menu
    def display_menu(self):
        print("Electric Circuit Solver")
        print("(0) Set Node Connections")
        print("(1) Evaluate Circuit")
        print("(1) Set Resistors")
        print("(3) Quit")

    # Display the current circuit
    def display_graph(self):
        if len(self.graph) > 0:
            print("Current circuit: ")
            for key in self.graph:
                print(key + " -> " + ', '.join(e.tail for e in self.graph[key]))

    # Display connections
    
    # Run the menu
    def run(self):
        while self.state != "quit":
            self.debug("state : " + self.state)
                
            # Main menu
            if self.state == "menu":
                self.display_menu()
                choice = int(input())
                if choice < 0 or choice > 2:
                    print("Choice out of bounds!")
                else:
                    if choice == 0:
                        self.state = "connections"
                    elif choice == 1:
                        self.state = "evaluate"
                    elif choice == 2:
                        self.state == "resistor"
                    elif choice == 3:
                        self.state = "quit"

            # Editting Circuit
            if self.state == "connections":
                self.edit_graph()

    # Editting Circuit
    def edit_graph(self):
        while self.state != "menu":
            self.debug("state : " + self.state)
            
            self.display_graph()
            print("(0) Add Connection")
            print("(1) Remove Connection")
            print("(2) Menu")
            choice = int(input())
            
            if choice < 0 or choice > 2:
                print("Choice out of bounds!")
            else:
                if choice == 0:
                    self.state = "add"
                elif choice == 1:
                    self.state = "remove"
                elif choice == 2:
                    self.state = "menu"

            # Adding connection
            if self.state == "add":
                connection = input("Give me a connection to add (Format: A -> [B, C])\n").replace(' ', '')
                # Make sure input is valid
                head = re.findall("^[A-Z,a-z](?=-)", connection)
                tail = re.findall("(?<=[\[,, ])[A-Z,a-z]", connection)
                # If no matches (or too many)
                if (len(head) != 1 or len(tail) < 1):
                    print("Invalid input.")
                else:
                    self.debug("set " + str(head) + " to " + str(tail))
                    # Make sure the head is initialized
                    if head[0] not in self.graph:
                        self.graph[head[0]] = []
                    # No duplicates
                    self.graph[head[0]] = self.graph[head[0]] + list(Connection(connect) for connect in tail if connect not in self.graph[head[0]])
                    
            elif self.state == "remove":
                remove = input("Which connection to remove? (Format: A, B)\n").split(", ")
                self.debug("remove " + remove[1] + " from " + remove[0])
                try:
                    self.graph[remove[0]] = [x for x in self.graph[remove[0]] if x.tail != remove[1]]
                    if len(self.graph[remove[0]]) == 0:
                        self.graph.pop(remove[0], None)
                except:
                    print("Invalid input.")

    def edit_resistors(self):
        while self.state != "menu":
            self.debug("state : " + self.state)

            self.list(connections)
        
    # Prints a debug message
    def debug(self, message):
        if DEBUG:
            print("[DEBUG] " + message)
                      
solver = Solver()
solver.run()

