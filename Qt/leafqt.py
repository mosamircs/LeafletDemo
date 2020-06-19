import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget


class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        lat = 26.8206
        lon = 30.8025
        zoom = 6

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([lat, lon], zoom)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)


        self.marker = L.marker([lat, lon])
        self.marker.bindPopup("Lat : " + str(lat) + " ,Lon : " + str(lon))
        self.map.addLayer(self.marker)

        latlngs = [[26.8206, 30.8025], [27.8206, 31.8025], [28.8206, 32.8025]]
        polyline = L.polyline(latlngs).addTo(self.map);

        # L.control.scale().addTo(self.map);
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())
