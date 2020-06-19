import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget


class MapWindow(QWidget):
    def __init__(self, lat = 26.8206, lon = 30.8025, zoom = 6):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        

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


import socket               # Import socket module



if __name__ == '__main__':
	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12345                # Reserve a port for your service.

	s.connect((host, port))
	count = s.recv(1024)
	print(int(count))
	data = []
	for _ in range(0, int(count), 1):
		data.append(s.recv(8))
	print(data[0])
	print(data[1])
	s.close()

	app = QApplication(sys.argv)
	widget = MapWindow()
	sys.exit(app.exec_())
