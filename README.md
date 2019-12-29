# Crypto-report
Files used for my cryptography report about rainbow tables

Basic implementation for MD5 but easily changeable for other hash algorithms


## Rainbow Table Demo from

https://mieuxcoder.com/2008/01/02/rainbow-tables



## Basic usage 

### md5_hash

hash with md5 all things passed as parameter

```shell
python md5_hash.py test foo bar
```

out 

```
098f6bcd4621d373cade4e832627b4f6
acbd18db4cc2f85cedef654fccc4a4d8
37b51d194a7513e45b56f6524f2d51f2
```

for using a file

```
python md5_hash.py $(cat RainbowTableDemo/passwords.txt) 
```



### Brute-force

```sh
python md5_hash.py foo | time python md5_brutforce_mulprocessing.py
```

out

```
password hash md5 :
acbd18db4cc2f85cedef654fccc4a4d8
...
mot : foo
```



### Dictionary

#### Generating 

python genDico.py -h for details

```shell
python genDico.py -f /tmp/dico.table -l 3 -v 2  
```

out 

```
time to generate the table : 0.413s
the generated file is 29.31 MB
```



#### Usage

Using  grep to find the first occurrence of the hash in the table

```shell
grep -m 1 $(python md5_hash.py foo)  /tmp/dico.table 
```

out

```shell
foo,acbd18db4cc2f85cedef654fccc4a4d8
```





