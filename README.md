# Building own MySQL Client supporting X Protocol with Python

- [X Protocol](https://dev.mysql.com/doc/dev/mysql-server/latest/mysqlx_protocol.html)

Example:
```bash
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec ubuntu bash
$ mysql -h db -uroot -ptest < ex.sql
$ mysql -h db -uroot -ptest -e "SELECT * FROM foo.bar"
#=> +------+------+
#=> | id   | name |
#=> +------+------+
#=> |    1 | dog  |
#=> |    2 | cat  |
#=> +------+------+

$ python3 sample.py
#=> type: SINT
#=> name: "id"
#=> original_name: "id"
#=> table: "bar"
#=> original_table: "bar"
#=> schema: "foo"
#=> catalog: "def"
#=> length: 11
#=>
#=> type: BYTES
#=> name: "name"
#=> original_name: "name"
#=> table: "bar"
#=> original_table: "bar"
#=> schema: "foo"
#=> catalog: "def"
#=> collation: 255
#=> length: 40
#=>
#=> field: "\002"
#=> field: "dog\000"
#=>
#=> field: "\004"
#=> field: "cat\000"
```
