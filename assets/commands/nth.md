# TAGLINE

从输入中提取特定字段

# TLDR

**提取第 n 个字段**

```echo "[a b c]" | nth [2]```

**从 CSV 提取**

```nth -d "," [1] < [file.csv]```

**提取多个字段**

```nth [1] [3] [5] < [file.txt]```

**使用自定义分隔符**

```nth -d ":" [1] < [/etc/passwd]```

# SYNOPSIS

**nth** [_options_] _fields_ [_file_]

# PARAMETERS

_FIELDS_
> 要提取的字段编号（从 1 开始）。

**-d** _DELIMITER_
> 字段分隔符（默认：空白字符）。

**-0**
> 使用 null 作为输出分隔符。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nth** 从输入中提取特定字段，是 awk/cut 的简单替代品。

该工具高效地处理字段提取，语法比 awk 更简洁。

# CAVEATS

字段编号从 1 开始。比 awk 简单但功能较弱。

# HISTORY

nth 提供**简单的字段提取**功能，作为 awk 和 cut 的替代方案。

# INSTALL

```nix: nix profile install nixpkgs#nth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cut](/man/cut)(1), [awk](/man/awk)(1), [paste](/man/paste)(1)
