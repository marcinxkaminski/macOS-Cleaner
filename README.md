# macOS Cleaner 👨🏼‍💻🧹
Cleaning app for macOS. Removes all files associated with apps you want to remove.

## Important! ⚠️
  _Note, that removing files and directories from Libraries and etc. not always could be done without 'root' user permissions (with sudo) so it is really __dangerous__ to use sudo if you don't know what you're doing!_


## How it works? 🤔
You need always to specify your username in order to properly navigate to user's Library directory, where the most files are. Secondly, you need to specify the names of apps to remove. For e.g. if you want to remove Photoshop files you could specify both 'Photoshop' and 'Adobe' apps (note that all Adobe apps could be removed). Then the script will scan all folders and if any matches, it will prompt the message if it should delete this folder or not.


## Prerequisites ☕️
  * [Python 3.6 or later](//www.python.org/downloads) 🐍


## Install 💻
  1. Clone project
    ```bash
    git clone https://github.com/marcinxkaminski/macOS-Cleaner.git
    ```

  2. Go to project
    ```bash
    cd macOS-Cleaner
    ```
  3. You MUST set configuration variables!


## Configuration & References 🛠
  * `USERNAME`
    Your computer user username, used by your system. Allows to navigate to proper Library directory for the user.

  * `LIBRARIES_PATHS`
    List of paths to the Libraries directories, both global for all users and local for your current computer user. What's more, if you want to scan any other folder to clean, you could add it here.

  * `APPS_TO_REMOVE`
    List of apps (directories) names you want to remove.


## Run 🏃🏼‍♀️🏃🏼‍♂️
  ``python3 clean.py`` or ``sudo python3 clean.py`` (be careful with it!)
