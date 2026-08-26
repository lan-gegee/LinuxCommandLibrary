# TAGLINE

邮件头提取与处理工具

# TLDR

**从邮件提取头部**

```formail -x [Subject:] < [email.txt]```

**向邮件添加头部**

```formail -a "[X-Custom: value]" < [email.txt]```

**将 mbox 拆分为单封邮件**

```formail -s [command] < [mbox]```

**提取 From 行**

```formail -x From: < [email.txt]```

**强制添加头部**

```formail -A "[X-Custom: value]" < [email.txt]```

**生成自动回复**

```formail -r < [email.txt]```

# SYNOPSIS

**formail** [_options_] [_output_] < _input_

# PARAMETERS

**-x** _header_
> 提取特定头部。

**-X** _header_
> 连同续行一起提取头部。

**-a** _header_
> 若不存在则添加头部。

**-A** _header_
> 总是添加头部。

**-i** _header_
> 替换头部。

**-u** _header_
> 使头部唯一。

**-r**
> 生成回复头部。

**-s** _command_
> 拆分并用命令处理。

**-b**
> 不转义正文中 "From " 开头的行。

**-n** _count_
> 只输出前 n 封邮件。

# DESCRIPTION

**formail** 是 procmail 套件中的邮件处理工具。它可以提取头部、添加或修改头部、拆分 mbox 文件，并帮助生成自动回复。

该工具从 stdin 读取并写入 stdout，专为在管道和 procmail 配方中使用而设计。它能够处理 RFC 822 邮件格式的各种细节。

# CAVEATS

属于已不再积极开发的 procmail 套件。MIME 处理能力有限。复杂头部可能需要仔细提取。新项目请考虑现代替代品。

# HISTORY

formail 由 **Stephen van den Berg** 在 **1990** 年代作为 **procmail** 邮件处理套件的一部分开发。虽然 procmail 已不再活跃维护，formail 在邮件处理脚本中仍然有用。

# INSTALL

```apt: sudo apt install procmail```

```dnf: sudo dnf install procmail```

```zypper: sudo zypper install procmail```

```brew: brew install procmail```

```nix: nix profile install nixpkgs#procmail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[procmail](/man/procmail)(1), [mail](/man/mail)(1), [mailx](/man/mailx)(1)
