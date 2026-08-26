# TAGLINE

执行 npm 软件包

# TLDR

**运行软件包命令**

```npx [package-name]```

**运行特定版本**

```npx [package]@[version]```

**不安装直接运行**

```npx --no-install [package]```

**带参数运行**

```npx [create-react-app] [my-app]```

**从 GitHub 运行**

```npx github:[user]/[repo]```

**运行本地二进制文件**

```npx [./node_modules/.bin/command]```

**执行软件包命令**

```npx -p [package] -c "[command]"```

# SYNOPSIS

**npx** [_options_] _package_ [_args_]

# PARAMETERS

_PACKAGE_
> 要执行的软件包。

_ARGS_
> 要传递的参数。

**--no-install**
> 缺失时不安装。

**-p** _PKG_
> 要安装的软件包。

**-c** _CMD_
> 要运行的命令。

**-y**, **--yes**
> 自动确认提示。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npx** 用于执行 npm 软件包的二进制文件。它会先检查本地 **node_modules/.bin**，再检查全局安装的软件包，如果都找不到则临时下载该软件包。

常见用途包括运行项目脚手架工具（create-react-app、create-next-app）、一次性实用程序，以及在不全局安装的情况下测试不同版本的软件包。

# CAVEATS

首次运行时下载。会缓存软件包。npm 5.2+ 的一部分。

# HISTORY

npx 随 **npm 5.2** 推出，旨在简化 npm 软件包的运行而无需安装。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-exec](/man/npm-exec)(1), [yarn](/man/yarn)(1)
