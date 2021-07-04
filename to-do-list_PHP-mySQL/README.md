# To-do-list_PHP-mySQL

## Installation:

1. Import "to_do.sql" to your database
```
mysql -u root -p to_do < ..../To-do-list_PHP-mySQL/to_do.sql
```

2. Change database info in "database.php"
```
<?php
//Username and Password must be changed to actual one
$dbServername = "localhost";
$dbUsername = 'root';
$dbPassword = 'root';
$dbName = "to_do";
```

3. Run PHP environment
```
php -S localhost:4000
```

## Description:

* User can add task to to-do list
* User can edit any added task
* User can delete any added task
* User can mark task as done
* All tasks are saved in mySQL database

![To-do list PHP mySQL Demo](demo/to-do-list_PHP-mySQL.gif)
