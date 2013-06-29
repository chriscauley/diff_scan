diff_scan
=========

Visual test sweet for web development

Requirements
--------

* webkit2png - https://github.com/AdamN/python-webkit2png/

webkit2png's pip installation didn't install it on the python path, so I found it easier to just build from source.

```bash
apt-get install python-qt4 libqt4-webkit xvfb
apt-get install flashplugin-installer

git clone https://github.com/adamn/python-webkit2png.git python-webkit2png
python python-webkit2png/setup.py install
```

