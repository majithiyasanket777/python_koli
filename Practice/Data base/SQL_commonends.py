"""
1-
2- sudo apt install mysql-server
(yaha pe check karna hoga start hogaya na hamara sql) 
3- sudo mysql (Enter) 
Ager Exit hona hai my sql shell se to :- exit (Enter)
4 sudo mysql_secure_installation
exit my sql
5.sudo snap install mysql-workbench-community
"""
# my password is :- 'Root@1234

"""
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';


py mysql

Diffrence beteen py mysql and connectore
"""
#--------------#---------------------pyMySQL--------------------#--------------------#

"""
1. pip install pymysql

"""
#----------------#----------------#-------------------#-----------------#-------------
# How to install pip on ubuntu

"""
1. sudo apt-get install python-pip

2. pip install mysql-connector-python
3. 


"""

# Diffrence pyMySQl and MYSQL connector

"""
Feature	           PyMySQL	                        MySQL Connector (mysql-connector-python)
Developer	      Third-party	                    Oracle (Official)
Performance	      Slightly slower (pure Python)	    Faster (C extensions)
Compatibility	  MySQL and MariaDB	                MySQL only
Support	          Community-supported	            Officially supported by Oracle
Installation	  pip install pymysql	            pip install mysql-connector-python
Use Case	      Lightweight apps	                Production environments


PyMySQL: Use when you need compatibility with both MySQL and MariaDB or if you want a 
library entirely written in Python.

MySQL Connector: Use when working with MySQL exclusively and require an officially 
supported, high-performance library.

"""

# cd ..   exit that enviorement

# F11 full screen 

