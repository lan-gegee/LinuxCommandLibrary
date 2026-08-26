# TAGLINE

管理软件包的所有权

# TLDR

**列出软件包所有者**

```npm owner ls [package-name]```

**添加所有者**

```npm owner add [username] [package-name]```

**移除所有者**

```npm owner rm [username] [package-name]```

# SYNOPSIS

**npm** **owner** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 所有者管理子命令。

**ls** _PKG_
> 列出所有者。

**add** _USER_ _PKG_
> 添加所有者。

**rm** _USER_ _PKG_
> 移除所有者。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm owner** 管理软件包的所有权，控制谁可以发布更新。

该命令用于修改维护者，需要当前所有者权限。

# CAVEATS

需要身份验证。所有者可以添加/移除其他所有者。会影响发布权限。

# HISTORY

npm owner 提供**维护者管理**功能，用于控制软件包的发布权限。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-access](/man/npm-access)(1)
