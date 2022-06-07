---
layout: default
---

### centos
[download CentOS-X-X86_64-MIMIMAL](https://www.centos.org/download/)

#rsync
```
rsync -av -e "ssh -i (key position) -p ****"  user@remote:/source destination 

rsync -e "ssh -i (key position) -p ****" -r local source/ user@remote:/destination
```

top:
```
top -p pid
top -d seconds
```
https://www.yingsoo.com/news/posts/61997.html

https://blog.csdn.net/qq_40907977/article/details/102608593

