# TAGLINE

修复损坏的 scamper warts 文件

# TLDR

**修复损坏的 warts 文件**并将输出写到标准输出

```sc_wartsfix [input.warts] > [fixed.warts]```

**修复并通过管道**传给 sc_wartsdump 检查

```sc_wartsfix [input.warts] | sc_wartsdump```

# SYNOPSIS

**sc_wartsfix** _file_

# DESCRIPTION

**sc_wartsfix** 尝试从被截断或损坏的 scamper warts 文件中抢救有效记录。它会读取输入文件，跳过损坏或不完整的记录，并将恢复出的有效记录写到标准输出。当 scamper 数据采集被中断（例如进程崩溃、磁盘写满）并留下一个只写入了一部分的 warts 文件时，这个工具非常有用。

该工具是 **scamper** 互联网测量工具集的一部分。

# CAVEATS

只能恢复结构完整的记录；损坏记录内的数据会丢失。输出应使用 sc_wartsdump 进行验证。

# SEE ALSO

[sc_wartscat](/man/sc_wartscat)(1), [sc_wartsdump](/man/sc_wartsdump)(1), [scamper](/man/scamper)(1)
