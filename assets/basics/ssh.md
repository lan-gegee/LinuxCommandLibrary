# SSH

## 连接
以某个用户的身份连接远程主机，可选指定非标准端口；也可以只执行一条命令后返回。
```[ssh](/man/ssh) [user]@[host]```
```[ssh](/man/ssh) -p 2222 [user]@[host]```
```[ssh](/man/ssh) [user]@[host] [command]```

用 **exit**、**logout** 或 **Ctrl+d** 结束会话。

首次连接主机时，SSH 会显示其密钥指纹并存入 ~/.ssh/known_hosts。之后若突然出现“主机密钥已变更”警告，说明服务器可能被重装过，或者有人正在截获该连接。

如果会话失去响应（网络中断），输入 **Enter ~ .** 强制关闭它。

## 密钥与免密登录
生成密钥对；**ed25519** 是现代默认选择（仅当老旧服务器要求 RSA 时才使用 **-t rsa -b 4096**）。私钥留在你自己的机器上，公钥放到服务器上。
```[ssh-keygen](/man/ssh-keygen) -t ed25519```
```[ssh-keygen](/man/ssh-keygen) -t rsa -b 4096```

把公钥安装到服务器上，之后即可免密码登录。
```[ssh-copy-id](/man/ssh-copy-id) [user]@[host]```
```[ssh](/man/ssh) -i [keyFile] [user]@[host]```

Agent 会把解密后的密钥保存在内存中，因此受口令保护的密钥每个会话只需解锁一次。
```[ssh-add](/man/ssh-add)```
```[ssh-add](/man/ssh-add) -l```

**务必用口令保护私钥**，并把 ~/.ssh/id_ed25519 的权限模式保持为 **600**。可以安全分享的是 .pub 文件。

## 客户端配置
连接设置保存在 **~/.ssh/config** 中，每台主机一个配置块。此后，一条 **ssh myserver** 即可替代完整的用户名/主机/端口/密钥长串参数，而且 Tab 补全也能识别这个别名。
```
Host myserver
    HostName server.example.com
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```
```[ssh](/man/ssh) myserver```

## 传输文件
**scp** 复制文件和目录（**-r**）；**rsync** 同样能做到，但支持断点续传且只传输差异部分，更适合大型或重复性的传输。
```[scp](/man/scp) [localFile] [user]@[host]:[remotePath]```
```[scp](/man/scp) [user]@[host]:[remoteFile] .```
```[scp](/man/scp) -r [localDir] [user]@[host]:[remoteDir]```
```[rsync](/man/rsync) -avz [localDir]/ [user]@[host]:[remoteDir]/```

**sftp** 提供交互式会话，支持 **get**、**put**、**ls** 和 **cd**；**sshfs** 可把远程目录挂载得像本地磁盘一样。
```[sftp](/man/sftp) [user]@[host]```
```[sshfs](/man/sshfs) [user]@[host]:[remoteDir] [localDir]```
```fusermount -u [localDir]```

## 端口转发
**-L** 让远程服务可在本地访问：示例把运行在服务器 localhost:5432 上的数据库暴露到你本地的 localhost:5432。**-N** 只建立隧道而不启动 Shell。
```[ssh](/man/ssh) -L 5432:localhost:5432 [user]@[host]```
```[ssh](/man/ssh) -N -L 8080:internal-host:80 [user]@[gateway]```

**-R** 则相反：远程服务器上的一个端口转发到你的机器。
```[ssh](/man/ssh) -R 8080:localhost:3000 [user]@[host]```

**-D** 把连接变成 SOCKS5 代理；把浏览器指向 localhost:9999，其流量就会经由该服务器转发。
```[ssh](/man/ssh) -D 9999 [user]@[host]```

## 跳板机与 X11
用 **-J** 经由堡垒机访问只能通过它才能到达的机器，并用 **-X** 在连接上运行图形程序。
```[ssh](/man/ssh) -J [user]@[bastion] [user]@[internalHost]```
```[ssh](/man/ssh) -X [user]@[host]```

## 保持会话活跃
发送保活数据包，让空闲连接不被 NAT 超时中断；可在 ~/.ssh/config 中按主机或全局设置。
```
Host *
    ServerAliveInterval 60
```

对于必须在中断后仍继续的任务，在服务器上运行 **tmux**：重新连接后再接入会话，你的程序仍在运行（参见 Tmux 基础页面）。
