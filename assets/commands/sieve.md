# TAGLINE

用 Sieve 语言过滤邮件

# TLDR

**编译并检查** Sieve 脚本中的错误

```sieve --compile-only [path/to/script.sieve]```

**编译并转储**反汇编的 Sieve 代码

```sieve --dump [path/to/script.sieve]```

对邮箱**运行 Sieve 脚本**

```sieve [path/to/script.sieve] [path/to/mailbox]```

以详细输出进行**过滤**

```sieve --verbose [path/to/script.sieve] [path/to/mailbox]```

设置用于跟踪的**调试级别**

```sieve --debug=[trace4] [path/to/script.sieve]```

# SYNOPSIS

**sieve** [_options_] _script_ [_mailbox_]

# PARAMETERS

**-c**, **--compile-only**
> 编译脚本后退出，不执行。用于语法检查。

**-D**, **--dump**
> 编译脚本并把反汇编的 Sieve 代码输出到终端。

**-v**, **--verbose**
> 提高详细级别。

**--debug=**_level_
> 设置调试级别。Sieve 特有级别：**trace1**（优化前的解析树）、**trace2**（优化后的解析树）、**trace3**（解析器跟踪）、**trace4**（执行的测试和动作）、**trace9**（每条指令的执行）。

**--no-compile-only**
> 执行脚本（禁用仅编译模式）。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**sieve** 是一个邮件过滤工具，使用 Sieve 语言（RFC 5228）编写的脚本处理邮件。Sieve 是一种领域专用语言，设计用于在投递时过滤邮件，支持将邮件归档到文件夹、丢弃垃圾邮件、转发和休假自动回复等动作。

Sieve 语言支持对邮件头和内容的条件分支与模式匹配，但其基础规范有意不提供变量和循环，以防止程序失控运行。针对基础标准的扩展增加了变量、include 文件和高级字符串操作等特性。

sieve 可以只编译脚本检查错误而不执行，也可以处理实际的邮箱。它通常与 Dovecot（通过 Pigeonhole）或 GNU Mailutils 等邮件服务器配合使用。

# CAVEATS

出于安全考虑，Sieve 语言有刻意的限制：基础规范中没有变量和循环。部署前应使用 **--compile-only** 充分测试脚本。在过滤已有邮箱时，错误的脚本可能导致意外的邮件删除。在对生产邮箱应用过滤器之前，尽量先使用可用的模拟模式。

# HISTORY

Sieve 语言最初由 IETF 在 **RFC 3028**（2001 年 1 月）中标准化，基础规范随后在 **RFC 5228**（2008 年）中更新。GNU Mailutils 的实现在其邮件处理套件中提供了 **sieve** 命令。Dovecot 的 Pigeonhole 项目提供了另一个流行实现，其 **sieve-filter** 命令用于服务器端过滤。

# INSTALL

```apt: sudo apt install mailutils```

```pacman: sudo pacman -S mailutils```

```apk: sudo apk add mailutils```

```zypper: sudo zypper install mailutils```

```brew: brew install mailutils```

```nix: nix profile install nixpkgs#mailutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dovecot](/man/dovecot)(1), [procmail](/man/procmail)(1), [maildrop](/man/maildrop)(1)
