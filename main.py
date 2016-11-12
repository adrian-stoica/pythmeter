import machine
import network
import socket
import dht
import os
from time import sleep

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('SSID', 'PASSWORD')

d = dht.DHT11(machine.Pin(5))

def http_get(url):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 80)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break

while True:
	try:
		if sta_if.isconnected() is False:
			sta_if.connect()
			sleep(5)
		d.measure()
		http_get('http://YOURURL/post.php?temperature=%s&humidity=%s&key=123456' %(d.temperature(), d.humidity()))
		sleep(300)
	except() as error:
		if KeyboardInterrupt:
			break
		else:
			if os.stat('error.log')[6] > 200000:
				os.remove('error.log')
			strerror=str(error)
			f=open('error.log', 'a')
			f.write(strerror+'\n')
			f.close()
			pass

