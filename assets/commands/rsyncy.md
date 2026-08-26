# TAGLINE

为 rsync 提供状态与进度条

# TLDR

**带可视化进度条同步文件**

```rsyncy -a [/source/] [/destination/]```

**远程同步并显示进度**

```rsyncy -avz [remote:/path/] [/local/]```

**同时启用删除与压缩的同步**

```rsyncy -avz --delete [/source/] [/destination/]```

**试运行**以预览更改

```rsyncy -avn [/source/] [/destination/]```

# SYNOPSIS

**rsyncy** [_rsync-options_] _source_ _destination_

# PARAMETERS

所有标准的 **rsync** 选项都被支持并原样传递给 rsync。rsyncy 会自动追加进度显示所需的 **--info** 标志。

# DESCRIPTION

**rsyncy** 对 rsync 进行封装，用一个可视化的进度条展示整体传输进度、速度、已用时间和文件计数。你只需像平时那样传入 rsync 的参数即可，它会自动补上所需的 **--info** 标志。rsync 自带的 **--progress** 标志只能显示单个文件的进度，而 rsyncy 展示的是跨所有文件的整体进度。

# HISTORY

**rsyncy** 由 **Christian Zangl**（laktak）创建，使用 **Go** 语言编写。

# INSTALL

```brew: brew install rsyncy```

```nix: nix profile install nixpkgs#rsyncy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [progress](/man/progress)(1), [pv](/man/pv)(1)
