# led_strip

Here is an interface for controlling the WS2801 led strips with a raspberry pi. I modified some of the code from [audio-reactive-led-strip](https://github.com/scottlawsonbc/audio-reactive-led-strip) so that it would work with the WS2801 strips. You can control the leds via the webbrowser.

![Image1](https://i.imgur.com/77E0aAP.png)

I am using several other projects and have made modifications to those projects.

I am using Twitter [Bootstrap](https://getbootstrap.com/), [jQuery](https://jquery.com/), [audio-reactive-led-strip](https://github.com/scottlawsonbc/audio-reactive-led-strip), [huebee](http://huebee.buzz/), and [How to connect and control a Raspberry Pi WS2801 RGB LED Strip](https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/)

## Requirements:
1. Raspberry Pi
2. WS2801 LED strip
3. 5V 10A power supply (But I am using a 20A, so that should be fine)
4. Jumper cables and breadboard
5. USB microphone

I followed this [guide](https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/)

## Install prerequisites:
```
sudo apt-get update
sudo apt-get install python-pip -y
sudo pip install adafruit-ws2801
sudo pip install flask
sudo apt-get install python-numpy python-scipy python-pyaudio
```

## Audio device configuration -- Taken from: [audio-reactive-led-strip](https://github.com/scottlawsonbc/audio-reactive-led-strip)
For the Raspberry Pi, a USB audio device needs to be configured as the default audio device.

Create/edit `/etc/asound.conf`
```
sudo nano /etc/asound.conf
```
Set the file to the following text
```
pcm.!default {
    type hw
    card 1
}
ctl.!default {
    type hw
    card 1
}
```

Next, set the USB device to as the default device by editing `/usr/share/alsa/alsa.conf`
```
sudo nano /usr/share/alsa/alsa.conf:
```
Change
```
defaults.ctl.card 0
defaults.pcm.card 0
```
To
```
defaults.ctl.card 1
defaults.pcm.card 1
```
Put the `led.py` file into `audio-reactive-led-strip/python/` replacing the old `led.py`

Now Just run the following:

```
sudo python lights.py
```

If you are getting bufferoverflow issues follow [this](https://github.com/scottlawsonbc/audio-reactive-led-strip/commit/fa492bbffc13cc59820ffff1bf8767daad969620)
