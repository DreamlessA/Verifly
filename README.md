# Verifly

This program is designed to run on Rasberry Pi zero (or any other similar board) to provide automated 2FA ID verification service. The verification process includes three parts: OpenCert based certificate verification, Azure cloud service based face recognition and ZFM-20 series Fingerprint scanner (which can be easily found on Adafruit or other sites, other ZFM fingerprint sensor may also be used as alternative).

#### To start using this program your first need to prepare the following hardware:
  - A Rasberry Pi or similar board that can meet the same software and hardware requirement
  - A screen with SPI protocol
  - An audio system (that may include dac, amp and speaker ) with I2S protocol
  - a ZFM series fingerprint sensor that goes through UART protocol
  - a Pi Camera

#### You also need to prepare the following software:
##### Python3 and Libraries:
  - PIL (python image library)
  - opencv
  - pyzbar
  - picamera
##### Azure cloud service with face API:
  - replace the KEY and ENDPOINT field in the image_process file with your credentials
##### Follow the steps on https://docs.opencerts.io/ to create your blockchain based cerifitcate as your ID:
  - You should first record your fingerprint data locally as test.fingerprint file:
    - Type "python3 fingerprint_reader.py" in bash 
  - Then prepare a photo of jpg or png format
  - And turn the fingerpirnt data and photo into base64 format
    - Type "base64_convertor.py FILENAME" in bash
  - And add them to the certificate following the instruction on the opencert site and deploy the certificate:
    - The tool to generate certificate from json can be found at https://github.com/Open-Attestation/open-attestation-cli
    - The tool to deploy the certificate can be found at https://admin.opencerts.io/deploy/
##### In the end, put you certificate into a web server so that it can be acessed with a link. Turn that that URL to a QR Code and you are all good to go!  

&nbsp;

##### Note:
- The program has been tested on Rasberry Pi zero and Rasberry Pi 4 and was fully functioning.
- To autorun it as a service at boot: 
  - Edit the WorkingDirectory in verification.service file and then add it to the system as a service
- To manually start it
  - Type "python3 verify.py to start the verification program" in bash