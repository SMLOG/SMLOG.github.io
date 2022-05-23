---
layout: default
---

### ssh

.ssh/config proxy setting
```bash 
Host *github.com
    ProxyCommand connect -H proxyIP:port %h %p
    ServerAliveInterval 30
```
or with ssh -o "ProxyCommand="

```bash
/bin/su -c '/usr/bin/autossh -M 5678 -NR 1234:localhost:2223 user1@123.123.123.123 -p2221' - user1
```

[SSH反向连接及Autossh](https://www.cnblogs.com/eshizhan/archive/2012/07/16/2592902.html)