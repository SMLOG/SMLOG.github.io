---
layout: default
---


edit /etc/sysconfig/network-scripts/ifcfg-enp0s3

change "ONBOOT=no" to "ONBOOT=yes"

PuTTY：http://putty.cs.utah.edu/download.html

Xming：http://xming.en.softonic.com/



### oracle 19c

[download](https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html)

create group
```bash


groupadd -g 5001 dba
groupadd -g 5002 asmdba
groupadd -g 5003 backupdba
groupadd -g 5004 dgdba
groupadd -g 5005 kmdba
groupadd -g 5006 racdba
groupadd -g 5007 oper
groupadd -g 5008 oinstall
useradd -u 5000 -g oinstall -G dba,asmdba,backupdba,dgdba,kmdba,racdba,oper oracle
wget http://yum.oracle.com/public-yum-ol7.repo -O /etc/yum.repos.d/public-yum-ol7.repo
wget http://public-yum.oracle.com/RPM-GPG-KEY-oracle-ol7 -O /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
yum install oracle-database-preinstall-19c.x86_64 -y


 groupadd oinstall
 groupadd dba
 groupadd asmdba
 groupadd backupdba
 groupadd dgdba
 groupadd kmdba
 groupadd racdba
 groupadd oper

 useradd -g oinstall -G dba,asmdba,backupdba,dgdba,kmdba,racdba,oper oracle
 passwd  oracle

[root@localhost ~]# mkdir -p /u01/app/oracle/product/19c/db_1
# mkdir -p /u01/app/oraInventory
[root@localhost ~]# chown -R oracle:oinstall /u01/app
# chmod -R 775 /u01/*
[root@localhost usr]# mkdir -p /usr/swap

[root@localhost usr]# cd /usr/swap/

[root@localhost swap]# dd if=/dev/zero of=swapfile bs=1024 count=2749398

[root@localhost swap]# mkswap /usr/swap/swapfile

[root@localhost swap]# swapon /usr/swap/swapfile

[root@localhost swap]# free -h

#add below line to /etc/fstab

/usr/swap/swapfile swap swap defaults 0 

mount -o size=1500M  -o remount /dev/shm

echo "
oracle   soft   nofile    1024
oracle   hard   nofile    65536
oracle   soft   nproc    16384
oracle   hard   nproc    16384
oracle   soft   stack    10240
oracle   hard   stack    32768
oracle   hard   memlock    134217728
oracle   soft   memlock    134217728
oracle   soft   data    unlimited
oracle   hard   data    unlimited
" >> /etc/security/limits.conf

echo "
fs.file-max = 6815744
kernel.sem = 250 32000 100 128
kernel.shmmni = 4096
kernel.shmall = 1073741824
kernel.shmmax = 4398046511104
kernel.panic_on_oops = 1
net.core.rmem_default = 262144
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048576
net.ipv4.conf.all.rp_filter = 2
net.ipv4.conf.default.rp_filter = 2
fs.aio-max-nr = 1048576
net.ipv4.ip_local_port_range = 9000 65500
" >> /etc/sysctl.conf
sysctl -p


cat /etc/sysctl.conf 
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
#ORACLE SETTING

kernel.shmmax = 64424509440
kernel.shmmni = 4096
kernel.shmall = 15728640
kernel.sem = 5010 641280 5010 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default = 262144
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048586
fs.aio-max-nr = 1048576
fs.file-max = 6815744


sysctl -p


[root@localhost ~]# su - oracle

[oracle@localhost ~]$ vi .bash_profile

export ORACLE_HOME=/u01/app/oracle/product/19c/dbhome_1
export PATH=$PATH:$ORACLE_HOME/bin
export ORACLE_SID=orcl

[oracle@localhost ~]$ source .bash_profile

[oracle@localhost db_1]$ unzip -d /u01/app/oracle/product/19c LINUX.X64_193000_db_home.zip


systemctl stop firewalld.service
systemctl disable firewalld.service
systemctl status firewalld.service

sed -i s'\enforcing\disable\g' /etc/selinux/config

yum install bc binutils  compat-libcap1  compat-libstdc++33  elfutils-libelf  elfutils-libelf-devel  fontconfig-devel  glibc  glibc-devel  ksh  libaio  libaio-devel  libX11  libXau  libXi  libXtst  libXrender  libXrender-devel  libgcc  libstdc++  libstdc++-devel  libxcb  make  smartmontools  sysstat  kmod* libstdc++ gcc-c++ compat-libstdc++-33 -y

#yum -y install xdpyinfo
#[root@localhost lib]# dnf install libns

yum install xauth
#X11 forward

echo $DISPLAY

[oracle@localhost 19c]./runInstaller


```



[refer link1](https://blog.csdn.net/okc_champion/article/details/117899030?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-117899030-blog-119835073.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-117899030-blog-119835073.pc_relevant_paycolumn_v3&utm_relevant_index=11)
[link2](https://oracledbwr.com/step-by-step-oracle-19c-installation-on-linux/)
[link3](https://blog.csdn.net/weixin_49080355/article/details/119835073)
[link4] https://www.freesion.com/article/21051210748/

silent:
http://t.zoukankan.com/halberd-lee-p-12559583.html

Other: exFAT
```bash 

sudo yum install epel-release
sudo rpm -v --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
sudo yum install exfat-utils fuse-exfat

```
[link1](https://cloud.tencent.com/developer/article/1626805)
[link2](https://blog.csdn.net/qq_41204553/article/details/123983870)
[link3](https://blog.csdn.net/xuheng8600/article/details/79784547)

GUI
```bash
yum grouplist
yum groupinstall "Server with GUI"
reboot
startx


oracle$ ./runInstaller -silent -responseFile ~/db_install.rsp

```

sqlplus:
```
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm 
yum install rlwrap
```


https://www.codeleading.com/article/5097919542/


```sql
conn system
conn sys as sysdba
select * from v$version;
select sys_context('USERENV','CON_NAME') from dual;
select con_id,dbid,guid,name,open_mode from v$pdbs;
show pdbs;
select name,cdb from v$database;

--创建用户（oracle创建用户会自动创建schema）
create user vbo identified by vbo;
--创建表空间
create tablespace ts_vbo datafile 'C:\oracle\data\qa\vbo01.dbf' size 500M AUTOEXTEND ON;
--添加数据文件给表空间
ALTER TABLESPACE ts_vbo ADD DATAFILE 'C:\oracle\data\qa\vbo02.dbf' size 500M AUTOEXTEND ON;
--删除表空间及数据文件
--drop tablespace ts_vbo including contents and datafiles;

--给用户分配默认表空间
alter user vbo default tablespace ts_vbo;

--授予用户角色权限
grant connect,resource,RECOVERY_CATALOG_OWNER,unlimited tablespace to vbo;

```

```bash
dbca
netca
```

startup:
```
startup nomount
ipcs -m
show parameter spfile;
startup mount;
show parameter control;
alter database open;
select file_name from dba_data_files;
select group#,member from v$logfile;

```
http://www.wallcopper.com/database/1704.html
https://www.51cto.com/article/541583.html
```sql
select flashback_on from v$database;

select log_mode from v$database;
archive log list


```

https://blog.csdn.net/qq_41944882/article/details/106737047
rman:
```
rman target /
rman tareget sys/oracle@orcl

RMAN>show all

RMAN> configure retention policy clear;

```

```sql
CREATE pluggable DATABASE pdborcl admin USER pdbadmin identified BY Learning roles=(connect)
file_name_convert= ('D:\App\Oracle\oradata\orcl\pdbseed', 'D:\App\Oracle\oradata\orcl\pdborcl'); 
```

select distinct isspecified from v$spparameter;

CREATE DATABASE mynewdb
/USER SYS IDENTIFIED BY sys_password
/USER SYSTEM IDENTIFIED BY system_password
/EXTENT MANAGEMENT LOCAL
/UNDO TABLESPACE undotbs1
/DEFAULT TEMPORARY TABLESPACE tempts1
/DEFAULT TABLESPACE users;


rlwrap:
```bash
wget https://github.com/hanslub42/rlwrap/releases/download/v0.43/rlwrap-0.43.tar.gz
yum -y install readline*
tar -xzvf rlwrap-0.43.tar.gz
cd rlwrap-0.43
./configure
make
make install
```


https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/index.html
https://docs.oracle.com/en/database/oracle/oracle-database/19/admqs/index.html

```
LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.0.202)(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER=
  (SID_LIST=
      (SID_DESC=
         (GLOBAL_DBNAME=demo)
         (SID_NAME=demo)
        # (ORACLE_HOME=/u01/app/oracle/product/19.3/dbhome_1)
       )
      )
```

select dbms_xdb_config.getHttpsPort() from dual;
exec DBMS_XDB_CONFIG.SETLISTENERLOCALACCESS(false);


http://t.zoukankan.com/opma-p-11606242.html


tmpfs: https://blog.csdn.net/cougar_mountain/article/details/22988673
```
#edit /etc/fstab
tmpfs /dev/shm tmpfs defaults,size=1500M 0 0
mount –o remount  /dev/shm

```


lsnrctl:


```
lsnrctl start
lsnrctl reload
lsnrctl stop

alter system set local_listener=listener;
alter system set LOCAL_LISTENER='(ADDRESS = (PROTOCOL = TCP)(HOST = DaveDai)(PORT = 1522))';


alter system register;

```
```
[oracle@node2 oracle]$ lsnrctl status

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 26-MAY-2022 22:26:37

Copyright (c) 1991, 2019, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=node2)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 19.0.0.0.0 - Production
Start Date                26-MAY-2022 20:53:29
Uptime                    0 days 1 hr. 33 min. 7 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /u01/app/oracle/product/19.3/dbhome_1/network/admin/listener.ora
Listener Log File         /u01/app/oracle/diag/tnslsnr/node2/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=node2)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=node2)(PORT=5500))(Security=(my_wallet_directory=/u01/app/oracle/admin/orcl/xdb_wallet))(Presentation=HTTP)(Session=RAW))
Services Summary...
Service "86b637b62fdf7a65e053f706e80a27ca" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s) for this service...
Service "dff5f5f5653e282de055edcb06fe117c" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s) for this service...
Service "orcl" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s) for this service...
Service "orclXDB" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s) for this service...
Service "pdb1" has 1 instance(s).
  Instance "orcl", status READY, has 1 handler(s) for this service...
The command completed successfully
```

https://blog.csdn.net/congjiao2376/article/details/100419283?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-100419283-blog-101862797.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-100419283-blog-101862797.pc_relevant_antiscanv2&utm_relevant_index=5


connect string for sid:

```
(DESCRIPTION =
 (ADDRESS = (PROTOCOL = TCP)(HOST =127.0.0.1)(PORT = 1522)
  )
 (CONNECT_DATA =
  (SID= orcl)
```


session,progress:

http://blog.itpub.net/21416913/viewspace-743930/

```
```


https://blog.csdn.net/eussi/article/details/79054708


ORA-00845: MEMORY_TARGET not supported on this system
```bash
mount -o remount,size=1G /dev/shm

#edit /etc/fstab
tmpfs /dev/shm tmpfs defaults,size=1G 0 0
mount –o remount  /dev/shm

sqlplus / as sysdba
SQL> startup nomount
SQL> alter system set memory_target=495M scope=both;
```

create new user can't login:
name can wrap with "",example: "c##test"

https://blog.csdn.net/weixin_44238730/article/details/123493315?spm=1001.2101.3001.6650.11&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-123493315-blog-90690816.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-123493315-blog-90690816.pc_relevant_antiscanv2&utm_relevant_index=14


```sql
grant all on sys.app_user to "c##test2";

```
monitor sql:
```sql
select inst_id,username,status,count(*) from gv$session group by inst_id,username,status order by 3,4;

select SNAP_ID,
       DBID,
       to_char(BEGIN_INTERVAL_TIME, 'yyyy-mm-dd hh24:mi:ss'),
       to_char(END_INTERVAL_TIME, 'yyyy-mm-dd hh24:mi:ss'),
       FLUSH_ELAPSED,
       SNAP_LEVEL
  from dba_hist_snapshot order by 1;

  select a.sql_id,
       a.module,
       a.elap,
       a.exec,
       decode(a.exec, 0, to_number(null), (a.elap / a.exec)) elap_one,
       b.sql_text
  from dba_hist_sqltext b,
       (select sql_id,
               max(module) module,
               sum(elapsed_time_delta) / 1000000 elap,
               sum(executions_delta) exec
          from dba_hist_sqlstat
         where dbid = 1634419405
           and instance_number = 1
          -- and 6504 < snap_id
          -- and snap_id <= 6528
         group by sql_id) a
 where a.sql_id = b.sql_id
 order by elap desc;
```
http://blog.itpub.net/29785807/viewspace-2156502/




dba:

http://blog.itpub.net/29785807/viewspace-2874066/


rac:
http://blog.itpub.net/29785807/viewspace-2864667/


1、user_*：当前用户所有的对象；
2、all_*：当前用户可以访问的对象;
3、dba_*：数据库中所有的对象

http://www.itpub.net/thread-2096851-1-1.html