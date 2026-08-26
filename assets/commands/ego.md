# TAGLINE

Funtoo Linux 系统个性管理器

# TLDR

**同步** Portage 树

```ego sync```

**更新**引导加载程序配置

```ego boot update```

**阅读** Funtoo wiki 页面

```ego doc [wiki_page]```

**打印**当前 profile

```ego profile show```

**启用/禁用** mix-in

```ego profile mix-in +[gnome] -[kde-plasma-5]```

**查询**软件包相关的 Funtoo bug

```ego query bug [package]```

# SYNOPSIS

**ego** _command_ [_arguments_]

# DESCRIPTION

**ego** 是 Funtoo 官方的系统个性管理工具。它为同步仓库、管理 profile、更新引导加载程序配置以及访问 Funtoo 文档提供统一接口。

可用模块包括：**sync**、**profile**、**query**、**doc**、**boot**、**kit** 和 **config**。它用一个连贯的接口取代了多个独立的工具。

# PARAMETERS

**sync**
> 同步 Portage 树

**boot update**
> 更新引导加载程序配置

**doc** _page_
> 阅读 wiki 文档

**profile show**
> 显示当前 profile

**profile mix-in** _changes_
> 使用 +/- 启用/禁用 mix-in

**query bug** _package_
> 查询软件包的相关 bug

**kit**
> 显示 kit 信息

**config**
> 查看和修改 /etc/ego.conf 设置

**help** [_module_]
> 显示 ego 或特定模块的帮助。

# CONFIGURATION

**/etc/ego.conf**
> ego profile 和设置的主配置文件。

# CAVEATS

Funtoo Linux 特有。原版 Gentoo 或其他发行版上不可用。需要正确的 /etc/ego.conf 配置。Ego 是对 **eselect** 的封装，也是其在 Funtoo 上的预期替代品；快捷方式 `epro` 等价于 `ego profile`。

# HISTORY

**ego** 由 **Funtoo Linux** 项目引入，该项目是由 Daniel Robbins（Gentoo 创始人）领导的 Gentoo 衍生发行版。它将此前相互独立的功能（profile 选择、Portage 树同步、引导加载程序生成）整合为单一的模块化命令，并在 Funtoo 系统上取代了 eselect 的部分功能。

# INSTALL

```nix: nix profile install nixpkgs#ego```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emerge](/man/emerge)(1), [eselect](/man/eselect)(1)
