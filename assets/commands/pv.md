# TAGLINE

监控通过管道传输的数据

# TLDR

**显示传输进度**

```pv [file] > [output]```

**带进度的管道**

```cat [file] | pv > [output]```

**限制传输速率**

```pv -L [1m] [file] > [output]```

**显示预计完成时间**

```pv -e [file] > [output]```

**为传输命名**

```pv -N "Copying" [file] > [output]```

# SYNOPSIS

**pv** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入文件。

**-L** _RATE_
> 速率限制。

**-N** _NAME_
> 传输名称。

**-e**
> 显示预计完成时间。

**-p**
> 显示百分比。

**-t**
> 显示已用时间。

**-r**
> 显示速率。

**-s** _SIZE_
> 预期大小。

# DESCRIPTION

**pv**（Pipe Viewer）监控流经 Unix 管道的数据进度。它可以插入管道中的任意两个命令之间，显示进度条、传输速率、已用时间、预计剩余时间和完成百分比。

当给定文件作为输入时，pv 可以计算总大小并显示有意义的进度百分比。对于大小未知的流，使用 **-s** 标志指定预期大小。**-L** 选项限制传输速率，可用于对操作进行节流。在复杂的管道中，多个 **-N** 标志可以为不同的 pv 实例命名，以便独立跟踪每个阶段。pv 常用于给 **dd** 磁盘镜像、数据库导入或大文件传输等操作添加可视化反馈。

# CAVEATS

会带来少量开销。插入到命令之间使用。

# HISTORY

pv 是为**监控数据**在管道中的传输进度而创建的。

# INSTALL

```apt: sudo apt install pv```

```dnf: sudo dnf install pv```

```pacman: sudo pacman -S pv```

```apk: sudo apk add pv```

```zypper: sudo zypper install pv```

```brew: brew install pv```

```nix: nix profile install nixpkgs#pv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [rsync](/man/rsync)(1), [progress](/man/progress)(1)
