
# CamFF

This script implements the vulnerabilities of outdoor surveillance cameras using Sophia web server to implement management, viewing and configuration methods.

**CamFF** - exploit for cheap Chinise cameras that have /tdkcgi (Sophia linux server).

This script use [theoreticalstructures ](https://www.theoreticalstructures.io/2022/05/27/the-unbearable-lightness-of-web-vulnerabilities/) exploit (use [web archive](http://web.archive.org/web/20220610073810/https://www.theoreticalstructures.io/2022/05/27/the-unbearable-lightness-of-web-vulnerabilities/)) and tested by Falcon cams

![wayo a3lD1](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAKOV5s72dKtUx3trc7MIfBZqyPJe4Obq0rcLPxxxkCA&s)

DDOS script can turn off http and rtsp server on camera for ~30 sec
just change LIST variable :0

# Usage

Change LIST Targets in camFF.py file and run by python (>= 3.6)


    dev/cc22> python camFF.py
   
   To exploit this vulnerability on Falcon Eye hardware, use files from the falcon folder
