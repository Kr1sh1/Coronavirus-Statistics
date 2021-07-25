import operator
import math

from PySide6.QtGui import QColor
from StatisticsRetriever import StatisticsRetriever
from PySide6 import QtWidgets, QtCore, QtCharts

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        data_retriever = StatisticsRetriever()
        data_retriever.refresh_data()
        data = data_retriever.retrieve_data()

        line_series = QtCharts.QLineSeries()
        date_time = QtCore.QDateTime()

        for date, value in data.items():
            date = map(int, date.split("-"))
            date_time.setDate(QtCore.QDate(*date))
            line_series.append(date_time.toMSecsSinceEpoch(), value)

        chart_view = QtCharts.QChartView()
        chart_view.chart().addSeries(line_series)
        chart_view.chart().setTheme(chart_view.chart().ChartThemeDark)

        max_daily_cases = max(data.items(), key=operator.itemgetter(1))[1]
        tick_count = 10

        axis_y = QtCharts.QValueAxis()

        # tick interval code from here: https://stackoverflow.com/a/326746
        unroundedTickSize = max_daily_cases/(tick_count-1);
        x = math.ceil(math.log10(unroundedTickSize)-1);
        pow10x = math.pow(10, x);
        roundedTickRange = math.ceil(unroundedTickSize / pow10x) * pow10x;
        
        axis_y.setTickInterval(roundedTickRange)
        axis_y.setTickType(QtCharts.QValueAxis.TicksDynamic)
        axis_y.setGridLineVisible(True)
        axis_y.setGridLineColor(QColor(255, 0, 0))
        
        axis_x = QtCharts.QDateTimeAxis()
        axis_x.setFormat("MM-yyyy")

        chart_view.chart().setAxisX(axis_x, line_series)
        chart_view.chart().setAxisY(axis_y, line_series)
        self.setCentralWidget(chart_view)
