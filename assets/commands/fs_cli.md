# TAGLINE

FreeSWITCH 命令行界面

# TLDR

以交互会话连接到**本地 FreeSWITCH** 实例

```fs_cli```

连接到**远程 FreeSWITCH** 服务器

```fs_cli -H [host] -P [port] -p [password]```

执行**单条命令**后退出

```fs_cli -x "[command]"```

显示 FreeSWITCH **系统状态**

```fs_cli -x "status"```

**重载** FreeSWITCH XML 配置

```fs_cli -x "reloadxml"```

检查某个**模块是否已加载**

```fs_cli -x "module_exists [module_name]"```

显示**当前通话**

```fs_cli -x "show calls"```

连接失败时**重试**

```fs_cli -r```

# SYNOPSIS

**fs_cli** [_options_]

# PARAMETERS

**-H**, **--host** _HOST_
> 连接到位于 _HOST_ 的远程 FreeSWITCH 服务器。

**-P**, **--port** _PORT_
> 连接到 _PORT_ 上的 Event Socket（默认：8021）。

**-p**, **--password** _PASSWORD_
> Event Socket 密码（默认：ClueCon）。

**-x**, **--execute** _COMMAND_
> 执行命令并退出。

**-r**, **--retry**
> 连接失败时重试。

**-l**, **--loglevel** _LEVEL_
> 设置日志级别（0-7）。

**-q**, **--quiet**
> 禁用向控制台输出日志。

**-d**, **--debug** _LEVEL_
> 调试级别（0-7）。

# CONFIGURATION

**/etc/freeswitch/autoload_configs/event_socket.conf.xml**
> Event Socket Layer 配置，控制 ESL 连接的监听地址、端口和认证密码。

# DESCRIPTION

**fs_cli** 是 FreeSWITCH 的命令行界面客户端，通过 Event Socket Layer（ESL）连接到正在运行的 FreeSWITCH 服务器。它提供对 FreeSWITCH API 的交互式访问，用于管理通话、配置和系统状态。

该工具可以在交互模式下实时控制，也可以通过 **-x** 选项执行单条命令以用于脚本和自动化。它使用配置的凭据连接 ESL 端口（默认 8021）。

常见操作包括查看通话状态、重载配置、管理通道以及监控系统健康状况。

# CAVEATS

需要在 FreeSWITCH 中加载并正确配置 Event Socket 模块。生产环境中应修改默认密码 "ClueCon"。必须妥善保护 ESL 端口的网络访问。

# HISTORY

fs_cli 是 FreeSWITCH 项目的一部分。FreeSWITCH 是由 Anthony Minessale II 于 **2006** 年发起的开源通信平台，旨在作为构建电话应用的现代化、可扩展的 Asterisk 替代方案。

# INSTALL

```apk: sudo apk add freeswitch```

```brew: brew install freeswitch```

```nix: nix profile install nixpkgs#freeswitch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[asterisk](/man/asterisk)(8)
