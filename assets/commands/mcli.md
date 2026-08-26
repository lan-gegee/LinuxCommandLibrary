# TAGLINE

Minecraft 服务器管理 CLI

# TLDR

**列出已配置的**服务器

```mcli server list```

**显示服务器信息**

```mcli server info [server]```

**启动服务器**

```mcli server start [server]```

**停止服务器**

```mcli server stop [server]```

**连接到服务器**控制台

```mcli server attach [server]```

**创建备份**

```mcli backup create [server]```

**跟踪服务器**日志

```mcli log [server]```

# SYNOPSIS

**mcli** _command_ [_subcommand_] [_options_]

# PARAMETERS

**server**
> 管理服务器生命周期：list、info、start、stop、restart、attach。

**backup**
> 创建、列出或恢复服务器备份。

**log**
> 显示或跟踪服务器日志。

**config**
> 读取或修改 mcli/服务器配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mcli** 是一个用于管理 Linux 主机上多个 Minecraft 服务器实例的命令行界面。它将服务器 JAR 生命周期、控制台连接、世界备份和各实例配置统一封装在一个 CLI 之后。

服务器通常定义在配置文件或目录中；`mcli server list` 枚举它们，而 `start`/`stop`/`attach` 子命令作用于指定名称的实例。备份从世界目录生成，具体是在服务器运行还是停止时进行取决于配置。

# CAVEATS

需要可用的 Java 运行时来启动底层的服务器 JAR。运行 mcli 的用户需要对服务器目录拥有读写权限。控制台连接通常依赖已安装的 **screen** 或 **tmux**。

# HISTORY

**mcli** 是一个社区开发的工具，源于在 Linux 机器上脚本化管理 Minecraft 服务器的实际需求，取代了围绕 `screen` 和服务器 JAR 的临时 shell 包装脚本。

# INSTALL

```pacman: sudo pacman -S minio-client```

```apk: sudo apk add minio-client```

```zypper: sudo zypper install minio-client```

```nix: nix profile install nixpkgs#minio-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1)
