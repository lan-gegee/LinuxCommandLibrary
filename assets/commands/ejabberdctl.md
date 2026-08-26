# TAGLINE

ejabberd XMPP 服务器控制工具

# TLDR

**启动 ejabberd 服务器**

```sudo ejabberdctl start```

**停止 ejabberd 服务器**

```sudo ejabberdctl stop```

**检查服务器状态**

```ejabberdctl status```

**注册新用户**

```ejabberdctl register [user] [domain] [password]```

**注销用户**

```ejabberdctl unregister [user] [domain]```

**列出已注册用户**

```ejabberdctl registered_users [domain]```

**重启服务器**

```sudo ejabberdctl restart```

# SYNOPSIS

**ejabberdctl** [_options_] _command_ [_args_]

# PARAMETERS

**start**
> 启动 ejabberd 服务器。

**stop**
> 停止 ejabberd 服务器。

**restart**
> 重启 ejabberd 服务器。

**status**
> 显示服务器状态。

**register** _user_ _host_ _password_
> 注册新用户。

**unregister** _user_ _host_
> 移除用户。

**registered_users** _host_
> 列出主机上的用户。

**connected_users**
> 列出在线用户。

**kick_user** _user_ _host_
> 断开用户连接。

**reload_config**
> 重新加载配置。

**backup** _file_
> 备份数据库。

**restore** _file_
> 恢复数据库。

# CONFIGURATION

**/etc/ejabberd/ejabberd.yml**
> ejabberd 的主配置文件，控制服务器行为、虚拟主机和模块。

# DESCRIPTION

**ejabberdctl** 是 ejabberd（开源 XMPP/Jabber 即时通讯服务器）的命令行管理工具。它管理服务器操作、用户账户和配置。

该工具通过 Erlang RPC 与正在运行的 ejabberd 节点通信，无需访问 Web 界面即可进行管理。它支持 Web 管理界面提供的所有管理功能。

# CAVEATS

需要安装并配置好 ejabberd。某些命令需要 root 权限。大多数命令要求服务器正在运行。数据库变更可能需要重启才能生效。Erlang 环境必须正确配置。

# HISTORY

ejabberd 由 **Alexey Shchepin** 自 **2002 年**起开发，用 Erlang 编写以获得可扩展性和容错能力。它已成为部署最广泛的 XMPP 服务器之一，被 WhatsApp 及其他消息平台大规模使用。

# INSTALL

```apt: sudo apt install ejabberd```

```pacman: sudo pacman -S ejabberd```

```apk: sudo apk add ejabberd```

```brew: brew install ejabberd```

```nix: nix profile install nixpkgs#ejabberd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prosodyctl](/man/prosodyctl)(1)
