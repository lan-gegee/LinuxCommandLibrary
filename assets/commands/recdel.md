# TAGLINE

从 GNU recutils 数据库中删除记录

# TLDR

**删除匹配的记录**

```recdel -e "[Name = 'John']" [file.rec]```

**按记录类型删除**

```recdel -t [Type] -e "[condition]" [file.rec]```

**删除前要求确认**

```recdel -c -e "[Status = 'obsolete']" [file.rec]```

**删除前 N 条匹配记录**

```recdel -n [1] -e "[condition]" [file.rec]```

# SYNOPSIS

**recdel** [_options_] [_file_]

# PARAMETERS

**-t**, **--type** _type_
> 记录类型。

**-e**, **--expression** _expr_
> 选择表达式。

**-n**, **--num** _n_
> 删除前 n 条记录。

**-c**, **--confirm**
> 请求确认。

**-i**, **--case-insensitive**
> 不区分大小写匹配。

# DESCRIPTION

**recdel** 从 GNU recutils 纯文本数据库文件中删除与给定选择表达式匹配的记录。它支持与 **recsel** 相同的表达式语法，包括相等比较、正则匹配、比较运算符和逻辑组合，从而可以精确指定要删除的记录。

默认情况下它直接修改原文件，但可以将输出重定向到标准输出以便安全预览。**-c** 标志在每次删除前提示确认，**-n** 将操作限制为前 N 条匹配记录。属于 GNU recutils 工具集。

# EXAMPLES

```bash
# Delete by condition
recdel -e "Status = 'deleted'" items.rec

# Delete specific type
recdel -t Contact -e "Email ~ 'spam'" contacts.rec

# Delete with confirmation
recdel -c -e "Price < 0" products.rec

# Delete first match only
recdel -n 1 -e "Name = 'Test'" data.rec

# Dry run (output to stdout)
recdel -e "old = 'yes'" file.rec | less
```

# EXPRESSIONS

```
=       - Equal
!=      - Not equal
~       - Regex match
<, >    - Comparison
&&, ||  - Logical operators
```

# CAVEATS

直接修改原文件。批量删除前请先备份。属于 GNU recutils。

# HISTORY

recdel 是 **Jose E. Marchesi** 开发的 **GNU recutils** 的组成部分，用于基于文本的数据库管理。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recsel](/man/recsel)(1), [recins](/man/recins)(1), [recset](/man/recset)(1), [rec2csv](/man/rec2csv)(1)
