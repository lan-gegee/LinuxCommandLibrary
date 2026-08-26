# TAGLINE

管理 Doom Emacs 配置框架

# TLDR

**安装 Doom Emacs**

```doom install```

配置变更后**同步软件包**

```doom sync```

**更新软件包**

```doom upgrade```

**检查问题**

```doom doctor```

**重建软件包**

```doom build```

**清理无用**软件包

```doom purge```

# SYNOPSIS

**doom** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：install、sync、upgrade、doctor、build、purge。

**install**
> 执行 Doom Emacs 的初始安装。

**sync**
> 让软件包与配置保持同步。

**upgrade**
> 将软件包更新到最新版本。

**doctor**
> 诊断常见问题。

**build**
> 重新构建已安装的软件包。

**purge**
> 移除孤立的软件包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doom** 是 Doom Emacs（一个 Emacs 配置框架）的命令行界面，负责该发行版的安装、更新和维护。

sync 命令是 Doom 工作流的核心：修改 init.el 或 packages.el 之后，用它确保已安装的软件包与配置一致。它会处理软件包的安装、移除和字节编译。

doom doctor 通过检查缺失依赖、过期软件包、配置错误之类的常见问题来协助排障。

# CONFIGURATION

**~/.doom.d/init.el**
> 核心配置文件，用于启用 Doom 模块和特性。

**~/.doom.d/config.el**
> 用户专属设置、按键绑定和自定义内容。

**~/.doom.d/packages.el**
> Doom 默认集合之外的额外 Emacs 软件包声明。

# CAVEATS

需要 Emacs 27.1 及以上版本。软件包较多时同步可能耗时。某些操作需要访问互联网。主要版本之间可能出现破坏性变更。

# HISTORY

Doom Emacs 由 **Henrik Lissner** 自 **2016 年**前后开始打造。doom CLI 为这个流行的 Emacs 配置提供管理能力，该配置以速度和精心挑选的软件包集合著称。

# INSTALL

```aur: yay -S doom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emacs](/man/emacs)(1)
