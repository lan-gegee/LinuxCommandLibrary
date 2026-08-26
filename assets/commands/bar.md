# TAGLINE

为数据传输显示进度条。

# TLDR

**带进度条复制文件**

```bar -if [input_file] -of [output_file]```

管道传输数据时**显示进度**

```cat [large_file] | bar > [output_file]```

**指定预期大小**以获得准确的进度

```bar -s [1000000000] -if [input_file] -of [output_file]```

**为进度条设置自定义标题**

```bar -ti "[Backup]" -if [input_file] -of [output_file]```

**限速传输**至固定速率

```bar -th [1M] -if [input_file] -of [output_file]```

每 2 秒**刷新显示**

```bar -i [2] -if [input_file] -of [output_file]```

# SYNOPSIS

**bar** [_options_] [_file_]

# PARAMETERS

**-if**, **--in-file** _FILE_
> 从 FILE 读取输入（默认：stdin）。

**-of**, **--out-file** _FILE_
> 将输出写入 FILE（默认：stdout）。

**-s**, **--size** _bytes_
> 用于准确显示百分比的预期数据量。

**-c**, **--completed** _bytes_
> 已复制的字节数（用于续传）。

**-bs**, **--buffer-size** _size_
> I/O 缓冲区分配大小。

**-th**, **--throttle** _rate_
> 将吞吐量限制在指定速率内。

**-i**, **--interval** _seconds_
> 显示刷新频率，单位秒（默认：1）。

**-ti**, **--title** _text_
> 为进度条设置自定义标题。

**-sw**, **--screen-width** _cols_
> 假定终端宽度固定为 _cols_ 个字符。

**-db**, **-nb**, **--display-bar**, **--no-bar**
> 切换进度条显示。

**-dp**, **-np**, **--display-percent**, **--no-percent**
> 切换百分比显示。

**-dth**, **-nth**, **--display-throughput**, **--no-throughput**
> 切换吞吐量显示。

**-dt**, **-nt**, **--display-time**, **--no-time**
> 切换已用时间 / 预计剩余时间显示。

**-ds**, **-ns**, **--display-summary**, **--no-summary**
> 切换完成摘要显示。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示程序版本。

# DESCRIPTION

**bar** (clpbar) 复制数据流，并在 stderr 上打印显示信息，包括已传输的数据量、吞吐量和传输时间。它最初用于估算通过 SSH/tar 管道移动大量数据所需的时间。

该工具适用于监控长时间运行的数据传输，例如磁盘镜像、大文件复制或需要视觉反馈的数据流操作。从普通文件读取时，它会自行获取总大小。

对于大小未知、来自管道的输入，可以使用 **-s** 选项手动指定预期大小。没有大小信息时，**bar** 只显示已传输字节和传输速率，不显示百分比。配置默认值可以放在 _/etc/clpbarrc_、_~/.barrc_ 或 _./.barrc_ 中。

# CAVEATS

**bar** 这个命令名在不同发行版上会与多种系统工具冲突。更普遍可用、应用更广的 **pv**（pipe viewer）提供了类似功能。显示百分比需要事先知道总大小。性能影响很小，但在极高速传输时可测量。

# HISTORY

Unix 生态中存在过各种名为 "bar" 的传输进度显示工具。这一概念早于图形界面，为原本静默运行的操作提供反馈。Andrew Wood 开发的 **pv**（pipe viewer）于 **2002** 年首次发布，成为这一用途的事实标准，不过以其他名称存在的更简单实现仍在延续。

# INSTALL

```apt: sudo apt install bar```

```aur: yay -S bar```

```brew: brew install bar```

```nix: nix profile install nixpkgs#bar```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pv](/man/pv)(1), [dd](/man/dd)(1), [rsync](/man/rsync)(1), [progress](/man/progress)(1)
