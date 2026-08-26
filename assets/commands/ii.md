# TAGLINE

极简的基于文件系统的 IRC 客户端

# TLDR

**连接 IRC 服务器**

```ii -s [irc.libera.chat] -n [nickname]```

**指定端口连接**

```ii -s [irc.libera.chat] -p [6697] -n [nickname]```

**指定 IRC 目录**

```ii -s [server] -i [~/.irc] -n [nickname]```

**加入频道**

```echo "/j #channel" > ~/irc/server/in```

**发送消息**

```echo "Hello world" > ~/irc/server/#channel/in```

# SYNOPSIS

**ii** [_options_]

# PARAMETERS

**-s** _server_
> IRC 服务器地址。

**-p** _port_
> 服务器端口（默认 6667）。

**-n** _nickname_
> IRC 昵称（默认为 $USER）。

**-k** _env_var_
> 保存 IRC 密码的环境变量（避免在命令行上暴露密码）。

**-f** _fullname_
> 真实姓名（GECOS 字段）。

**-i** _prefix_
> IRC 目录前缀（默认 ~/irc）。

**-t**
> 使用 TLS 连接。

**-v**
> 不验证 TLS 证书。

**-4**
> 仅通过 IPv4 连接。

**-6**
> 仅通过 IPv6 连接。

**-u** _socket_
> 连接到 UNIX 域套接字而不是网络服务器。

# DESCRIPTION

**ii**（IRC It）是一个极简的基于文件系统的 IRC 客户端。它会创建一个目录结构，每个服务器和频道都是一个目录，其中包含 **in** 文件（写入以发送）和 **out** 文件（读取消息）。

这种设计遵循 Unix 哲学，允许通过标准文件操作和 shell 脚本与 IRC 交互。它可以与 tail、cat 及自定义脚本等工具结合使用。

# DIRECTORY STRUCTURE

```
~/irc/
└── irc.libera.chat/
    ├── in          # Send commands
    ├── out         # Server messages
    └── #channel/
        ├── in      # Send to channel
        └── out     # Channel messages
```

# USAGE

```bash
# Monitor channel
tail -f ~/irc/server/#channel/out

# Join channel
echo "/j #linux" > ~/irc/server/in

# Send message
echo "Hello!" > ~/irc/server/#channel/in
```

# CAVEATS

没有内置界面；需要脚本或其他工具。不借助包装器则不支持 SSL。功能有限。频道/昵称需手动管理。

# HISTORY

ii 是 **suckless** 项目的一部分，秉承其极简、基于文件系统的工具哲学。它展示了 IRC 可以仅靠标准 Unix 文件操作工作。

# INSTALL

```apt: sudo apt install ii```

```dnf: sudo dnf install ii```

```apk: sudo apk add ii```

```brew: brew install ii```

```nix: nix profile install nixpkgs#ii```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1), [sic](/man/sic)(1)
