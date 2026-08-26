# TAGLINE

GnuPG 组件配置工具

# TLDR

**列出所有 GnuPG 组件**

```gpgconf --list-components```

**列出 GnuPG 使用的目录**

```gpgconf --list-dirs```

**重新加载 gpg-agent**

```gpgconf --reload gpg-agent```

**终止 gpg-agent**

```gpgconf --kill gpg-agent```

**启动 gpg-agent**

```gpgconf --launch gpg-agent```

**列出某个组件的选项**

```gpgconf --list-options [gpg-agent]```

**应用默认配置**

```gpgconf --apply-defaults```

# SYNOPSIS

**gpgconf** [_options_] [_command_]

# SUBCOMMANDS

**--list-components**
> 列出已安装的 GnuPG 组件。

**--list-dirs**
> 列出 GnuPG 使用的目录。

**--list-options** _component_
> 列出组件的选项。

**--list-config**
> 列出全局配置。

**--check-options** _component_
> 检查组件的选项。

**--apply-defaults**
> 应用默认值。

**--reload** _component_
> 重新加载某个组件。

**--kill** _component_
> 终止正在运行的组件。

**--launch** _component_
> 启动某个组件。

**--check-programs**
> 检查已安装的程序。

# DESCRIPTION

**gpgconf** 是一个用于查询和修改 GnuPG 组件配置的工具。它可以管理 gpg-agent 等守护进程、以编程方式应用设置以及检查 GnuPG 的安装情况。

该工具常用于在配置更改后重新加载 gpg-agent、列出可用组件以及排查 GnuPG 安装问题。

# INSTALL

```apt: sudo apt install gpgconf```

```apk: sudo apk add gnupg-gpgconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1)
