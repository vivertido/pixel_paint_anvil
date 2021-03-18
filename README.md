# pixel_paint_anvil
A tool for remotely creating Sense HAT 8x8 pixel drawings using Anvil.

![Imgur](https://i.imgur.com/QdMGb4t.png)

## Usage

This tool is meant to be used with a client Anvil app. Copy the app from Anvil here: [PixelPaint](https://anvil.works/build#clone:JCMXMGJ2VZRZ3MXS=ZVD67MYOZH3SL7YHYGCXV2LG)

On your Raspberry Pi, install the anvil.server package first.
```bash
$ pip install anvil-uplink
```

Clone this app on your Pi. 

On your Anvil app, enable Uplink.

![uplink](https://anvil.works/learn/tutorials/img/raspberry-pi/uplink-gear-menu.png)

Get your Uplink key.

![uplink key](https://anvil.works/learn/tutorials/img/raspberry-pi/enable-uplink.png)

On your **pixel_paint_server.py** file, replace the anvil uplink key

```python
anvil.server.connect("<your key goes here>")

```

On the client side, Click Run to launch the app, on the Pi, run the app from Thonny or the command line: 

```bash
$ python3 /your/path/pixel_paint_server.py

```

Saved designs are in a raw Python list, with RGB values and a timestamp and are appended to a .txt file. 
To use these, copy and paste them into other Sense HAT scripts as needed. 

That's it!
