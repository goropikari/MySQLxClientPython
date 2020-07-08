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

# Follow packets

Open two terminals. Execute `docker-compose exec ubuntu bash` at each terminals (terminal 1, 2).
```
ngrep -N -x # terminal 1

python3 sample.py # terminal 2
```

Then we obtain packets tranfering between MySQL server and client.
```
# ngrep -N -x
interface: eth0 (172.22.0.0/255.255.0.0)
filter: ((ip || ip6) || (vlan && (ip || ip6)))
####
T(6) 172.22.0.3:33060 -> 172.22.0.2:59520 [AP] #4
  05 00 00 00 0b 08 05 1a    00                         .........
##
T(6) 172.22.0.2:59520 -> 172.22.0.3:33060 [AP] #6
  0a 00 00 00 04 0a 07 4d    59 53 51 4c 34 31          .......MYSQL41
##
T(6) 172.22.0.3:33060 -> 172.22.0.2:59520 [AP] #8
  17 00 00 00 03 0a 14 40    4e 5f 41 5a 43 3d 62 72    .......@N_AZC=br
  1d 16 45 10 3a 74 01 2f    01 48 00                   ..E.:t./.H.
##
T(6) 172.22.0.2:59520 -> 172.22.0.3:33060 [AP] #10
  33 00 00 00 05 0a 30 00    72 6f 6f 74 00 2a 35 63    3.....0.root.*5c
  31 37 38 38 63 34 64 38    31 36 32 37 30 35 39 66    1788c4d81627059f
  65 65 65 37 62 37 31 39    38 37 31 34 33 35 39 31    eee7b71987143591
  32 33 35 31 36 66 00                                  23516f.
##
T(6) 172.22.0.3:33060 -> 172.22.0.2:59520 [AP] #12
  0f 00 00 00 0b 08 03 10    02 1a 08 08 0b 12 04 08    ................
  02 18 06 03 00 00 00 04    0a 00                      ..........
##
T(6) 172.22.0.2:59520 -> 172.22.0.3:33060 [AP] #14
  1f 00 00 00 0c 0a 15 73    65 6c 65 63 74 20 2a 20    .......select *
  66 72 6f 6d 20 66 6f 6f    2e 62 61 72 1a 03 73 71    from foo.bar..sq
  6c 20 00                                              l .
##
T(6) 172.22.0.3:33060 -> 172.22.0.2:59520 [AP] #16
  21 00 00 00 0c 08 01 50    0b 12 02 69 64 1a 02 69    !......P...id..i
  64 22 03 62 61 72 2a 03    62 61 72 32 03 66 6f 6f    d".bar*.bar2.foo
  3a 03 64 65 66 28 00 00    00 0c 08 07 40 ff 01 50    :.def(......@..P
  28 12 04 6e 61 6d 65 1a    04 6e 61 6d 65 22 03 62    (..name..name".b
  61 72 2a 03 62 61 72 32    03 66 6f 6f 3a 03 64 65    ar*.bar2.foo:.de
  66 0a 00 00 00 0d 0a 01    02 0a 04 64 6f 67 00 0a    f..........dog..
  00 00 00 0d 0a 01 04 0a    04 63 61 74 00 01 00 00    .........cat....
  00 0e 0f 00 00 00 0b 08    03 10 02 1a 08 08 04 12    ................
  04 08 02 18 00 01 00 00    00 11                      ..........
#####
```
