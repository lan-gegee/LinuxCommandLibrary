# 用户与组

## 创建用户
**useradd** 是底层工具：加 **-m** 创建主目录，加 **-s** 设置登录 Shell。在基于 Debian 的系统上，**adduser** 是更友好的交互式前端。所有用户和组管理操作都需要 root 权限。
```[useradd](/man/useradd) -m -s /bin/bash [name]```
```[adduser](/man/adduser) [name]```
```[passwd](/man/passwd) [name]```

只用 **useradd [name]** 创建的账户没有主目录，对真实用户来说这很少是你想要的结果。

## 删除与重命名用户
**-r** 还会删除用户的主目录和邮件池。
```[userdel](/man/userdel) [name]```
```[userdel](/man/userdel) -r [name]```
```[deluser](/man/deluser) [name]```
```[usermod](/man/usermod) -l [newUsername] [oldUsername]```

## 修改用户
更改用户的 Shell、主目录或注释字段。
```[usermod](/man/usermod) -s /bin/zsh [name]```
```[chsh](/man/chsh) -s /bin/zsh [name]```
```[usermod](/man/usermod) -d /new/home -m [name]```

锁定账户（禁用密码登录），以及重新解锁。
```[usermod](/man/usermod) -L [name]```
```[usermod](/man/usermod) -U [name]```

强制下次登录时修改密码，或查看密码时效信息。
```[passwd](/man/passwd) -e [name]```
```[chage](/man/chage) -l [name]```

## 组
创建、重命名和删除组。
```[groupadd](/man/groupadd) [name]```
```[groupmod](/man/groupmod) -n [newGroupname] [oldGroupname]```
```[groupdel](/man/groupdel) [name]```

将现有用户加入组。**-aG** 中的 **-a** 至关重要：没有它，用户会被从所有其他附加组中移除。
```[usermod](/man/usermod) -aG [groupName] [userName]```
```[gpasswd](/man/gpasswd) -a [userName] [groupName]```
```[adduser](/man/adduser) [userName] [groupName]```

将用户从组中移除。
```[gpasswd](/man/gpasswd) -d [userName] [groupName]```
```[deluser](/man/deluser) [userName] [groupName]```

组变更在下一次登录时生效。用 **newgrp [groupName]** 可以不注销就在当前 Shell 中激活某个组。

## 授予 sudo
加入管理员组即可获得 sudo 权限：Debian/Ubuntu 上该组是 **sudo**，Fedora、RHEL 和 Arch 上是 **wheel**。
```[usermod](/man/usermod) -aG sudo [user]```
```[usermod](/man/usermod) -aG wheel [user]```

编辑 sudoers 文件务必只用 **visudo**，它会在保存前检查语法（sudoers 文件损坏可能把你锁在系统之外）。
```[visudo](/man/visudo)```

## 列出用户与组
**getent** 会查询所有账户数据库，包括 LDAP 和其他网络来源；/etc 下的文件只显示本地账户。
```[getent](/man/getent) passwd```
```[getent](/man/getent) group```
```[cat](/man/cat) /etc/passwd```
```[cat](/man/cat) /etc/group```

## 我是谁，谁在这里
显示当前用户及其 ID 和所属组，以及任意用户的组。
```[whoami](/man/whoami)```
```[id](/man/id) [user]```
```[groups](/man/groups) [user]```

查看谁已登录、他们在做什么，以及登录历史。
```[who](/man/who)```
```[w](/man/w)```
```[last](/man/last)```

## 切换用户
**su -** 以另一个用户的身份启动完整的登录 Shell（不给名字则为 root）；**sudo -i** 通过 sudo 打开 root Shell。
```[su](/man/su) - [user]```
```[sudo](/man/sudo) -i```
```[sudo](/man/sudo) -u [user] [command]```
