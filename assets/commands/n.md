# TAGLINE

node

# TLDR

**安装最新版 Node.js**

```n latest```

**安装 LTS 版本**

```n lts```

**安装指定版本**

```n [18.16.0]```

**列出已安装的版本**

```n ls```

**切换到已安装的版本**

```n```

**移除版本**

```n rm [18.16.0]```

**以指定版本运行**

```n run [18.16.0] [script.js]```

**清除所有版本**

```n prune```

# SYNOPSIS

**n** [_command_] [_version_]

# PARAMETERS

_VERSION_
> Node.js 版本号。

**latest**
> 安装最新版本。

**lts**
> 安装 LTS 版本。

**ls**
> 列出已安装的版本。

**rm** _VERSION_
> 移除版本。

**run** _VERSION_
> 以指定版本运行。

**prune**
> 移除旧版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**n** 是一个 Node.js 版本管理器。它用于安装并在不同 Node.js 版本之间切换。

该工具管理多个安装。为版本控制提供简单的界面。

# CAVEATS

全局安装需要 sudo。比 nvm 更简单。基于 Bash 脚本实现。

# HISTORY

n 由 **TJ Holowaychuk** 创建，作为 nvm 之外更简单的 Node.js 版本管理方案。

# INSTALL

```brew: brew install n```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvm](/man/nvm)(1), [node](/man/node)(1), [npm](/man/npm)(1)
