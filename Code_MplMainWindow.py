from MplMainWindow import *
from PyQt4.QtGui import *
import sys
import cv2
import numpy as np
from beam import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from frame_type import *
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

matplotlib.use('Agg')


class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, )

        self.img = np.ones((410, 640))
        self.img *= 255

        self.scene1 = QGraphicsScene(self)
        self.ui.mplCanvas.setScene(self.scene1)
        self.scene2 = QGraphicsScene(self)
        self.ui.mplCanvas2.setScene(self.scene2)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ax2 = self.figure2.add_axes([0.1, 0.1, 0.8, 0.8])

        # line, = self.ax2.plot()
        self.canvas2.print_figure('temp2.jpg')

        self.beamImg = cv2.imread('temp2.jpg')
        self.beamImg = cv2.resize(self.beamImg, (310, 280))
        self.QTBeamImg = np2q(self.beamImg)
        beammap2 = QtGui.QPixmap.fromImage(self.QTBeamImg)
        self.scene2.addPixmap(beammap2)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax1 = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])

        # line, = self.ax1.plot()
        self.canvas.print_figure('temp1.jpg')

        self.MainImg = cv2.imread('temp1.jpg')
        self.MainImg = cv2.resize(self.MainImg, (310, 280))
        self.QTMainImg1 = np2q(self.MainImg)
        mainmap1 = QtGui.QPixmap.fromImage(self.QTMainImg1)
        self.scene1.addPixmap(mainmap1)

        self.commandLine = ''
        # self.ui.textLeftBrowser.setText(self.commandLine)

        self.BeamList = []

        self.connect(self.ui.GenerateButtom, QtCore.SIGNAL('clicked()'), self.Generate)
        self.connect(self.ui.AddBeamButton, QtCore.SIGNAL('clicked()'), self.AddBeam)
        self.connect(self.ui.Solve, QtCore.SIGNAL('clicked()'), self.Solve)
        self.connect(self.ui.AddForce, QtCore.SIGNAL('clicked()'), self.AddForce)
        self.connect(self.ui.ShowButton, QtCore.SIGNAL('clicked()'), self.Show)

    def Generate(self):
        self.world = World(int(self.ui.WorldFreedomDegreeEdit.text()))
        self.commandLine += 'World created.\n'
        self.ui.textLeftBrowser.setText(self.commandLine)

    def AddBeam(self):
        ID = int(self.ui.IDEdit.text())
        StartX = float(self.ui.StartEditX.text())
        StartY = float(self.ui.StartEditY.text())
        EndX = float(self.ui.EndEditX.text())
        EndY = float(self.ui.EndEditY.text())
        EA = float(self.ui.EAEdit.text())
        EI = float(self.ui.EIEdit.text())
        lambdaa = []
        lambdaa.append(int(self.ui.L1.text()))
        lambdaa.append(int(self.ui.L2.text()))
        lambdaa.append(int(self.ui.L3.text()))
        lambdaa.append(int(self.ui.L4.text()))
        lambdaa.append(int(self.ui.L5.text()))
        lambdaa.append(int(self.ui.L6.text()))

        temp = beam(ID, [StartX, StartY], [EndX, EndY], EA, EI)
        temp.set_lambda(lambdaa)

        self.world.add_beam(temp)

        self.commandLine += 'Beam ' + str(ID) + ' added.\n'
        self.commandLine += str(temp.K_e) +'\n'
        self.ui.textLeftBrowser.setText(self.commandLine)

        line, = self.ax2.plot([StartX, EndX], [StartY, EndY], linewidth=5.0)
        self.canvas2.print_figure('temp2.jpg')

        self.beamImg = cv2.imread('temp2.jpg')
        self.beamImg = cv2.resize(self.beamImg, (321, 291))
        self.QTBeamImg = np2q(self.beamImg)
        beammap2 = QtGui.QPixmap.fromImage(self.QTBeamImg)
        self.scene2.addPixmap(beammap2)

    def AddForce(self):
        x = int(self.ui.BeamId.text())
        mode = self.ui.TypeEdit.text()
        self.world.beam_list[x].add_force(float(self.ui.ForceEdit.text()), float(self.ui.LocEdit.text()),mode)
        self.commandLine += 'Force Added\n'
        self.ui.textLeftBrowser.setText(self.commandLine)

    def Solve(self):
        self.commandLine += 'Solving\n'
        self.ui.textLeftBrowser.setText(self.commandLine)
        self.ans = self.world.solve()
        self.commandLine += 'Finished\n'
        self.commandLine += str(self.world.system_disp) + '\n'
        self.ui.textLeftBrowser.setText(self.commandLine)

    def Show(self):
        number = int(self.ui.ShowEdit.text())
        beam = self.world.beam_list[number]
        self.commandLine += 'Displacements:' + '\n'
        self.commandLine += str(beam.Displacement) + '\n'
        self.commandLine += 'Forces:' + '\n'
        self.commandLine += str(beam.Force) + '\n'
        self.ui.textLeftBrowser.setText(self.commandLine)

        cv2.line(self.img, (60, 200), (500, 200), (0, 0, 0), 3)

        cv2.putText(self.img, str(beam.Force[2, 0]), (50, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.putText(self.img, str(beam.Force[5, 0]), (510, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        if (beam.Force[2, 0] > 0):
            h1 = 100
        else:
            h1 = -100
        h2 = int(beam.Force[5, 0] / beam.Force[2, 0] * h1)



        cv2.line(self.img, (60, 200), (60, 200 + h1), (0, 0, 0), 1)
        cv2.line(self.img, (500, 200), (500, 200 + h2), (0, 0, 0), 1)
        cv2.line(self.img, (60, 200 + h1), (500, 200 + h2), (0, 0, 0), 1)
        self.img = cv2.resize(self.img, (280, 320))
        self.QTMainImg1 = np2q(self.img)
        mainmap1 = QtGui.QPixmap.fromImage(self.QTMainImg1)
        self.scene1.addPixmap(mainmap1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Myform()
    MainWindow.show()
    QtGui.QApplication.connect(app, QtCore.SIGNAL('lastWindowClosed()'), app.quit)
    sys.exit(app.exec_())
