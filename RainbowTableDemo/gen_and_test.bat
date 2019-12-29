REM Windows only
@echo off
java -Xmx512m -jar RainbowTableDemo.jar hash passwords.txt hashes.txt
java -Xmx512m -jar RainbowTableDemo.jar generate table#1-100-100000.rt 100 100000
java -Xmx512m -jar RainbowTableDemo.jar generate table#2-100-100000.rt 100 100000
java -Xmx512m -jar RainbowTableDemo.jar crack table#1-100-100000.rt hashes.txt
java -Xmx512m -jar RainbowTableDemo.jar crack table#2-100-100000.rt hashes.txt