# TAGLINE

Nim 软件包管理器

# TLDR

**安装软件包**

```nimble install [package]```

**构建项目**

```nimble build```

**运行项目**

```nimble run```

**初始化项目**

```nimble init```

**搜索软件包**

```nimble search [query]```

**列出已安装的软件包**

```nimble list --installed```

**更新软件包列表**

```nimble refresh```

**运行测试**

```nimble test```

# SYNOPSIS

**nimble** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Nimble 命令。

**install** _PKG_
> 安装软件包。

**build**
> 构建当前项目。

**run**
> 构建并运行。

**init**
> 初始化新项目。

**search** _QUERY_
> 搜索软件包。

**test**
> 运行测试。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nimble** 是 Nim 的软件包管理器，用于安装依赖和管理项目。

该工具负责软件包安装，支持本地和远程软件包。

# CAVEATS

需要 Nim 环境。基于软件包注册表运作。软件包可在 nimble.directory 查找。

# HISTORY

Nimble 作为 Nim 编程语言的**官方软件包管理器**而诞生。

# INSTALL

```apk: sudo apk add nimble```

```nix: nix profile install nixpkgs#nimble```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nim](/man/nim)(1), [npm](/man/npm)(1), [cargo](/man/cargo)(1)
