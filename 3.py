import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        for _ in range(2):
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        t.penup()
        t.goto(self.dxpos, self.dypos)

    def cleardisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        t.pencolor("white")
        for _ in range(2):
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.penup()
        t.pencolor("black")


class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.pencolor("black")
        t.forward(self.pthick / 2)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick / 2)

    def pushdisk(self, disk):
        # Position the disk above the previous disk in the stack
        if self.stack:
            top_disk = self.stack[-1]
            disk.newpos(self.pxpos - disk.dwidth / 2, top_disk.dypos + top_disk.dheight)
        else:
            disk.newpos(self.pxpos - disk.dwidth / 2, self.pypos)
        disk.cleardisk()
        disk.showdisk()
        
        self.stack.append(disk)

    def popdisk(self):
        if len(self.stack) == 0:
            return None
        pickdisk = self.stack.pop()
        pickdisk.cleardisk()
        pickdisk.newpos(pickdisk.dxpos, 200 + pickdisk.dypos)
        pickdisk.showdisk()
        pickdisk.cleardisk()
        return pickdisk


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        # Create and push disks to the start pole
        for i in range(n):
            disk = Disk("d" + str(i), 0, i * 30, 20, (n - 1 - i) * 30)
            self.startp.pushdisk(disk)

    def move_disk(self, start, destination):
        disk = start.popdisk()
        if disk:
            destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)


# Main execution
h = Hanoi()
h.solve()
t.done()
