# TAGLINE

列出已安装的软件包

# TLDR

**列出已安装的软件包**

```npm ls```

**列出所有层级**

```npm ls --all```

**列出指定软件包**

```npm ls [package-name]```

**列出全局软件包**

```npm ls -g```

**JSON 输出**

```npm ls --json```

**仅生产依赖**

```npm ls --production```

**显示指定深度**

```npm ls --depth=[2]```

# SYNOPSIS

**npm** **ls** [_package_] [_options_]

# PARAMETERS

_PACKAGE_
> 要查找的软件包。

**--all**
> 显示所有依赖。

**-g**
> 全局软件包。

**--json**
> JSON 输出。

**--depth** _N_
> 树的深度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm ls** 列出已安装的软件包，并显示依赖树。

该命令展示软件包的层级结构，并标明各依赖的版本。

# CAVEATS

别名：npm list。树可能很大，可用 depth 限制深度。

# HISTORY

npm ls 提供**依赖可视化**，帮助理解软件包之间的关系。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-explain](/man/npm-explain)(1), [npm-outdated](/man/npm-outdated)(1)
