# TAGLINE

管理 JavaScript monorepo

# TLDR

**初始化 monorepo**

```lerna init```

**引导安装各个软件包**

```lerna bootstrap```

**在所有软件包中运行脚本**

```lerna run [build]```

**在特定软件包中运行**

```lerna run [build] --scope=[package-name]```

**发布软件包**

```lerna publish```

**列出软件包**

```lerna list```

**为软件包提升版本号**

```lerna version```

# SYNOPSIS

**lerna** _command_ [_options_]

# PARAMETERS

**init**
> 初始化 monorepo。

**bootstrap**
> 安装依赖。

**run** _SCRIPT_
> 运行 npm 脚本。

**publish**
> 发布软件包。

**version**
> 提升版本号。

**list**
> 列出软件包。

**--scope** _PKG_
> 针对特定的软件包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Lerna** 负责 JavaScript monorepo 的管理。它可以处理单个仓库中的多个软件包。

该工具协调版本管理与发布。它会链接本地依赖并跨软件包运行脚本。

# CAVEATS

可以考虑 npm/yarn workspaces。高级功能可用 Nx。需要 Node.js。

# HISTORY

Lerna 由 **Sebastian McKenzie**（Babel 作者）创建，用于管理 monorepo，目前由 Nx 维护。

# INSTALL

```brew: brew install lerna```

```nix: nix profile install nixpkgs#lerna```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [nx](/man/nx)(1)
