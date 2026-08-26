# TAGLINE

管理 npm 软件包缓存

# TLDR

**清除 npm 缓存**

```npm cache clean --force```

**校验缓存完整性**

```npm cache verify```

**显示缓存位置**

```npm cache ls```

# SYNOPSIS

**npm** **cache** _command_ [_options_]

# PARAMETERS

**clean**
> 删除缓存文件夹的内容。

**verify**
> 校验缓存完整性。

**ls**
> 列出缓存内容。

**--force**
> clean 命令必需。

# DESCRIPTION

**npm cache** 管理 npm 软件包缓存。缓存放的是下载过的软件包，用于加快安装速度。verify 会校验完整性并删除损坏的条目。clean 需要 --force 标志。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1)
