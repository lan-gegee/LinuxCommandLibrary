# TAGLINE

执行命令并将 stdout 和 stderr 都保存到日志文件

# TLDR

将**命令输出保存**到日志

```logsave [path/to/logfile] [command]```

将 **stdin** 保存到日志

```logsave [logfile] -```

**追加**到日志文件

```logsave -a [logfile] [command]```

以**详细**输出运行

```logsave -v [logfile] [command]```

# SYNOPSIS

**logsave** [_options_] _logfile_ _command_ [_arguments_]

# DESCRIPTION

**logsave** 执行一个命令并将 stdout 和 stderr 都保存到日志文件。它会记录时间戳和退出状态，因此适合用来记录计划任务或系统脚本的输出。

# PARAMETERS

**-a**
> 追加到日志文件而不是覆盖

**-v**
> 详细模式

**-**
> 从 stdin 读取而不执行命令

# CAVEATS

属于 e2fsprogs 软件包的一部分。日志文件中会记录开始、结束的时间戳以及命令的退出状态。

# INSTALL

```apt: sudo apt install logsave```

```apk: sudo apk add e2fsprogs-extra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[script](/man/script)(1), [tee](/man/tee)(1), [logger](/man/logger)(1)
