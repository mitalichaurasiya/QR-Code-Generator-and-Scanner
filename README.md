# QR-Code-Generator-and-Scanner

This project can do both task:

* Generate a QR Code
* Scan a QR Code
  
QR CODE GENERATOR

* QR Code is a 2-D matrix code created by Japanese Corporation Denso Wave in 1994.
* QR stands for Quick Response.
* QR Code is needed because it allows the user to access the information instantly.

PRINCIPLE OF OPERATION
* The captured image is segmented in order to reduce searching space and extract the regions of interest.
* Afterwards a horizontal and vertical scans are performed to localize preliminary QR Code patterns, followed by Principle Component Analysis (PCA) Method which allows removing false positives.
* Thereafter, the remaining patterns are assembled according to a constraint so as to localize the corresponding QR Codes.
* The incorporation of PCA decreases notably the processing time and increases QR Code recognition accuracy (96%).
* QR code allows 30% of the code structure to take damage without affecting its readability on scanners.

MODULES USED

* qrcode - It is used for generating qr code images.
* pillow - It contains all the basic image processing functionalities like image resizing, rotation and transformation.

QR CODE SCANNER

* Here, we have built our own scanner also.
* Alongwith building the qr code, an individual can scan it also.

MODULES USED IN SCANNER

* CV2 - It is used to solve computer vision problems.
* pyzbar - Decode function is imported from pyzbar which we will used to detect and decode the QR Code.
