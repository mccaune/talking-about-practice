#To-do-list_PHP-mySQL

##Installation:

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

3. As email was blocking scrip.js file, you must change extension from script.txt to script.js

4. Run PHP environment
```
php -S localhost:4000
```


