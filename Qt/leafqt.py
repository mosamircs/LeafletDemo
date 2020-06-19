import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget
import socket               


class MapWindow(QWidget):
    def __init__(self, planes):
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        

        self.map = L.map(self.mapWidget)
        self.map.setView([26.8022, 30.8025], 6)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)

        for plane in planes:
        	print(plane)
	        self.marker = L.marker([plane[0], plane[1]])
	        self.marker.bindPopup("Lat : " + str(plane[0]) + " ,Lon : " + str(plane[1]))
	        self.map.addLayer(self.marker)

        latlngs = [[26.8022, 30.8888], [27.8206, 31.8025], [28.8206, 32.8025]]
        polyline = L.polyline(latlngs).addTo(self.map);

        self.show()





if __name__ == '__main__':
	s = socket.socket()         
	host = socket.gethostname() 
	port = 12345                

	s.connect((host, port))
	count = int(s.recv(4))
	print(int(count))
	data = []
	for _ in range(0, int(count), 1):
		data.append(s.recv(7)) # Receive 7 bytes
	s.close()

	planes = []
	for i in range(0, count-1, 2):
		planeData = [float(data[i]), float(data[i+1])]
		planes.append(planeData)
	print(planes)

	app = QApplication(sys.argv)
	widget = MapWindow(planes)
	sys.exit(app.exec_())
