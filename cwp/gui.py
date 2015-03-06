__author__ = 'mFoxRU'

from PyQt4 import QtCore, QtGui, uic
import pyqtgraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

from wavelets import wavelets_dic


class GuiApp(QtGui.QMainWindow):
    spin_slide_factor = 10


    def __init__(self):
        # Init
        super(GuiApp, self).__init__()
        self.ui = uic.loadUi('mainwindow.ui', self)

        # Fill ui
        self.wavelet_select.addItems(sorted(wavelets_dic.keys()))

        # Select wavelet
        self.wavelet = wavelets_dic[str(self.wavelet_select.currentText())]()

        # Create and insert plot
        self.plot = pg.PlotWidget(self, title=' ')
        self.plot.getPlotItem().plot()

        grid = QtGui.QGridLayout()
        self.plot_frame.setLayout(grid)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.plot)

        # Connect signals and slots
        self.wavelet_points.valueChanged.connect(self._points)
        self.scale_spinbox.valueChanged.connect(self._scale)
        self.scale_slider.valueChanged.connect(self._scale)

        self.plot_nf()


    @QtCore.pyqtSlot(int)
    def _points(self, value):
        self.wavelet.set_points(value)

    @QtCore.pyqtSlot(int)
    @QtCore.pyqtSlot(float)
    def _scale(self, value):
        # It's not a best solution, but it simplifies code
        if isinstance(value, int):  # It was Slider
            value = float(value)/self.spin_slide_factor
            self.scale_spinbox.setValue(value)
        else:   # It was Spinbox
            self.scale_slider.setValue(value*self.spin_slide_factor)

        self.wavelet.set_scale(value)

    def plot_nf(self):
        self.plot.listDataItems()[0].setData(self.wavelet.vector)