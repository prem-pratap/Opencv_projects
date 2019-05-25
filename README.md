# Opencv_projects


INSTALLATION OF  OPENCV 0N UBUNTU

Step 1 :    Login with Non-root user and  do below given steps

Note:  here i am login with me user

Step  2 :     update and upgrade system

ml@ml:~$ sudo apt-get  update  &&  sudo apt-get  upgrade

Step 3 :   Installing  python contrib dependency

ml@ml:~$ sudo pip install  opencv-contrib-python

Step  4 :   Installing  all recommended packages  (compilers)

ml@ml:~$ sudo apt-get install  build-essential

Step 5 :   Install required software 

ml@ml:~$ sudo apt-get install  cmake  git libgtk2.0-dev  pkg-config libavcodec-dev  libavformat-dev  libswscale-dev

Step 6:    Few recommended packages need to be install 

ml@ml:~$ sudo apt-get  install  python-dev python-numpy  libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev  libjasper-dev  libdc1394-dev

ml@ml:~$ sudo apt-get  install  libavcodec-dev  libavformat-dev libswscale-dev libv4l-dev

ml@ml:~$ sudo apt-get  install  libxvidcore-dev  libx264-dev

ml@ml:~$ sudo apt-get  install  libgtk-3-dev

ml@ml:~$ sudo apt-get  install  libgtk-3-dev libatlas-base-dev  gfortran python2.7-dev  python3.5-dev

Step 7:  Downloading  opencv  

ml@ml:~$  wget -O  opencv.zip  https://github.com/opencv/opencv/archive/3.3.0.zip

Step: 8:  Downloading opencv_contrib

ml@ml:~$  wget -O  opencvcontrib.zip  https://github.com/opencv/opencv_contrib/archive/3.3.0.zip

Step 9:  Unzip both the files

ml@ml:~$ unzip  opencv.zip  opencv_contrib

step 10:   setup environment and upgrade pip

ml@ml:~$ sudo apt-get install python-pip && pip install --upgrade pip

ml@ml:~$ sudo pip  install virtualenv  virtualenvwrapper

ml@ml:~$ sudo  rm -rvf  ~/.cache/pip


step 11 :  making  environment persistant  for all and adding  line in the last line

ml@ml:~$ cat  ~/.bashrc

# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs

source /usr/local/bin/virtualenvwrapper.sh

# Loading  this  file  

ml@ml:~$ source   ~/.bashrc

Step  12:   creating  virtual environment

ml@ml:~$ mkvirtualenv cv -p python3

Note:     if you restarted your terminal or  shutdown your system then to load the environment

ml@ml:~$ workon  cv

Step 13:   configure the cmake

(cv) ml@ml:~$ cd  opencv-3.3.0/
(cv) ml@ml:~/opencv-3.3.0$ mkdir build  ;  cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
      -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
      -D BUILD_EXAMPLES=ON ..





Note:  It will take some time

Step 14 :  Compiling  opencv

make -j4

Step 15:   installopencv  (make sure you are under  build folder)

(cv) ml@ml:~/opencv-3.3.0/build$ sudo make install
(cv) ml@ml:~/opencv-3.3.0/build$ sudo ldconfig


finally :

Go to directory given on web:
=====================

rename the file  cv2.so

(cv) ml@ml:~$ cd /usr/local/lib/python3.5/site-packages/
(cv) ml@ml:/usr/local/lib/python3.5/site-packages$ ls
cv2.so


goto your home directory  and make link of that file 

ml@ml:~$  cd         ~/.virtualenvs/cv/lib/python3.5/site-packages/

ml@ml:~/.virtualenvs/cv/lib/python3.5/site-packages$ ln -s  /usr/local/lib/python3.5/site-packages/cv2.so cv2.so 


Now you can enjoy Image processing with OPENCV 

