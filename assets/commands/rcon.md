# TAGLINE

命令行 Source RCON 客户端

# TLDR

**发送单条命令**

```rcon -H [host] -p [port] -P [password] status```

**含多个单词的服务器命令**

```rcon -H [host] -p [port] -P [password] sm plugins list```

**从 stdin 读取命令**

```rcon -H [host] -p [port] -P [password] <<EOF
status
sm plugins list
EOF```

**使用保存的服务器配置档**

```rcon -s [profile] status```

**使用其他配置文件**

```rcon -c [~/.rconrc] -s [profile] status```

# SYNOPSIS

**rcon** **-H** *host* **-p** *port* **-P** *password* [*command*...]
**rcon** **-s** *profile* [*command*...]

# DESCRIPTION

**rcon** 是一款命令行 Source RCON 客户端。它向暴露了 Source RCON 协议的游戏服务器发送命令，并将应答打印到 stdout。选项之后的额外 argv 单词会被拼接成一条服务器命令。如果 argv 中没有给出命令，则从 stdin 逐行读取（以 **#** 开头的行视为注释），因此可以运行脚本文件。

使用 CMake 构建（需要 **libbsd**、**check**、**glib-2.0**）。可通过 **INSTALL_BASH_COMPLETION=ON** 获得可选的 bash 补全。多个平台都有软件包（参见 repology）。

# PARAMETERS

**-H** *host*

> 服务器主机名或 IP。

**-p** *port*

> RCON 端口。

**-P** *password*

> RCON 密码。

**-s** *profile*

> 配置文件中的命名服务器条目。

**-c** *file*

> 配置文件路径（默认 **$HOME/.rconrc**）。

*command*...

> 服务器命令单词（会被拼接在一起）。省略则从 stdin 读取命令。

# CONFIGURATION

默认配置文件为 **$HOME/.rconrc**。在其中定义服务器配置档（主机、端口、密码），然后用 **-s** 选择。由于凭据以明文存储，建议收紧文件权限（**chmod 600**）。

# CAVEATS

RCON 未加密；密码将以明文在网络中传输。请只在可信网络或隧道中使用。成功时退出码为 0，失败时为非零。与 Redis 及 Source 引擎游戏之外其他名为 "RCON" 的协议无关。

# SEE ALSO

[mcrcon](/man/mcrcon)(1), [netcat](/man/netcat)(1)

# RESOURCES

```[Source code](https://github.com/n0la/rcon)```

<!-- verified: 2026-07-19 -->

# INSTALL

```apk: sudo apk add rcon```

```nix: nix profile install nixpkgs#rcon```

<!-- packages: 2026-07-22 -->
