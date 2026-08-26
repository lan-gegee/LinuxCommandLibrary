# TAGLINE

Yazi 文件管理器的命令行配套工具

# TLDR

**安装插件**或主题包

```ya pkg add [owner/repo]```

**更新所有已安装的软件包**

```ya pkg upgrade```

**删除软件包**

```ya pkg delete [owner/repo]```

**列出已安装的软件包**

```ya pkg list```

**从 package.toml 安装软件包**

```ya pkg install```

向 yazi**发布消息**

```ya pub [receiver] [args]```

向 yazi**发出命令**

```ya emit [command] [args]```

**显示版本**

```ya --version```

# SYNOPSIS

**ya** _subcommand_ [_options_] [_arguments_]

# SUBCOMMANDS

**pkg**
> 插件和主题的软件包管理器。

**pub**
> 向运行中的 yazi 实例发布消息。

**emit**
> 向运行中的 yazi 实例发出命令。

# PKG SUBCOMMANDS

**pkg add** _package_ [_package_...]
> 安装软件包（owner/repo 格式）。

**pkg upgrade**
> 更新所有已安装的软件包。

**pkg delete** _package_ [_package_...]
> 移除已安装的软件包。

**pkg list**
> 列出已安装的软件包。

**pkg install**
> 从 package.toml 安装锁定的版本。

# DESCRIPTION

**ya**（yazi-cli）是 **Yazi** 的命令行配套工具，Yazi 是一个用 Rust 编写的高速终端文件管理器。它提供插件和主题的软件包管理功能，并可与运行中的 Yazi 实例通信。

软件包管理器从 GitHub 仓库下载插件和主题。软件包以 **owner/repo** 格式指定（例如 **yazi-rs/plugins**）。已安装的软件包记录在 **~/.config/yazi/package.toml** 中。

**pub** 和 **emit** 命令允许外部脚本与运行中的 Yazi 实例交互，实现自动化以及与其他工具的集成。它们会验证接收者存在并具备所需的能力。

ya 随主 **yazi** 文件管理器二进制文件一同安装。

# CAVEATS

ya 的软件包操作需要联网。**ya** 版本必须与已安装的 **yazi** 版本匹配。某些软件包可能要求特定的 Yazi 版本。

# HISTORY

**ya**（yazi-cli）由 **sxyazi** 作为 **Yazi** 项目的一部分开发。Yazi 于 **2023 年**前后首次发布，是用 Rust 编写的现代异步终端文件管理器。CLI 工具的加入为文件管理器生态提供了软件包管理和进程间通信能力。

# INSTALL

```apk: sudo apk add yazi-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yazi](/man/yazi)(1), [ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1)
