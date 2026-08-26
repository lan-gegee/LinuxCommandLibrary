# TAGLINE

Docker 守护进程后台服务

# TLDR

运行 Docker **守护进程**

```dockerd```

监听**指定的套接字**

```dockerd -H unix://[path/to/tmp.sock] -H tcp://[ip_address]```

指定 **PID 文件**

```dockerd -p [path/to/pid_file]```

以**调试模式**运行

```dockerd -D```

设置**日志级别**

```dockerd -l [debug|info|warn|error|fatal]```

# SYNOPSIS

**dockerd** [_options_]

# DESCRIPTION

**dockerd** 是 Docker 守护进程，负责管理容器、镜像、网络和卷。它是一个持久运行的后台服务，监听 Docker API 请求。

通常由 systemd 管理，而不是直接运行。

# PARAMETERS

**-H, --host** _socket_
> 要监听的套接字（unix://、tcp://、fd://）

**-p, --pidfile** _file_
> PID 文件路径

**-D, --debug**
> 启用调试模式

**-l, --log-level** _level_
> 日志级别

**--storage-driver** _driver_
> 存储驱动（overlay2、devicemapper 等）

**--data-root** _path_
> Docker 数据的根目录（默认 /var/lib/docker）。

**--tls**, **--tlsverify**
> 使用 TLS（并验证远程证书）。

**--tlscert** _file_, **--tlskey** _file_, **--tlscacert** _file_
> 用于安全守护进程连接的 TLS 证书、密钥和受信任 CA。

**--userland-proxy**=_true|false_
> 为发布端口的回环流量启用 userland-proxy。

**--live-restore**
> 守护进程停机期间保持容器存活。

# CONFIGURATION

**/etc/docker/daemon.json**
> Docker 守护进程的主配置文件，控制存储驱动、日志、网络、镜像仓库加速器和运行时设置。

# CAVEATS

需要 root 权限或正确的组成员身份。通常通过 /etc/docker/daemon.json 进行配置。不使用 TLS 暴露 TCP 套接字是不安全的。

# INSTALL

```apt: sudo apt install docker.io```

```apk: sudo apk add docker-engine```

```brew: brew install docker-engine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [systemctl](/man/systemctl)(1), [containerd](/man/containerd)(8)
