# TAGLINE

显示软件包为何被安装

# TLDR

**解释软件包为何被安装**

```npm explain [package-name]```

**以 JSON 格式输出解释**

```npm explain [package-name] --json```

**解释指定版本**

```npm explain [package@version]```

# SYNOPSIS

**npm** **explain** [_package_]

# PARAMETERS

_PACKAGE_
> 要解释的软件包。

**--json**
> JSON 输出格式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm explain** 显示软件包为何被安装，并展示依赖链。

该命令会追踪依赖树，显示通向该软件包的所有路径。

# CAVEATS

别名：npm why。会显示所有依赖路径。要求该软件包已安装。

# HISTORY

npm explain 的加入是为了帮助理解复杂项目中的**依赖关系**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-ls](/man/npm-ls)(1), [npm-why](/man/npm-why)(1)
