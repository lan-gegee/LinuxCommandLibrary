# TAGLINE

极简命令行 IRC 客户端

# TLDR

使用来自 $USER 的用户名连接**默认服务器**

```sic```

连接到**特定主机**并指定昵称

```sic -h [host] -n [nickname]```

以**密码**认证方式连接

```sic -h [host] -n [nickname] -k [password]```

连接到指定的**端口**

```sic -h [host] -p [port] -n [nickname]```

# SYNOPSIS

**sic** [**-h** _host_] [**-p** _port_] [**-n** _nick_] [**-k** _keyword_] [**-v**]

# PARAMETERS

**-h** _host_
> 服务器主机名（默认：**irc.oftc.net**）。

**-p** _port_
> 服务器端口（默认：6667）

**-n** _nickname_
> 客户端昵称（默认为 $USER 环境变量）

**-k** _keyword_
> 用于昵称注册/认证的密码

**-v**
> 显示版本信息并退出

# COMMANDS

**:j #channel**
> 加入频道

**:l #channel**
> 离开频道

**:m #channel|user message**
> 向频道或用户发送消息

**:s #channel|user**
> 设置消息默认发送到的活动频道/用户。

**: COMMAND**
> 任何以 **:** 开头的行都会原样作为原始 IRC 命令发送给服务器（例如 **:TOPIC #chan :new topic**）。

**text without colon**
> 作为消息发送给通过 **:s** 设置的当前活动目标。

# DESCRIPTION

**sic**（simple IRC client）是 suckless 项目推出的极简 IRC 客户端。它从标准输入读取命令，并将所有服务器响应输出到标准输出。所有频道的流量都被复用到单一流中，而不是为每个频道使用独立的缓冲区。

该客户端遵循 suckless 的简洁与极简哲学，只提供最核心的 IRC 功能。它被设计为可以通过管道和 shell 脚本与其他 Unix 工具组合，实现扩展功能。

# CAVEATS

没有内置的频道分离；所有消息都出现在同一流中。没有回滚或历史缓冲。不支持颜色和格式。适合熟悉命令行界面和 Unix 管道的高级用户。建议搭配 **tmux** 或 **screen** 等工具使用以获得更好的会话管理。

# HISTORY

**sic** 由 **suckless.org** 社区开发，该社区以 **dwm** 和 **st** 等极简软件闻名。suckless 哲学强调简单、清晰和节俭，打造把一件事做好并通过 Unix 管道集成的工具。该项目自 **2000 年代中期**以来一直活跃。

# INSTALL

```apt: sudo apt install sic```

```apk: sudo apk add sic```

```brew: brew install sic```

```nix: nix profile install nixpkgs#sic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1), [ii](/man/ii)(1)
