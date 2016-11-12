import machine
import network
import socket
import dht
import os
from time import sleep

#Define privacy variable
ssid=''
wifikey=''
posturl=''#needs to be without http://
d = dht.DHT11(machine.Pin(5)) #set the input pin for DHT11 sensor

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, wifikey)

def err_log(log)
        if os.stat('error.log')[6] > 200000:
        os.remove('error.log')
        strerror=str(log)
        f=open('error.log', 'a')
        f.write(strerror+'\n')
        f.close()


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
		http_get('http://%s/post.php?temperature=%s&humidity=%s&key=123456' %(posturl, d.temperature(), d.humidity()))
		sleep(300)
	except() as error:
		if KeyboardInterrupt:
			break
		else:
			err_log(error)
			pass
