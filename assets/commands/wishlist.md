# TAGLINE

SSH 目录与主机浏览器

# TLDR

以默认设置**启动 SSH 目录**

```wishlist```

使用指定的**配置文件**启动

```wishlist -c [config.yaml]```

**监听特定端口**

```wishlist -p [2222]```

以指定的监听地址启动

```wishlist -l [0.0.0.0:2222]```

# SYNOPSIS

**wishlist** [_-c config_] [_-p port_] [_-l address_] [_options_]

# PARAMETERS

**-c** _FILE_
> YAML 配置文件的路径。

**-l** _ADDRESS_
> 要绑定的监听地址（如 0.0.0.0:2222）。

**-p** _PORT_
> 监听端口（默认：22）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**wishlist** 是一个 SSH 目录，提供终端用户界面来浏览和连接已配置的 SSH 主机。它呈现一个可搜索的可用服务器菜单，无需记住主机名或输入完整的 SSH 命令即可快速选择并连接。

主机在一个 YAML 配置文件中定义，包含主机名、端口和用户等连接信息。该工具属于 Charm 生态，本身也作为 SSH 服务器运行，这意味着用户可以从任何机器通过 SSH 连接到 wishlist 来访问自己的主机目录。

# CAVEATS

需要配置。Charm Labs 出品。Go 实现。

# HISTORY

**wishlist** 是 **Charm** 生态的一部分，提供便于访问主机的 SSH 目录。

# INSTALL

```pacman: sudo pacman -S wishlist```

```brew: brew install wishlist```

```nix: nix profile install nixpkgs#wishlist```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [sshd](/man/sshd)(8), [tmux](/man/tmux)(1)
