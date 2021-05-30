# PiTutorial

Raspberry Pi tutorial for beginners.


## Things you need to follow this tutorial
* Monitor with HDMI input
* HDMI cable
* Keyboard (USB)
* micro SD


## Installation!

1. Attach heat sinks
    ![image of heat sinks](images/heat-sink.jpg)

2. Make Raspberry Pi OS image (micro SD)
    * follow steps in https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi
    * You can download latest Raspberry Pi OS image from https://www.raspberrypi.org/downloads/raspbian/.
        * [RASPBIAN STRETCH LITE](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip): CLI only, preferred 
        * [RASPBIAN STRETCH WITH DESKTOP](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip): GUI included, but slow
    * Insert the micro SD card to the slot in the back.
        ![image of heat sinks](images/sd-card.jpg)
    * Connect the power, monitor (through HDMI), keyboard (through USB) to your RPI. Then, you will see four raspberries and many booting logs on your screen.
        ![image of heat sinks](images/booting.jpg)
    * Log in with default id/pw
        * id: pi
        * pwd: raspberry

3. Configuring your RPI
    * Change password!
        ```bash
        passwd
        ```
        Account "pi" is an administrator. So, it's very important to use a strong password to secure your system. 

        It's also a good idea to make a new id that you like and make it an administrator. You can do it as follows.
        ```bash
        sudo adduser [ID YOU WANT]
        sudo adduser [ID YOU WANT] sudo
        ```
        
        Here, "sudo" is a special command (only for administrators) to change or set critical system settings. Any sudo command requires authentification based on the password of the current your.
        
        System-critical operations can be done only by sudoers.
        
        For example, you can reboot your RPI with this command:
        ```bash
        sudo reboot
        ```
        
        You can shutdown the system with:
        ```bash
        sudo shutdown -h now
        ```
        It's a good idea to shutdown before you unplug the power. 
        
        
    * Using raspi-config
        In RPI, you can change any setting you like using command line commands. 
        There is an easier way. Execute: 
        ```bash
        sudo raspi-config
        ```
        You will see a menu for some common settings.
        ![image of heat sinks](images/raspi-config.png)
        
    * Enable SSH
    
        SSH is the standard way to connect any Linux-based machine. Using ssh, you can remotely connect to your RPI. So, let's turn it on.
        
        Run "raspi-config" and select "5 Interfacing Options" > "P2 SSH". Then, you can enable SSH.
        ```bash
        sudo raspi-config
        ```        
        ![image of heat sinks](images/raspi-config-interface.png)
        ![image of heat sinks](images/raspi-config-ssh1.png)

    * Change locale
    
        By default, RPI is set up for British English and British keyboards. The former may not a big problem, but the latter is. With default setting, you may not type special characters like " or #!
        So, let's change the locale and keyboard layout using raspi-config. 
        
        Run "raspi-config" and select "4 Localization Options" > "I1 Change Locale"
        ```bash
        sudo raspi-config
        ```        
        ![image of locale setting](images/raspi-config-locale1.png)
        ![image of locale setting](images/raspi-config-locale2.png)        
        
        Here, uncheck anything starting with "en_GB" and check "en_US.UTF-8 UTF-8."
        ![image of locale setting](images/raspi-config-locale3.png)
        
        Set also default locale to "en_US.UTF-8 UTF-8." Then, wait for a while.
        ![image of locale setting](images/raspi-config-locale4.png)

    
        ```bash
        sudo reboot
        ```    

    * Change keyboard layout
    
        Run "raspi-config" and select "4 Localization Options"> "I3 Change Keyboard layout". 
        Select "Generic 102-key", "English(US)", and default for the others. Then reboot.
        ```bash
        sudo raspi-config
        ```
        ![image of locale setting](images/raspi-config-keyboard1.jpg)
        ![image of locale setting](images/raspi-config-keyboard2.jpg)
        ![image of locale setting](images/raspi-config-keyboard3.jpg)
        ```bash
        sudo reboot
        ```

    * For other settings, see https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration
    
4. Network setup 
    * Because this is an "IoT" class, we will use WiFi.
    * But, unfortunately, the built-in WiFi has a serious compatibility issues with many WiFi APs. See [here](http://forums.rasplay.org/topic/196/공지-raspberrypi-model-3b-wifi-issue) for more detail.
    * You have two solutions
        * Replace WiFI AP (which I did for rooms 326 and 413)
        * Add another WiFi dongle to your RPI 
    * In room 326, you can setup as follows to access the WiFi.
    
        **ADD** the following lines at the end of /etc/wpa_supplicant/wpa_supplicant.conf. (**DO NOT CHANGE THE FIRST THREE LINES!**)
        ```
        network={
            ssid="RPI_5G"
            psk="raspberrypi"
            priority=1
        }
        network={
            ssid="RPI"
            psk="raspberrypi"
            priority=2
        }
        ```

        Then, reboot.

        ```bash
        sudo reboot
        ```

## Play with RPI
1. Change your hostname.

Hint: use "raspi-config" command

2. Change timezone.

Hint: use "raspi-config" command and see inside of localization options

3. Remotely connect your RPI using SSH.

4. Update your RPI

```bash
sudo apt-get update
sudo apt-get upgrade
```


## References
  * https://learn.adafruit.com/series/learn-raspberry-pi (original tutorial)
  * https://github.com/zhangshuo951227/raspberry-pi/wiki (updated for Jessie)
  * 2017 Summer Short Course 
