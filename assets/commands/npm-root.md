# TAGLINE

输出 node_modules 目录路径

# TLDR

**显示本地 node_modules 路径**

```npm root```

**显示全局 node_modules 路径**

```npm root -g```

# SYNOPSIS

**npm** **root** [_options_]

# PARAMETERS

**-g**
> 全局 node_modules。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm root** 输出 node_modules 目录路径，显示软件包的安装位置。

该命令显示模块所在目录，适合脚本和调试使用。

# CAVEATS

本地模式显示项目的 node_modules。全局模式显示系统路径。

# HISTORY

npm root 帮助定位用于软件包管理的 **node_modules 目录**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-prefix](/man/npm-prefix)(1), [npm-bin](/man/npm-bin)(1)
