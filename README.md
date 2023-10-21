# LittleHero 2.0

LittleHero 2.0 is an exciting Raspberry Pi-based project that combines computer vision, audio, and hardware control to create a versatile hero capable of carrying out various tasks. This README provides comprehensive instructions for setting up and running the project. 

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Audio Setup](#audio-setup)
- [Setting up the MAX7219](#setting-up-the-max7219)
- [Running the Project](#running-the-project)

---

## Prerequisites

Before you can start using LittleHero 2.0, you need to ensure that you have the following prerequisites in place:

1. **Raspberry Pi Setup:**
   - Make sure you have a working Raspberry Pi.
   - Expand the filesystem if not done already:
     ```shell
     $ sudo raspi-config
     Advanced > Expand File System
     $ sudo reboot
     ```

2. **OpenCV 4 Installation:**
   - Install OpenCV 4 and its dependencies:
     ```shell
     $ sudo apt-get update && sudo apt-get upgrade
     $ sudo apt-get install build-essential cmake unzip pkg-config
     $ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
     $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
     $ sudo apt-get install libxvidcore-dev libx264-dev
     $ sudo apt-get install libgtk-3-dev
     $ sudo apt-get install libcanberra-gtk*
     $ sudo apt-get install libatlas-base-dev gfortran
     $ sudo apt-get install python3-dev
     ```

3. **Download OpenCV 4:**
   - Download and extract OpenCV 4:
     ```shell
     $ cd ~
     $ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
     $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
     $ unzip opencv.zip
     $ unzip opencv_contrib.zip
     $ mv opencv-4.0.0 opencv
     $ mv opencv_contrib-4.0.0 opencv_contrib
     ```

4. **Install Numpy:**
   - Install Numpy using pip:
     ```shell
     pip install numpy
     ```

5. **Increase Swap Space:**
   - To prevent the Raspberry Pi from hanging during compilation, increase the swap space:
     ```shell
     $ sudo nano /etc/dphys-swapfile
     # Change CONF_SWAPSIZE from 100 to 2048
     $ sudo /etc/init.d/dphys-swapfile stop
     $ sudo /etc/init.d/dphys-swapfile start
     ```

6. **Compile OpenCV 4:**
   - Compile OpenCV with CMake:
     ```shell
     $ cd ~/opencv
     $ mkdir build
     $ cd build
     $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
              -D CMAKE_INSTALL_PREFIX=/usr/local \
              -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
              -D ENABLE_NEON=ON \
              -D ENABLE_VFPV3=ON \
              -D BUILD_TESTS=OFF \
              -D OPENCV_ENABLE_NONFREE=ON \
              -D INSTALL_PYTHON_EXAMPLES=OFF \
              -D BUILD_EXAMPLES=OFF ..
     # Compile using all cores
     $ make -j4
     $ sudo make install
     $ sudo ldconfig
     # Restore CONF_SWAPSIZE to 100MB and restart swap service
     ```

7. **Audio Setup:**
   - Install the pygame library for audio:
     ```shell
     $ sudo pip install pygame
     ```

8. **Setting up the MAX7219:**
   - Enable SPI in Raspberry Pi configuration.

---

## Installation

The following steps are required to install the LittleHero 2.0 project:

1. Clone this repository to your Raspberry Pi:
   ```shell
   $ git clone https://github.com/deepak1h/LittleHero2.0.git
   ```

2. Install the MAX7219 library:
   ```shell
   $ cd LittleHero2.0
   $ sudo apt-get install python-dev python-pip
   $ sudo pip install spidev
   $ git clone https://github.com/coding-world/max7219
   $ cd max7219
   $ sudo python setup.py install
   ```

3. Connect the 8x8 LED matrix to the Raspberry Pi as described in the [Setting up the MAX7219](#setting-up-the-max7219) section.

---

## Audio Setup

To play audio files, you can use the pygame library, which was installed in the [prerequisites](#prerequisites) section.

---

## Setting up the MAX7219

The MAX7219 setup is an essential part of the LittleHero 2.0 project. Please follow these steps:

1. Run `sudo raspi-config` and enable SPI (System > Advanced Options > SPI).

2. Reboot your Raspberry Pi to apply the SPI settings.

3. Install the MAX7219 library as explained in the [Installation](#installation) section.

4. Connect the 8x8 LED matrix to the Raspberry Pi as described in the [Prerequisites](#prerequisites) section.

5. Test the library installation with the following command:
   ```shell
   $ sudo python max7219/examples/matrix_test.py
   ```

---

## Running the Project

Connect wires according to the little,pdf instruction
Now that you have completed the setup, you are ready to run the LittleHero 2.0 project.

**Step 1: Connect the Hardware**
- Connect the motors to the motor driver.
- Connect the MAX7219.
- Attach the camera to the camera port.

**Step 2: Run the Project**
- Navigate to the project folder:
  ```shell
  $ cd LittleHero2.0
  ```
- Run the project using the following command:
  ```shell
  $ python3 run.py
  ```
This command will execute two files simultaneously, controlling LittleHero 2.0.

**Optional: Run on Boot**
- If you want to start the project on boot, edit the `.bashrc` file and add the command to run `run.py` at the end:
  ```shell
  $ nano ~/.bashrc
  # Add the following line to the end of the file
  python3 /path/to/LittleHero2.0/run.py
  ```

Now, LittleHero 2.0 should be up and running, ready to take on its heroic tasks!

Enjoy your LittleHero 2.0 adventure! If you encounter any issues or have questions, feel free to reach out to us for support.
