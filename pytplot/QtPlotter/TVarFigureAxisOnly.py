import pyqtgraph as pg
from .CustomAxis.NonLinearAxis import NonLinearAxis
from .CustomViewBox.CustomVB import CustomVB
import pytplot

class TVarFigureAxisOnly(pg.GraphicsLayout):
    def __init__(self, tvar_name):
        self.tvar_name=tvar_name
        
        #Sets up the layout of the Tplot Object
        pg.GraphicsLayout.__init__(self)
        self.layout.setHorizontalSpacing(50)
        self.layout.setContentsMargins(0,0,0,0)
        
        vb = CustomVB(enableMouse=False)
        yaxis = pg.AxisItem("left")
        yaxis.setLabel(pytplot.data_quants[self.tvar_name].yaxis_opt['axis_label'])
        yaxis.setWidth(100)
        yaxis.label.rotate(90)
        yaxis.label.translate(0, -40)
        xaxis = NonLinearAxis(orientation='bottom', data=pytplot.data_quants[self.tvar_name])
        self.plotwindow = self.addPlot(row=0, col=0, axisItems={'bottom': xaxis, 'left':yaxis}, viewBox=vb, colspan=1)
        self.plotwindow.buttonsHidden=True
        self.plotwindow.setMaximumHeight(20)
        
        #Set up the view box needed for the legends
        self.legendvb = pg.ViewBox(enableMouse=False)
        self.legendvb.setMaximumWidth(100)
        self.addItem(self.legendvb,0,1)