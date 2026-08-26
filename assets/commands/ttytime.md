# TAGLINE

显示 ttyrec 录像的时长

# TLDR

**显示单个录像的时长**

```ttytime [recording.tty]```

**显示多个录像的时长**

```ttytime [file1.tty] [file2.tty] [file3.tty]```

**显示目录中所有录像的时长**

```ttytime [*.tty]```

# SYNOPSIS

**ttytime** _file_ [_file_...]

# DESCRIPTION

**ttytime** 以秒为单位显示 ttyrec 录像的总播放时长。它读取 ttyrec 文件中内嵌的计时信息，并计算从头到尾的总耗时。

输出会为每个指定文件显示时长及其文件名。这样无需回放即可快速查看录像长度、整理录像，或基于会话时长编写脚本。

可以一次指定多个文件，批量获取一组录像的时长。

# OUTPUT FORMAT

输出由秒数和文件名组成：

```
173 session1.tty
42 session2.tty
1832 longdemo.tty
```

# CAVEATS

仅适用于 ttyrec 格式的文件。时长反映的是计时数据，而不是实际内容长度。损坏的录像可能报告错误的时间。

# HISTORY

**ttytime** 作为 ttyrec 和 ttyplay 的配套工具而创建，无需完整回放即可快速获取时长信息。它是 ttyrec 软件包的一部分，该软件包在 Unix 社区中常用于录制和分享终端会话。

# INSTALL

```apt: sudo apt install ttyrec```

```brew: brew install ttyrec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyrec](/man/ttyrec)(1), [ttyplay](/man/ttyplay)(1), [script](/man/script)(1)
