# TAGLINE

查询远程 Flatpak 软件包的信息

# TLDR

显示远程仓库中某个 flatpak 的**信息**

```flatpak remote-info [remote_name] [com.example.app]```

显示远程仓库中**历史版本的日志**

```flatpak remote-info --log [remote_name] [com.example.app]```

显示**特定提交**的信息

```flatpak remote-info --commit [COMMIT_HASH] [remote_name] [com.example.app]```

只显示**提交 ID**（机器可读）

```flatpak remote-info --show-commit [remote_name] [com.example.app]```

显示远程应用的**元数据**

```flatpak remote-info --show-metadata [remote_name] [com.example.app]```

显示特定**架构**的信息

```flatpak remote-info --arch [x86_64] [remote_name] [com.example.app]```

# SYNOPSIS

**flatpak remote-info** [_options_] _remote_ _ref_

# PARAMETERS

**--user**
> 使用按用户的配置

**--system**
> 使用默认的系统级配置

**--installation** _name_
> 使用指定的系统级安装

**--cached**
> 尽可能使用本地缓存的数据

**--runtime**
> 假定 ref 是一个运行时

**--app**
> 假定 ref 是一个应用

**--arch** _arch_
> 针对特定架构

**--commit** _commit_
> 显示特定提交的信息

**--log**
> 显示版本历史

**-r, --show-ref**
> 显示匹配到的 ref（机器可读）

**-c, --show-commit**
> 显示提交 ID（机器可读）

**-p, --show-parent**
> 显示父提交

**-m, --show-metadata**
> 显示元数据

**-v, --verbose**
> 输出调试信息

# DESCRIPTION

**Flatpak remote-info** 显示远程仓库中可用应用程序或运行时的详细信息。它展示的信息包括应用 ID、架构、分支、提交哈希、下载大小、安装大小以及运行时依赖。

默认输出为人类可读格式。使用 **--show-*** 选项则切换为适合脚本的机器可读输出。

**--log** 选项可用于查看可用版本，并找到特定提交以便执行降级操作或固定版本。

# CAVEATS

除非指定 **--cached**，否则查询远程仓库需要网络访问。cached 选项只有在仓库元数据此前已被获取的情况下才有效。某些信息可能并非对所有远程仓库或 ref 都可用。

# HISTORY

本命令是 Red Hat 的 Alexander Larsson 所开发 **Flatpak** 项目的一部分。Flatpak 约于 **2015 年**从 xdg-app 项目演化而来，如今已成为 Linux 桌面应用领先的通用软件包格式。

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-update](/man/flatpak-update)(1), [flatpak-install](/man/flatpak-install)(1)
