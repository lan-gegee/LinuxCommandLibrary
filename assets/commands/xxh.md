# TAGLINE

基于 SSH 的便携 Shell 环境

# TLDR

**用你的便携 shell 连接主机**

```xxh [hostname]```

**使用特定 shell 连接**

```xxh [hostname] +s [zsh]```

**带 SSH 参数连接**

```xxh -i [~/.ssh/id_rsa] -p [2222] [hostname]```

首次连接时**静默安装 shell**

```xxh [hostname] +s [fish] +i```

连接前**安装插件**

```xxh [hostname] +I [xxh-plugin-zsh-ohmyzsh]```

**以密封模式连接**（隔离 home 目录）

```xxh [hostname] +hh```

**列出可用 shell**

```xxh +LS```

**从远程主机移除 xxh**

```xxh [hostname] +hc```

# SYNOPSIS

**xxh** [_ssh_options_] _host_ [**+s** _shell_] [**+i**] [**+I** _plugin_] [**+hh**]

# PARAMETERS

**+s**, **+shell** _shell_
> 指定要使用的 shell（zsh、bash、fish、xonsh、osquery）

**+i**, **+install**
> 安装 shell 且不弹出确认提示

**+I**, **+install-plugin** _plugin_
> 连接前安装插件

**+hh**, **+hermetic-home**
> 使用密封的 home 目录（~/.xxh 隔离）

**+hc**, **+host-clean**
> 从远程主机移除 xxh 目录

**+LS**, **+list-shells**
> 列出可用的便携 shell

**+LP**, **+list-plugins**
> 列出可用的插件

**-i** _keyfile_
> SSH 身份密钥文件（传递给 ssh）

**-p** _port_
> SSH 端口（传递给 ssh）

# DESCRIPTION

**xxh** 通过 SSH 把你喜欢的 shell 和配置带到任何远程主机，无需 root 权限或系统级安装。它会上传 shell（zsh、fish、bash、xonsh）的便携版本以及你的插件和配置。

运行 **xxh host** 时，它会先在本地下载便携 shell（缓存以便复用），上传到远程主机的 **~/.xxh** 目录，然后通过 SSH 连接并运行该 shell。你的别名、主题和插件立即生效。

该工具是**密封的**：从远程主机删除 **~/.xxh** 目录即可完全恢复原始环境。不同的密封级别控制 xxh 环境与系统的隔离程度。

插件可以扩展功能，添加 oh-my-zsh、powerlevel10k 或命令行实用工具等。插件用 **+I plugin-name** 安装。

# CAVEATS

xxh 要求本地机器安装 Python 3.6+。首次连接新主机时上传便携 shell 可能较慢。某些插件可能有额外的依赖。远程主机需要 tar 和 gzip 等基本工具。

# HISTORY

**xxh** 的诞生是为了解决连接远程服务器时丢失自定义 shell 环境的问题。它用 Python 编写，提供了一种在多台机器间保持一致命令行体验的方式。该项目通过社区贡献的便携 shell 软件包支持多种 shell。

# INSTALL

```brew: brew install xxh```

```nix: nix profile install nixpkgs#xxh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [bash](/man/bash)(1)
