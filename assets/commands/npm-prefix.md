# TAGLINE

输出本地或全局前缀路径

# TLDR

**显示本地前缀**

```npm prefix```

**显示全局前缀**

```npm prefix -g```

# SYNOPSIS

**npm** **prefix** [_options_]

# PARAMETERS

**-g**
> 全局前缀。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm prefix** 输出本地或全局前缀路径，显示软件包的安装位置。

该命令显示安装目录，适合在脚本中使用。

# CAVEATS

本地模式显示最近的 package.json 所在目录。全局模式显示 npm 的全局路径。

# HISTORY

npm prefix 帮助定位**软件包安装目录**，便于脚本编写和调试。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-root](/man/npm-root)(1), [npm-bin](/man/npm-bin)(1)
