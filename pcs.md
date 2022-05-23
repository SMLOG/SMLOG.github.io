---
layout: default
---

### pcs


https://www.linuxprobe.com/centos7-high-availability-cluster.html

https://www.golinuxcloud.com/configure-ha-lvm-cluster-resource-linux/

``` bash

service network restart

hostnamectl --static set-hostname node2
systemctl stop firewalld.service
systemctl disable firewalld

# firewall-cmd --permanent --add-service=high-availability
#firewall-cmd --reload

yum -y install corosync pacemaker pcs
systemctl start pcsd && systemctl enable pcsd

passwd hacluster

pcs cluster auth node1 node2 -u hacluster

pcs cluster setup --name test node1 node2
pcs cluster start --all
pcs cluster enable --all

pcs resource create vip ocf:heartbeat:IPaddr2 ip=192.168.0.200 cidr_netmask=24 op monitor interval=30s

pcs property set stonith-enabled=false

crm_verify -L

https://192.168.0.202:2224/
```
