# TAGLINE

在 Mageia Linux 上安装软件包

# TLDR

**安装**软件包

```sudo urpmi [package]```

从**本地** RPM 安装

```sudo urpmi [path/to/file.rpm]```

只**下载**而不安装

```urpmi --no-install [package]```

**更新**所有软件包

```sudo urpmi --auto-select```

在**多台**机器上安装

```sudo urpmi --parallel local [package]```

# SYNOPSIS

**urpmi** [_OPTIONS_] _PACKAGE_...

# PARAMETERS

**--no-install**
> 只下载软件包而不安装

**--auto-select**
> 更新所有已安装的软件包

**--parallel** _CONFIG_
> 在多台机器上并行安装

**--auto**
> 自动确认操作

# DESCRIPTION

**urpmi** 是 Mageia Linux 的软件包安装工具。它可以从仓库或本地 RPM 文件安装软件包，并自动处理依赖关系。

该工具支持更新全部已安装的软件包，还能通过并行配置跨多台机器管理软件包。

# CAVEATS

Mageia 专用。请先运行 urpmi.update -a 以获取最新软件包列表。执行安装需要 root 权限。

# SEE ALSO

[urpme](/man/urpme)(8), [urpmq](/man/urpmq)(8), [urpmi.update](/man/urpmi.update)(8), [urpmi.addmedia](/man/urpmi.addmedia)(8)
