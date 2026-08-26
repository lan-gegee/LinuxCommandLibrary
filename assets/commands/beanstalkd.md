# TAGLINE

简单快速的工作队列服务器

# TLDR

在默认端口**启动 beanstalkd**

```beanstalkd```

在指定地址和端口**启动**

```beanstalkd -l [127.0.0.1] -p [11300]```

以持久化存储方式**运行**（binlog）

```beanstalkd -b [/var/lib/beanstalkd]```

**以特定用户身份运行**（放弃特权）

```beanstalkd -u [beanstalkd]```

**设置最大作业大小**

```beanstalkd -z [65535]```

以详细模式**启动**（-VV 可获得更多信息）

```beanstalkd -V```

**打印版本**并退出

```beanstalkd -v```

# SYNOPSIS

**beanstalkd** [_-l addr_] [_-p port_] [_-u user_] [_-z bytes_] [_-b path_] [_-V_] [_-h_]

# DESCRIPTION

**beanstalkd** 是一个简单、快速的工作队列服务器。它提供了管理作业队列的通用接口，最初的设计目的是通过异步执行耗时的任务来降低高流量 Web 应用的延迟。

生产者将作业推入队列，工作者（消费者）取出（reserve）作业进行处理。协议支持作业优先级、延迟、最长运行时间限制以及多个命名管道（tube，即队列）。

# PARAMETERS

**-l** _addr_
> 监听地址（IP 或 0.0.0.0 表示所有接口）。默认：0.0.0.0

**-p** _port_
> 监听的 TCP 端口。默认：11300

**-u** _user_
> 绑定端口后放弃特权，以指定用户运行

**-z** _bytes_
> 最大作业大小（字节）。默认：65535（64KB）

**-b** _path_
> 启用 binlog，将作业持久化到指定目录

**-f** _ms_
> 每 ms 毫秒将 binlog 同步到磁盘一次（默认 50ms，0 表示每次写入都同步）

**-s** _bytes_
> binlog 文件的最大大小（字节）。默认：10485760（10MB）

**-v**
> 打印版本并退出

**-V**
> 提高输出详细程度。一次为基本日志，两次（-VV）为详细日志

**-h**
> 打印包含可用选项的帮助消息

# CAVEATS

默认情况下，beanstalkd 将所有作业存储在内存中；重启会丢失全部排队作业，除非启用了 **-b** binlog。没有内置的身份验证机制；请通过防火墙规则保护访问，或只绑定到 localhost。超过最大大小（**-z**）的作业会被拒绝。

# HISTORY

Beanstalkd 由 **Keith Rarick** 于 **2007** 年在 Causes.com 创建，用于处理后台作业。它作为更重的消息队列系统的轻量替代品而广受欢迎，以其简洁性和亚毫秒级延迟著称。

# INSTALL

```apt: sudo apt install beanstalkd```

```dnf: sudo dnf install beanstalkd```

```aur: yay -S beanstalkd```

```apk: sudo apk add beanstalkd```

```brew: brew install beanstalkd```

```nix: nix profile install nixpkgs#beanstalkd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[redis-server](/man/redis-server)(1), [rabbitmq-server](/man/rabbitmq-server)(1), [memcached](/man/memcached)(1)
