# Setting up the Jetson Nano

Starting from the [default SD Card image](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write), software updates need to be done to maintain compatibility with the latest versions of Python and OpenCV used in this project.

## Install Python 3.8 or Newer

The default distro for the Jetson Nano ships with Ubuntu 18.04, and Python 3.6. To use the libraries in the project, we need Python >= 3.8. We'll be building Python 3.10 from source.

```bash
sudo dpkg --configure -a
sudo apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tar.xz
tar -xvf Python-3.10.2.tar.xz
mkdir build-python-3.10.2
cd build-python-3.10.2
../Python-3.10.2/configure --enable-optimizations
make -j $(nproc)
sudo -H make altinstall
```

If you are only going to be using Python3 throughout and not Python2, you can override the alias in the bash terminal.

```bash
nano ~/.bashrc
# Add alias python=python3 at the end
source ~/.bashrc
```

## Install useful tools

```bash
sudo apt install -y nano v4l-utils
```

### Install VSCode

```bash
git clone https://github.com/JetsonHacksNano/installVSCode.git
cd installVSCode
./installVSCode.sh
```

## Create a virtual environment

If you want to encapsulate your Python environment, you can use the `python3-venv` tool.

```bash
# Create a new virtual environment
python3 -m venv .venv
# Activate virtual environment
source .venv/bin/activate
```

## Install hardware libraries for Python

To make use of the Jetson Nano's hardware peripherals (UART, I2C, SPI etc) in Python, these libraries need to be installed:

```bash
sudo pip3 install Jetson.GPIO sparkfun-ublox-gps sparkfun-qwiic-bme280 serial
```

For imaging, the USB Webcam can be accessed through OpenCV, which comes preinstalled on the default Jetson Nano image. The drivers for it should be universally available in the distro, as a video4linux (v4l2) device.

## References

* [GPS Library](https://qwiic-ublox-gps-py.readthedocs.io/en/latest/)
* [BME280 Library](https://learn.sparkfun.com/tutorials/qwiic-atmospheric-sensor-bme280-hookup-guide/all)
* [Jetson Nano Setup](https://www.jetsonhacks.com/2019/10/10/jetson-nano-uart/)