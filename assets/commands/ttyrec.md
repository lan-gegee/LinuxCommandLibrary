# TAGLINE

带时序信息的终端会话录制工具

# TLDR

将终端会话**录制到默认文件**（ttyrecord）

```ttyrec```

**录制到指定文件**

```ttyrec [path/to/recording.tty]```

**追加到现有录像**

```ttyrec -a [path/to/recording.tty]```

**录制指定命令**而非默认 shell

```ttyrec -e [command] [path/to/recording.tty]```

录制并自动调用 uudecode 以便传输文件

```ttyrec -u [path/to/recording.tty]```

# SYNOPSIS

**ttyrec** [**-a**] [**-u**] [**-e** _command_] [_file_]

# PARAMETERS

**-a**
> 将输出追加到文件而不是覆盖。

**-u**
> 当会话中出现 uuencoded 数据时，自动调用 uudecode(1) 并保存其输出。适合从远程主机传输文件。

**-e** _command_
> ttyrec 启动时执行指定命令而不是默认 shell。

_file_
> 录像的输出文件。默认为当前目录下的 "ttyrecord"。

# DESCRIPTION

**ttyrec** 是一个终端会话录制器，以微秒级时间精度捕获所有终端输出。它派生自 script(1) 命令，但增加了精确回放所必需的计时信息。

启动后，ttyrec 会派生一个新 shell（或用 **-e** 指定的命令）并记录所有输出，直到 shell 退出。录像包含时间数据，使 ttyplay 能够以原始速度重现会话，非常适合制作教程、演示或记录终端操作流程。

所使用的 shell 由 SHELL 环境变量决定，未设置时回退到 /bin/sh。录像可用 **ttyplay** 回放，时长可用 **ttytime** 查看。

# CAVEATS

稍不注意，录像中可能包含密码等敏感信息。录制格式不可直接阅读，需要 ttyplay 才能回放。根据会话活动量，大型录像可能占用大量磁盘空间。回放时的终端尺寸应与录制时一致才能正确显示。

# HISTORY

**ttyrec** 由 **Satoru Takabayashi** 于 **21 世纪初**在日本开发。它在 Unix 社区中被广泛用于创建终端演示和教程。OVH 后来开发了增强版（ovh-ttyrec），增加了锁定和实时流支持等特性。

# INSTALL

```apt: sudo apt install ttyrec```

```brew: brew install ttyrec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyplay](/man/ttyplay)(1), [ttytime](/man/ttytime)(1), [script](/man/script)(1), [asciinema](/man/asciinema)(1)
