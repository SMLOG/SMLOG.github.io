---
layout: default
---


edit /etc/sysconfig/network-scripts/ifcfg-enp0s3

change "ONBOOT=no" to "ONBOOT=yes"

### oracle 19c

[download](https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html)

create group
```bash
[root@localhost ~]# groupadd oinstall
[root@localhost ~]# groupadd dba
[root@localhost ~]# groupadd asmdba
[root@localhost ~]# groupadd backupdba
[root@localhost ~]# groupadd dgdba
[root@localhost ~]# groupadd kmdba
[root@localhost ~]# groupadd racdba
[root@localhost ~]# groupadd oper

[root@localhost ~]# useradd -g oinstall -G dba,asmdba,backupdba,dgdba,kmdba,racdba,oper oracle
[root@localhost ~]# passwd  oracle

[root@localhost ~]# mkdir -p /u01/app/oracle/product/19c/db_1
# mkdir -p /u01/app/oraInventory
[root@localhost ~]# chown -R oracle:oinstall /u01/app
# chmod -R 775 /u01/*
[root@localhost usr]# mkdir -p /usr/swap

[root@localhost usr]# cd /usr/swap/

[root@localhost swap]# dd if=/dev/zero of=swapfile bs=200M count=5

[root@localhost swap]# mkswap /usr/swap/swapfile

[root@localhost swap]# swapon /usr/swap/swapfile

[root@localhost swap]# free -h

#add below line to /etc/fstab

/usr/swap/swapfile swap swap defaults 0 

[root@localhost ~]# su - oracle

[oracle@localhost ~]$ vi .bash_profile

export ORACLE_HOME=/u01/app/oracle/product/19c/db_1
export PATH=$PATH:/u01/app/oracle/product/19c/db_1/bin
export ORACLE_SID=orcl

[oracle@localhost ~]$ source .bash_profile

[oracle@localhost db_1]$ unzip -d /u01/app/oracle/product/19c LINUX.X64_193000_db_home.zip


systemctl stop firewalld.service
systemctl disable firewalld.service
systemctl status firewalld.service

sed -i s'\enforcing\disable\g' /etc/selinux/config

yum install bc binutils  compat-libcap1  compat-libstdc++33  elfutils-libelf  elfutils-libelf-devel  fontconfig-devel  glibc  glibc-devel  ksh  libaio  libaio-devel  libX11  libXau  libXi  libXtst  libXrender  libXrender-devel  libgcc  libstdc++  libstdc++-devel  libxcb  make  smartmontools  sysstat  kmod*

#yum -y install xdpyinfo
#[root@localhost lib]# dnf install libnsl
[oracle@localhost 19c]./runInstaller


```



[refer link1](https://blog.csdn.net/okc_champion/article/details/117899030?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-117899030-blog-119835073.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-117899030-blog-119835073.pc_relevant_paycolumn_v3&utm_relevant_index=11)
[link2](https://oracledbwr.com/step-by-step-oracle-19c-installation-on-linux/)
[link3](https://blog.csdn.net/weixin_49080355/article/details/119835073)

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

```