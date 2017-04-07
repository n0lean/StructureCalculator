import numpy as np
from matplotlib import pyplot as plt


class World():
    def __init__(self, freedom_degree):
        self.beam_list = []
        self.freedom_degree = freedom_degree
        self.system_matrix = np.matrix(np.zeros((freedom_degree, freedom_degree)))
        self.system_force = np.matrix(np.zeros((freedom_degree, 1)))
        self.system_disp = np.matrix(np.zeros((freedom_degree, 1)))

    def add_beam(self, beam):
        self.beam_list.append(beam)

    def solve(self):
        for beam in self.beam_list:
            lambdaa = beam.lambdaa
            x, y = 0, 0
            for i in lambdaa:
                y = 0
                for j in lambdaa:
                    if i * j != 0:
                        self.system_matrix[i - 1, j - 1] += beam.K[x, y]
                    y += 1
                if i != 0:
                    self.system_force[i - 1, 0] += beam.Force[x, 0]
                x += 1

        print(self.system_matrix)
        print(self.system_force)

        self.system_disp = np.linalg.inv(self.system_matrix) * self.system_force

        for i in self.beam_list:
            for j in range(6):
                if i.lambdaa[j] == 0:
                    continue
                else:
                    i.Displacement[j] = self.system_disp[i.lambdaa[j]-1]

        for i in self.beam_list:
            i.Force = i.K_e * i.T * i.Displacement

        return self.system_disp


class beam():
    def __init__(self, ID, start_point, end_point, EA, EI, mode='normal'):
        self.id = ID
        self.start_point = np.array(start_point, dtype=np.float32)
        self.end_point = np.array(end_point, dtype=np.float32)
        self.EA = np.float(EA)
        self.EI = np.float(EI)
        self.length = float(np.linalg.norm(self.start_point - self.end_point))
        self.mode = mode

        self.Force_list = []

        self.locked = np.zeros((6))

        self.lambdaa = np.zeros((6))

        self.K_e = np.matrix([[EA / self.length, 0, 0, -EA / self.length, 0, 0],
                              [0, 12. * EI / self.length ** 3, 6 * EI / self.length ** 2,
                               0,-12. * EI / self.length ** 3, 6 * EI / self.length ** 2],
                              [0, 6. * EI / self.length ** 2, 4 * EI / self.length,
                               0, -6. * EI / self.length ** 2,2 * EI / self.length],
                              [-EA / self.length, 0, 0, EA / self.length, 0, 0],
                              [0, -12. * EI / self.length ** 3, -6 * EI / self.length ** 2, 0,
                               12. * EI / self.length ** 3, -6 * EI / self.length ** 2],
                              [0, 6 * EI / self.length ** 2, 2 * EI / self.length, 0, -6. * EI / self.length ** 2,
                               4 * EI / self.length]])

        self.Force_e = np.matrix(np.zeros((6, 1)))
        self.Force = np.matrix(np.zeros((6, 1)))

        self.Displacement_e = np.matrix(np.zeros((6, 1)))
        self.Displacement = np.matrix(np.zeros((6, 1)))

        alpha = np.arcsin((end_point[1] - start_point[1]) / (
            (end_point[1] - start_point[1]) ** 2 + (end_point[0] - start_point[0]) ** 2) ** 0.5)
        self.t = np.matrix([[np.cos(alpha), np.sin(alpha), 0],
                            [-np.sin(alpha), np.cos(alpha), 0],
                            [0, 0, 1]], np.float32)
        temp1 = np.vstack((self.t, np.zeros((3, 3))))
        temp2 = np.vstack((np.zeros((3, 3)), self.t))
        self.T = np.hstack((temp1, temp2))

        self.freedom_degree = 6

        self.K = self.T.T * self.K_e * self.T

    def lock(self, loc, mode='lock'):
        if mode == 'lock':
            self.locked[loc] = 1
        else:
            self.locked[loc] = 0

    def set_seat(self, loc='left', type='hinge'):
        base = 0
        if loc == 'left':
            pass
        else:
            base += 3
        if type == 'hinge':
            self.lock(base, 'lock')
            self.lock(base + 1, 'lock')
            self.lock(base + 2, 'unlock')
            self.freedom_degree = - 2
        elif type == 'vertical_slide':
            self.lock(base, 'lock')
            self.lock(base + 1, 'unlock')
            self.lock(base + 2, 'lock')
            self.freedom_degree = - 2
        elif type == 'solid':
            self.lock(base, 'lock')
            self.lock(base + 1, 'lock')
            self.lock(base + 2, 'lock')
            self.freedom_degree = - 3
        elif type == 'free':
            for i in range(6):
                self.lock(i, 'unlock')
            self.freedom_degree = 6

    def add_force(self, num, loc, mode='single'):
        self.Force_list.append([num,loc,mode])

        a = loc
        num  = float(num)
        b = self.length - loc
        if mode == 'single':
            self.Force_e[0] += 0
            self.Force_e[1] += -num * b ** 2 / self.length ** 2 * (1 + 2 * a / self.length)
            self.Force_e[2] += -num * a * b ** 2 / self.length ** 2
            self.Force_e[3] += 0
            self.Force_e[4] += -num * a ** 2 / self.length ** 2 * (1 + 2 * b / self.length)
            self.Force_e[5] += -num * a ** 2 * b / self.length ** 2

        elif mode == 'free':
            self.Force_e[:] = 0

        elif mode == 'spread':
            self.Force_e[0] += 0
            self.Force_e[1] += -num * a * (1 - a ** 2 / self.length ** 2 + a ** 3 / 2 / self.length ** 3)
            self.Force_e[2] += -num * a ** 2 / 12 * (6 - 8 * a / self.length + 3 * a ** 2 / self.length ** 2)
            self.Force_e[3] += 0
            self.Force_e[4] += -num * a ** 3 / self.length ** 2 * (1 - a / 2 / self.length)
            self.Force_e[5] += -num * a ** 3 / 12 / self.length * (4 - 3 * a / self.length)

        elif mode == 'moment':
            self.Force_e[0] += 0
            self.Force_e[1] += 6 * num * a * b / self.length ** 3
            self.Force_e[2] += num * b / self.length * (3 * a / self.length - 1)
            self.Force_e[3] += 0
            self.Force_e[4] += -6 * num * a * b / self.length ** 3
            self.Force_e[5] += num * a / self.length * (3 * b / self.length - 1)

        self.Force = self.T.T * self.Force_e
        print('Force')
        print(self.Force)
    def set_lambda(self, status):
        self.lambdaa = status


if __name__ == '__main__':
    beam1 = beam(1, [0, 0], [0, 2], 1, 1)
    beam2 = beam(2, [0, 0], [4, 0], 1, 1)
    beam3 = beam(3, [4, 0], [4, 2], 1, 1)

    beam1.set_lambda([1, 2, 3, 0, 0, 0])
    beam2.set_lambda([1, 2, 3, 4, 5, 6])
    beam3.set_lambda([4, 5, 6, 0, 0, 0])

    beam2.add_force(1, beam1.length / 2)

    world = World(6)

    world.add_beam(beam1)
    world.add_beam(beam2)
    world.add_beam(beam3)

    world.solve()
    print(world.system_disp)
