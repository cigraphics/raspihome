raspihome
=========

raspberry pi smarthome

Scopul proiectului: monitorizarea de la distanta a unei incaperi sau a unei zone unde accesul este dificil sau periculos

Exemple de utilizare:

1) uz casnic/rezidential
- monitorizarea unor parametri de confort sau siguranta prin interfata web (inclusiv smartphone)
- folosirea unor senzori uzuali (temperatura, umiditate, presiune, gaze, lumiozitate, proximitate etc)
- controlul unor parametri de confort prin actionarea de relee (incalzire pardoseala, pompe recirculare apa, circuite prize/lumini etc)
- folosirea unui webcam cu detectie de miscare si trimiterea de imagini pe o adresa email predefinita

2) uz profesional
- centralizarea si agregarea unor parametri proveniti de la senzori distribuiti (ex. mini-statii meteo dispersate)
- statii mobile de culegere de date (video/audio, colectii de diversi senzori) folosind pe o plaforma cu roti motoare 
(line follower) controlate prin arduino si interfata pyfirmata cu raspberry pi
- streaming video/audio

Componentele proiectului:
- raspberry pi cu senzori i2c sau spi
- webcam usb
- stick usb wifi (pentru platforma mobila)
- controler arduino uno cu drivere pentru 4 motoare si (optional) senzori analogici suplimentari
