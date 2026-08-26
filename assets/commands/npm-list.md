# TAGLINE

显示已安装软件包的依赖树

# TLDR

**列出已安装的软件包**

```npm list```

**列出全局软件包**

```npm list -g```

**只列出顶层软件包**

```npm list --depth=0```

**以 JSON 格式列出**

```npm list --json```

**列出指定软件包**

```npm list [package-name]```

**列出生产依赖**

```npm list --prod```

# SYNOPSIS

**npm** **list** [_package_] [_options_]

# PARAMETERS

**-g**, **--global**
> 列出全局软件包。

**--depth** _n_
> 依赖树深度。

**--json**
> 以 JSON 格式输出。

**--prod**
> 仅生产依赖。

**--dev**
> 仅开发依赖。

**--all**
> 显示所有软件包。

# DESCRIPTION

**npm list** 显示已安装软件包的依赖树，包括版本和依赖关系。使用 depth=0 只看顶层。别名：npm ls。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1)
