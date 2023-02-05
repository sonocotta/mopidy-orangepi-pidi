## Host

install prerequisites
`apt install python3-dev python3.8-venv python3-gi pkg-config libcairo2-dev libgirepository1.0-dev`

PIL dependecies
`apt install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev iblcms2-dev ibwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev`

create venv
`Ctrl-Shift-P > Python: Create Environment`
`Ctrl-Shift-P > Python: Select Interpreter`

fix missing deps in the virtual env
`pip install pygobject`

fix missing deps in the virtual env <- TODO: get rid of dependency on numpy
`pip install numpy`

install deps, attach to mopidy installation in virtual env
`python setup.py develop`

run/debug mopidy in virtual env by hitting F5, or manually
`mopidy -vv -o http/port=5000 -o http/hostname=0.0.0.0`

GPIO permissions (if missing)
/etc/udev/rules.d/local.rules
`ACTION=="add", KERNEL=="spidev0.0", MODE="0666"`
`sudo usermod -a -G dialout dronische`