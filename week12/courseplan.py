class CoursePlan:
    def __init__(self):
        self.graph = {}
        self.containsCycle = False

    def add_course(self,course):
        self.graph[course] = []

    def add_requisite(self,course1,course2):
        self.graph[course1].append(course2)

    def find(self):
        color = {}
        for node in self.graph:
            color[node] = 0
        order = []

        def dfs(course):
            # solmu on käsittelyssä (ja solmulla on kaaria) = sykli on löytynyt
            if color[course] == 1 and len(self.graph[course]) > 0:
                self.containsCycle = True
                return

            # solmu on käsitelty jo
            if color[course] == 2:
                return
            
            # if course not in order:
            #     order.append(course)
            
            # solmu on käsittelyssä nyt
            color[course] = 1

            # käydään läpi solmun naapurit
            for next in self.graph[course]:
                dfs(next)

            # naapurit käsitelty eli solmukin on käsitelty
            color[course] = 2
            order.append(course)

        # tehdään kaikille solmuille syvyyshaku
        for node in self.graph:
            if color[node] == 0:
                dfs(node)
            
        if self.containsCycle:
            order = None
        else:
            order.reverse()

        return order

if __name__ == "__main__":
    # c = CoursePlan()
    # c.add_course("Ohpe")
    # c.add_course("Ohja")
    # c.add_course("Tira")
    # c.add_course("Jym")
    # c.add_requisite("Ohpe","Ohja")
    # c.add_requisite("Ohja","Tira")
    # c.add_requisite("Jym","Tira")
    # print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    # c.add_requisite("Tira","Tira")
    # print(c.find()) # None


    # lista
    # apulista
    # apulista käännetään lopuksi -> topologinen järjestys
        # jos mahdollisia suoritustapoja on useita, mikä tahansa niistä hyväksytään

        # jos löytyy sykli, järjestystä ei ole olemassa

    c = CoursePlan()
    print(c.find()) # None
    c.add_course('course5')
    c.add_requisite('course5','course5')
    print(c.find()) # None
    c.add_course('course3')
    c.add_course('course4')
    c.add_requisite('course3','course4')
    print(c.find())

    # c = CoursePlan()
    # c.add_course('course3')
    # c.add_course('course1')
    # c.add_requisite('course3','course1')
    # print(c.find()) # e.g. ['course3', 'course1']
    # print(c.find()) # e.g. ['course3', 'course1']
    # c.add_course('course5')
    # c.add_requisite('course5','course3')
    # print(c.find()) # ???

    c = CoursePlan()
    c.add_course('course1')
    c.add_course('course2')
    c.add_requisite('course1','course2')
    c.add_course('course3')
    c.add_requisite('course1','course3')
    print(c.find())
    print(c.find())
    c.add_course('course4')
    c.add_course('course5')
    c.add_requisite('course4','course5')