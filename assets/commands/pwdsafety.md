# TAGLINE

用于检查密码安全性的命令行工具

# TLDR

**从标准输入检查密码**

```echo "[password]" | pwdsafety```

# SYNOPSIS

**pwdsafety** [_options_]

# DESCRIPTION

**pwdsafety** 是一个命令行工具，从标准输入读取密码并评估其安全性。评分综合了多项检查：密码（或其反转）是否出现在内置的弱密码字典中，是否包含大写字母、小写字母、数字和符号，密码长度，以及 Shannon 熵计算。

该工具会输出数值评分，并说明哪些规则通过或未通过。当评分不高于 68 时，**pwdsafety** 还会建议一个随机的更强密码。

# EXIT STATUS

密码评估成功时返回 **0**（无论评分如何），输入错误时返回非零值。

# CAVEATS

不会存储、记录或传输任何密码信息——评估完全在本地进行。只从标准输入读取，因此在 shell 命令行上提供的密码会出现在进程列表和 shell 历史中；请改为从安全来源管道传入。

# HISTORY

**pwdsafety** 由 **edoardottt** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#pwdsafety```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [pwgen](/man/pwgen)(1)
