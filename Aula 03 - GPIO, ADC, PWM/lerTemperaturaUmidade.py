import Adafruit_DHT as dht

sensor = dht.DHT22
pin = "P8_11"

umidade, temperatura = dht.read_retry(sensor,pin)

if umidade is not None and temperatura is not None:
	print("Temp.={0:0.1f}C Umidade={1:0.1f}%"
		.format(temperatura, umidade))
else:
	print("Erro na leitura, tente novamente")
