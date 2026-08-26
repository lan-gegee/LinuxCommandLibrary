# TAGLINE

显示邮箱中邮件的发件人信息

# TLDR

**显示邮箱中的所有发件人**

```from```

**显示特定用户的发件人**

```from [username]```

按发件人地址/子串**过滤邮件**

```from -s [alice@example.com]```

**统计邮件数量**（仅 GNU mailutils）

```from -c```

**检查特定的邮箱文件**

```from -f [/var/mail/user]```

# SYNOPSIS

**from** [_-f file_] [_-s sender_] [_user_]

# PARAMETERS

_USER_
> 要为其查看邮件的用户名（读取该用户的系统邮箱）。

**-s** _SENDER_
> 只显示 From 地址匹配给定字符串的邮件头。_注意：_ 这**不会**显示主题行。

**-f** _FILE_
> 从指定的邮箱文件读取，而不是默认的系统邮箱。

**-c**
> 仅输出邮件数量。_仅 GNU mailutils 支持_；BSD/OpenBSD 的 **from** 中不可用。

**-d**, **--debug**
> 输出调试信息。_仅 GNU mailutils 支持。_

**-V**, **--version**
> 显示版本信息。_仅 GNU mailutils 支持。_

# DESCRIPTION

**from** 显示邮箱中每封邮件的邮件头，说明邮件来自谁（视实现而定，也可能包含主题和日期）。它读取系统邮箱（通常是 /var/mail/username）并每封邮件打印一行。

该工具无需打开完整的邮件客户端即可快速了解待处理邮件概况。配合 **-s** 可将输出过滤为发件人匹配给定地址或子串的邮件。它适合在 shell 脚本、cron 任务或终端快速检查中确认邮件状态。

# CAVEATS

只支持 mbox 格式的邮箱。可能无法用于现代邮件投递系统（Maildir、IMAP）。仅限于存储在传统 Unix mbox 文件中的本地邮件。

# HISTORY

**from** 是源自 4.2BSD 的经典 **BSD 工具**，用于查看本地邮件。它早于现代邮件系统出现，处理的是传统 Unix mbox 格式文件。

# INSTALL

```pacman: sudo pacman -S mailutils```

```apk: sudo apk add mailutils```

```zypper: sudo zypper install mailutils```

```brew: brew install mailutils```

```nix: nix profile install nixpkgs#mailutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mail](/man/mail)(1), [biff](/man/biff)(1), [mailx](/man/mailx)(1), [sendmail](/man/sendmail)(1)
