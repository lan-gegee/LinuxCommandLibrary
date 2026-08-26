# TAGLINE

通过局域网点对点方式复制文件

# TLDR

将文件/目录**复制**到另一台运行 pcp 的机器

```pcp [path]```

**接收**/等待传入的复制请求（对等模式）

```pcp```

自动发现失败时**显式指定**对端

```pcp --peer [host] [path]```

# SYNOPSIS

**pcp** [*options*] [*path*]

# DESCRIPTION

**pcp**（peer copy）在局域网内的机器之间传输文件，使用对等发现机制，无需像 scp 那样提供主机名和密钥，适合日常临时复制。一端广播并接收；另一端推送路径。使用 Go 实现；可通过 **go install**、Homebrew 或 **dennis-tra/pcp** 的发布版本安装。

与 Performance Co-Pilot 工具集（同样缩写为 PCP）无关。

# PARAMETERS

*path*

> 要发送的文件或目录。

**--peer** *address*

> mDNS/发现机制不可用时使用的目标对端。

**-h**, **--help**

> 查看完整选项列表（端口、代码、界面）。

# CAVEATS

面向可信的本地网络设计——在不了解威胁模型的情况下，不要在不受信任的链路上暴露。防火墙/mDNS 限制可能阻碍发现。在某些系统上与 Performance Co-Pilot 的命令重名。

# INSTALL

```apt: sudo apt install pcp```

```dnf: sudo dnf install pcp```

```pacman: sudo pacman -S pcp```

```zypper: sudo zypper install pcp```

```brew: brew install pcp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [rsync](/man/rsync)(1), [croc](/man/croc)(1), [magic-wormhole](/man/magic-wormhole)(1)

# RESOURCES

```[Source code](https://github.com/dennis-tra/pcp)```

<!-- verified: 2026-07-19 -->
