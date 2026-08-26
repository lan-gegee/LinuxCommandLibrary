# TAGLINE

导出 utmp 和 wtmp 登录记账文件

# TLDR

将 wtmp 文件**导出**到 stdout

```utmpdump /var/log/wtmp```

导出 **btmp** 文件（登录失败的记录）

```utmpdump /var/log/btmp```

**跟踪**文件的新增条目

```utmpdump -f /var/log/wtmp```

把输出写入**文件**

```utmpdump -o output.txt /var/log/wtmp```

将编辑后的导出内容**反向**（重新载入）写回文件

```utmpdump -r dumpfile > /var/log/wtmp```

# SYNOPSIS

**utmpdump** [_options_] [_filename_]

# DESCRIPTION

**utmpdump** 以原始格式转储 UTMP 和 WTMP 文件的内容，便于检查和调试。它还支持逆向操作，把编辑过的登录信息写回记账文件。

# PARAMETERS

**-f, --follow**
> 随着文件增长持续输出新追加的数据

**-o, --output FILE**
> 把输出写入指定文件而非 stdout

**-r, --reverse**
> 反向转储；将编辑过的登录信息写回 utmp/wtmp 文件

**-h, --help**
> 显示帮助文本并退出

**-V, --version**
> 打印版本并退出

# CAVEATS

本工具专为调试而设计。-r 选项必须极其谨慎地使用，操作不当可能损坏登录记账文件。时间戳采用 UTC-0 时区、毫秒精度的 ISO-8601 格式。

# HISTORY

**utmpdump** 属于 **util-linux** 软件包，可用于检查和修复损坏的 utmp、wtmp 条目。

# INSTALL

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[last](/man/last)(1), [lastb](/man/lastb)(1), [who](/man/who)(1), [w](/man/w)(1)
