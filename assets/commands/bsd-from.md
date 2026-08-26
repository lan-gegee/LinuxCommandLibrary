# TAGLINE

显示邮箱中邮件的发件人信息

# TLDR

**显示谁给你发过邮件**

```bsd-from```

只显示邮件数量

```bsd-from -c```

显示来自特定发件人的邮件

```bsd-from -s [sender]```

查看其他邮箱文件

```bsd-from -f [path/to/mailbox]```

检查其他用户的邮箱

```bsd-from [username]```

# SYNOPSIS

**bsd-from** [**-c**] [**-f** _file_] [**-s** _sender_] [_user_]

# DESCRIPTION

**bsd-from**（也称为 **from**）打印邮箱中的邮件头信息行，显示发过邮件的人名。默认情况下，它检查调用者的邮箱。

该命令提供了一种快速查看待处理邮件的方式，无需打开完整的邮件客户端。它显示各封邮件的 "From" 行，让人一目了然地了解谁发来过邮件。

# PARAMETERS

**-c**
> 只打印邮件数量后退出。

**-f** _file_
> 检查指定文件而非默认邮箱。使用 **-** 可从标准输入读取。

**-s** _sender_
> 只打印地址包含指定字符串的邮件。

**user**
> 检查指定用户的邮箱而非调用者自己的（需要相应权限）。

# CAVEATS

使用 **-f** 选项时不应指定 user 参数。检查其他用户的邮箱需要更高权限。

默认邮箱位置由 **MAIL** 环境变量决定；未设置时为 **/var/mail**。

# HISTORY

**from** 命令最早出现于 **1979** 年的 **BSD 3.0**，是 Berkeley Software Distribution 邮件工具集的一部分。

# SEE ALSO

[biff](/man/biff)(1), [mail](/man/mail)(1)

# RESOURCES

```[Source code](https://cgit.freebsd.org/src/tree/usr.bin/from)```

<!-- verified: 2026-06-22 -->
