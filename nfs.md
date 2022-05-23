---
layout: default
---

### nfs

server:

``` bash
sudo apt-get install nfs-kernel-server
sudo cat /etc/exports
/nfs *(rw,sync,no_roo_squash)

sudo mkdir /nfs
sudo chmod -R 777 /nfs
sudo chown -R vinson:vinson /nfs
sudo /etc/init.d/nfs-kernel-server restart
```

client:
``` bash
sudo apt-get install nfs-common
sudo mount -t nfs ip:/nfs /mnt -o nolock

#edit /etc/fstab
ip:/nfs /mnt nfs rw 0 0

```

MacOs:

```bash

❯ cat /etc/exports
/Users/xxxx/Documents -alldirs -maproot=root:wheel -network 192.168.31.0 -mask 255.255.255.0

sudo nfsd disable
sudo nfsd enable
sudo nfsd stop
sudo nfsd start
sudo nfsd status
mount -t nfs -o nolock 192.168.31.35:/Users/xxxx/Documents /home


showmount -e ip

sudo mount -t nfs -o resvport  ip:/nfs nfs
#or
sudo mount_ntfs -P ip:/nfs nfs

#-P=-o resvport
```