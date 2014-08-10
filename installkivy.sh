#!/bin/bash
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get install pkg-config python-setuptools python-pygame python-opengl python-gst0.10 python-enchant gstreamer0.10-plugins-good python-dev build-essential libgl1-mesa-dev libgles2-mesa-dev cython
sudo apt-get update
sudo add-apt-repository ppa:cython-dev/master-ppa
sudo apt-get update
sudo apt-get install cython
sudo apt-get update
sudo apt-get install python-kivy
sudo apt-get update
sudo pip install git+https://github.com/dgrtwo/ParsePy.git
