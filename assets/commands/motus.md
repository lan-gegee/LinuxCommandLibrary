# TAGLINE

极其简单的安全密码生成器

# TLDR

**生成一个易记的口令短语**

```motus```

**生成指定长度的**随机密码

```motus random -l [length]```

**生成一个数字 PIN**

```motus pin -l [digits]```

**分析密码强度**

```motus --analyze "[password]"```

# SYNOPSIS

**motus** [_command_] [_options_]

# PARAMETERS

**random**
> 生成一个随机字符串。

**pin**
> 生成一个数字 PIN。

**-l**, **--length** _N_
> 生成的密码或 PIN 的长度。

**--analyze**
> 为熵评分并标记弱密码选择。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**motus** 是一个命令行密码生成器，可以使用 EFF 词表、随机字符序列或数字 PIN 创建安全且易记的口令短语。生成的密码会自动复制到剪贴板。

可自定义选项包括单词数量、分隔符、大小写以及是否包含符号/数字。**--analyze** 选项会为密码的熵评分，并对弱选择发出警告。

# CAVEATS

剪贴板支持需要系统上有剪贴板提供程序。在无头（headless）环境中请使用 **--no-clipboard**。

# HISTORY

**motus** 由 **oleiade** 创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#motus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [pwgen](/man/pwgen)(1)
