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
        self.params_widgets = []

        # Fill ui
        self.wavelet_select.addItems(sorted(wavelets_dic.keys()))
        self.wavelet = wavelets_dic[str(self.wavelet_select.currentText())]()
        self._conf_ui()

        # Create and insert plot
        self.plot = pg.PlotWidget(self, title=' ')
        self.plot.getPlotItem().plot()

        grid = QtGui.QGridLayout()
        self.plot_frame.setLayout(grid)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.plot)

        # Connect signals and slots
        self.wavelet_select.currentIndexChanged[str].connect(self._wavelet)
        self.wavelet_points.valueChanged.connect(self._points)
        self.scale_spinbox.valueChanged.connect(self._scale)
        self.scale_slider.valueChanged.connect(self._scale)

        self.plot_nf()

    @QtCore.pyqtSlot(str)
    def _wavelet(self, value):
        value = str(value)
        self.wavelet = wavelets_dic[value](
            self.wavelet_points.value(),
            self.scale_slider.value()
        )
        self._conf_ui()
        self.plot_nf()

    def _conf_ui(self):
        # Delete old widgets
        for element in self.params_widgets:
            self.ui.param_box.layout().removeWidget(element)
            element.deleteLater()
        self.params_widgets[:] = []

        # Create new widgets
        for v, p in self.wavelet.params.iteritems():
            label = QtGui.QLabel('{}:'.format(v))
            spinbox = QtGui.QDoubleSpinBox()
            spinbox.setMinimum(p['min'])
            spinbox.setMaximum(p['max'])
            spinbox.setValue(p['def'])
            spinbox.setDecimals(1)
            spinbox.setSingleStep(0.1)

            slider = QtGui.QSlider()
            slider.setOrientation(QtCore.Qt.Horizontal)
            slider.setMinimum(p['min'] * self.spin_slide_factor)
            slider.setMaximum(p['max'] * self.spin_slide_factor)
            slider.setValue(p['def'] * self.spin_slide_factor)

            # Store for easier removal
            self.params_widgets.append(label)
            self.params_widgets.append(spinbox)
            self.params_widgets.append(slider)

            # Place widgets ot teh layout
            self.ui.param_box.layout().addWidget(label)
            self.ui.param_box.layout().addWidget(spinbox)
            self.ui.param_box.layout().addWidget(slider)

    @QtCore.pyqtSlot(int)
    def _points(self, value):
        self.wavelet.set_points(value)
        self.plot_nf()

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
        self.plot_nf()

    def plot_nf(self):
        self.plot.listDataItems()[0].setData(self.wavelet.vector)