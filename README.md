# Shokjøp

# **📚 Table of Contents**
  - [✨ Introduction](#introduction)
  - [🛠️ Requirements](#%EF%B8%8F-requirements)

    ## [Shokjøp Features](#shokjøp-features)

  - [Cart](#1-cart)
  - [Purchase History](#2-purchase-history)
     

# **✨Introduction**  

###  Shoskjøp aims is for every gamers who want to fulfill they're gaming experience using better gaming accessories.


#  🛠️ Requirements 

## **1. Download and install Visual Studio Code <img src=https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg width="25px">**
- Click on the link [https://code.visualstudio.com/download]
- Click on the type of operating system you have.
  
## 2. Installing  Python <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="30px">

- Click on the link [https://www.python.org/downloads/]

- Open the download file 
    - Click Customize installation
    - Make sure to select all boxes especially `pip` to install every types of libraries using the `pip` function
    - Click Next and select `"Add Python to environent Variables"` & `"Install Python 3.13 for all users"`
    
    - **INSTALL**

## 3. Cloning the Repository

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
   
- Installing libraries to python by typing the following commands. This will download all the libraries to use the website.

    ```bash 
    pip install -r requirements.txt
    ``` 

## 4. Installing MariaDB to PI 
### Make sure you install Ubuntu on your `PI` 

- Press `Windows Key` to open the "Search" menu.
   - Type `Terminal` and press **Enter**. This will open the Terminal Prompt.
   - install MariaDB by typing: 
```bash 
    sudo apt install mariadb-server
```
```bash
    sudo mariadb_secure_installation
```
## 5. Creating and Managing Databases
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
### Managing Tables in MariaDB:

1. Showing The Database:
- This statement works to show all of your database.
```bash
   SHOW DATABASES;
```
2. SELECTING The Database:
- This statement works if you have multiple database.
```bash
   USE "yourdatabase";
```
3. Viewing tables in your database
- To see the data inside a table, use the `SELECT` query. Replace `"yourtable"` with the name of the your table  to view.

```bash
   SELECT * FROM "yourdatabase";
```
4. Deleting a Row from a Table

- If you want to delete a specific row in a table, use the   `DELETE` statement with a `WHERE` and  Replace `"yourtable"` with the your table name and `"PLACE_YOUR_ID"` with the ID or condition to delete a spesific row.

```bash
    SELECT * FROM  "yourdatabase" WHERE Id IN = "PLACE_YOUR_ID";
```

# **Shokjøp Features**

<details>
<summary style="font-weight: bold; font-size: 15px;">Click to show the Features </summary>

## **1. Cart**  

<img src="Terminproj/static/img/Cart.gif">

- *This is a cart-based website that calculates the total items purchased and stores the purchase details in the database after the user completes their order.*


## **2. Purchase History**  

<img src="Terminproj/static/img/Purchase_history.gif">


- *This website displays the purchase history for users and administrators, with a dedicated database to store all past transactions.*


</details>
