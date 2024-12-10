# Shokjøp

## **📚 Table of Contents**
  - [✨ Introduction](#introduction)
  - [🛠️ Requirements](#%EF%B8%8F-requirements)

    ## [Shokjøp MVP](#shokjøp-features)

  - [Cart](#1basic-use-of-container-queries)
  - [Purchase History](#2basic-use-of-grid)
     

## **✨Introduction**  

###  Shoskjøp aims is for every gamers who want to fulfill they're gaming experience using better gaming accessories.




###  🛠️ Requirements 

## **1. Download and install Visual Studio Code <img src=https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg width="25px">**
- Click on the link [https://code.visualstudio.com/download]
- Click on the type of operating system you have.
  
## 2. Installing  Python <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="30px">

- Click on the link [https://www.python.org/downloads/]

### Other Method
- Press `Windows Key + R` to open the "Run" menu.
   - Type `cmd` and press **Enter**. This will open the Command Prompt.
   - install Python by typing: 
   ```bash 
    pip install python 
   ``` 
## **3. Installing MariaDB to PI 
### Make sure you install Ubuntu on your `PI` 

- Press `Windows Key` to open the "Search" menu.
   - Type `Terminal` and press **Enter**. This will open the Terminal Prompt.
   - install MariaDB by typing: 
```bash 
    sudo apt install mariadb-server
```
```bash
    sudo mysql_secure_installation
```
## 4. Creating and Managing Databases
- 1. Log in to MariaDB as root:

```bash
    sudo mysql -u root -p
```
- 2. Create a new database:
```bash
    CREATE DATABASE my_database;
```
- 3. Create a new user and grant privileges:
```bash
    CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';
    FLUSH PRIVILEGES;
```
- 4. Exit MariaDB:
```bash
    EXIT;
```
## 5. Clone the Repository

Follow these simple steps to clone the repository to your local machine:

1. **Create a folder** where you want to store the cloned files:
   - You can create a folder anywhere on your computer (example, in your "Documents" or on your desktop).

2. **Open the Command Prompt**:
   - Press `Windows Key + R` to open the "Run" menu.
   - Type `cmd` and press **Enter**. This will open the Command Prompt.

3. **Clone the Repository**:
   - In the Command Prompt, use the `git clone` command to clone the repository into the folder you created:
   ```bash
   git clone https://github.com/aemrcd/Terminoppgave-Nettbutikk-

## **Shokjøp Features**

## **1. Cart**  



## **2. Purchase History**  

<img src="./static/img/Gridexample.png">



- *if you are having trouble understanding the function there is a comment to fully understand the code it self*


## **3.Use of `align-content`**  

<img src="./static/img/align-content_Funtions.gif">


- For better explanation open `align-content`  in the *template & static folder* or create your own HTML file.* 













<details style="background-color:red ;">
<summary>shoutout</summary>

### soutout to Jasan for the help!


</details>
