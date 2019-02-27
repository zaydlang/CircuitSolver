class Solver:
    def __init__(self):
        self.graph = {}
        self.state = "menu"
        
    def display_menu(self):
        print("Electric Circuit Solver")
        print("(0) Set Node Connections")
        print("(1) Evaluate Circuit")
        print("(2) Quit")

    def display_graph(self):
        if len(self.graph) > 0:
            print("Current circuit: ")
            for key in self.graph:
                print(key + " -> " + ','.join(e for e in self.graph[key]))
        
    def run(self):
        while self.state != "quit":
            print("state : " + self.state)
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
                        self.state = "quit"

            if self.state == "connections":
                self.edit_graph()

    def edit_graph(self):
        while self.state != "menu":
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

            if self.state == "add":
                connection = input("Give me a connection to add (Format: A -> [B, C])\n")
                connection.replace(" ", "")
                head = connection[0]
                tail = connection[connection.find("[")+1:connection.find("]")].split(",")
                self.graph[head] = tail
            elif self.state == "remove":
                remove = input("Which connection to remove? (Format: A, B)\n").split(", ")
                self.graph[remove[0]].pop(remove[1])

solver = Solver()
solver.run()

