# PowerSecurityRaspberry
## _This code is about our computer vison code on raspberry_

It's better to have anaconda installed on your computer
to start this project very easly 

# Features
### This code use english as principal language for speaking and detection
- Tracking person using google mobilenet-ssd
- Using haarcascade by Opencv for face recognition
- Using SpeechRecognition and play sound for speaking with our client
- Secure our home entry and save all logs about people who enter to our home
# Installation

```sh
conda init <yourbash> # if you have linux
```
```sh
conda create -n "PowerSecurity" python=3.10 # We re creating our Virtual environment, better to have python 3.10 because it s work with our play sound module
```
```sh
    conda activate PowerSecurity
```
```sh
    python -m pip install tensorflow==2.8.0 gtts SpeechRecognition playsound==1.2.2 opencv-python
    #Please, it is necessary to respect versions
```
 ```sh
    conda install PyAudio
 ```
 
```
    cd PowerSecurityRaspberry
    python main.py
```
# Contributors
 - Ziad Bougrine (https://github.com/DerZiad)
- Asmae Mahjoubi (https://github.com/asmae1m)
 - Ayman Hemmouda (https://github.com/telos-matter)
 - Mohamed Hafidi (https://github.com/mohamedhafidi33)

