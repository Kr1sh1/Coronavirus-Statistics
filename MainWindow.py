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

        axisX = QtCharts.QDateTimeAxis()
        axisX.setFormat("MM-yyyy")

        chart_view.chart().setAxisX(axisX, line_series)
        self.setCentralWidget(chart_view)
