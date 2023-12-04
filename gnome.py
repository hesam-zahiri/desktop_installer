RED = "\033[1;31m"
WHITE = "\033[1;37m"
ORANGE = "\033[1;33m"

desktop_list = f"""


    {RED}[{WHITE}::{RED}]{ORANGE} ============================================= {RED}[{WHITE}::{RED}]{ORANGE}
{RED}{WHITE}{RED}{ORANGE}     ==                                {RED}{WHITE}{RED}{ORANGE}                 ==
{RED}{WHITE}{RED}{ORANGE}     ==                                {RED}{WHITE}{RED}{ORANGE}                 ==
{RED}{WHITE}{RED}{ORANGE}     ==         {RED}[{WHITE}a{RED}]{ORANGE} Arch       {RED}[{WHITE}d{RED}]{ORANGE} Debian    {RED}{WHITE}{RED}{ORANGE}           ==
{RED}{WHITE}{RED}{ORANGE}     ==         {RED}[{WHITE}r{RED}]{ORANGE} RedHat                              ==
{RED}{WHITE}{RED}{ORANGE}     ==                                {RED}{WHITE}{RED}{ORANGE}                 ==
{RED}{WHITE}{RED}{ORANGE}     ==                                {RED}{WHITE}{RED}{ORANGE}                 ==
    {RED}[{WHITE}::{RED}]{ORANGE} ============================================= {RED}[{WHITE}::{RED}]{ORANGE}

"""

print(desktop_list)

import subprocess
import os

# Get the name of the current Linux distribution
distribution_name = subprocess.check_output(["lsb_release", "-i"]).decode("utf-8").strip()

# Get a Linux distribution from the user
distribution = input("Choose your distribution base.(Choose the desired number.): ")

# If the distribution is Archbase, run the codes for installing GNOME Desktop on Arch

if distribution == "a":
  print("Your distribution is Archbase.")
  subprocess.Popen(["sudo", "pacman", "-Sy", "gnome-shell"]).wait()
  subprocess.Popen(["sudo", "systemctl", "enable", "gnome-session"]).wait()
  subprocess.Popen(["sudo", "systemctl", "start", "gnome-session"]).wait()
  subprocess.Popen(["sudo", "reboot"]).wait()

# If the distribution is Debian Base, run the codes for installing the GNOME desktop on Debian

elif distribution == "d":
  print("Your distribution is debian base.")
  subprocess.Popen(["sudo", "apt-get", "install", "gnome-shell"]).wait()
  subprocess.Popen(["sudo", "update-alternatives", "-s", "x-session-manager", "/usr/bin/gnome-session"]).wait()
  subprocess.Popen(["sudo", "reboot"]).wait()
  
# If it is Red Hat Base distribution, run the codes related to installing GNOME desktop on Red Hat

elif distribution == "r":
  print("Your distribution is Red Hat Base.")
  subprocess.Popen(["sudo", "yum", "install", "gnome-shell"]).wait()
  subprocess.Popen(["sudo", "systemctl", "enable", "gnome-session"]).wait()
  subprocess.Popen(["sudo", "systemctl", "start", "gnome-session"]).wait()
  subprocess.Popen(["sudo", "reboot"]).wait()

# If it's another distribution, send an error message
else:
  print("Your distribution is not supported.")
