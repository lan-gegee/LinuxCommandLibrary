# TAGLINE

WSL 的 systemd 命名空间容器（bottle）

# TLDR

**初始化**容器（启动时运行一次）

```genie -i```

在容器内运行一个**登录 shell**

```genie -s```

在容器内运行**指定的命令**

```genie -c [command]```

# SYNOPSIS

**genie** [_options_]

# PARAMETERS

**-i**, **--initialize**
> 为 systemd 初始化容器命名空间

**-s**, **--shell**
> 在容器内启动登录 shell

**-c**, **--command** _COMMAND_
> 在容器内运行命令后退出

**-u**, **--user** _USER_
> 以指定用户身份运行（默认：当前用户）

**-v**, **--verbose**
> 启用详细输出

# CONFIGURATION

**/etc/genie.ini**
> 主配置文件，控制 systemd 路径、用户映射以及容器行为。

# DESCRIPTION

**genie** 在 Windows Subsystem for Linux（WSL）内创建一个"bottle"——一个以 systemd 作为 PID 1 运行的 PID 命名空间。这使得依赖 systemd 的服务能够在 WSL 默认环境下无法运行的情况中正常工作。

WSL 通常使用 Microsoft 的 init 系统，这导致 systemd 服务无法运行。genie 通过创建一个可让 systemd 正常运行的命名空间来规避此问题，并提供进入该环境的途径。

每个 WSL 会话先用 **-i** 初始化一次容器，然后使用 **-s** 进入或用 **-c** 在 systemd 环境中运行命令。

# CAVEATS

需要 WSL 2。受 WSL 自身限制影响，某些 systemd 服务可能仍无法完美运行。容器在使用前必须初始化，并持续存在直到 WSL 关闭。网络配置在容器内的表现可能有所不同。

# HISTORY

genie 由 Arkane Systems 开发，旨在解决 WSL 缺乏 systemd 支持的问题。随着 systemd 成为大数 Linux 发行版的标准 init 系统，许多服务和工具都假定它存在，这在 WSL 独特的环境中造成了兼容性问题。

# SEE ALSO
