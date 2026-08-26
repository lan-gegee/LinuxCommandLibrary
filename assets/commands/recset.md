# TAGLINE

更新 GNU recutils 数据库中的字段值

# TLDR

**更新字段值**

```recset -f [Field] -v "[new_value]" -e "[condition]" [file.rec]```

**为所有记录设置字段**

```recset -f [Status] -v "[active]" [file.rec]```

**更新特定类型**

```recset -t [Type] -f [Field] -v "[value]" -e "[condition]" [file.rec]```

**缺失时添加字段**

```recset -a -f [NewField] -v "[value]" [file.rec]```

# SYNOPSIS

**recset** [_options_] [_file_]

# PARAMETERS

**-t**, **--type** _type_
> 记录类型。

**-f**, **--field** _name_
> 要设置的字段。

**-v**, **--value** _value_
> 新值。

**-e**, **--expression** _expr_
> 选择表达式。

**-a**, **--add**
> 缺失时添加字段。

**-n**, **--num** _n_
> 更新前 n 条匹配记录。

# DESCRIPTION

**recset** 修改 GNU recutils 纯文本数据库文件中的字段值，基于选择表达式更新已有字段或添加新字段。它使用与 **recsel** 相同的表达式语法来定位特定记录，然后将指定字段设置为新值。

**-a** 标志只向尚不存在该字段的记录添加字段，**-n** 将更新限制为前 N 条匹配记录。不提供选择表达式时，文件中的所有记录都会被更新。文件会被原地修改。属于 GNU recutils 工具集。

# EXAMPLES

```bash
# Update matching records
recset -f Status -v "completed" -e "Status = 'pending'" tasks.rec

# Update all records
recset -f Updated -v "$(date)" data.rec

# Update specific type
recset -t Contact -f Phone -v "555-0000" -e "Name = 'John'" contacts.rec

# Add field if not exists
recset -a -f Category -v "General" -e "!Category" items.rec

# Update first match
recset -n 1 -f Priority -v "high" -e "Status = 'new'" tasks.rec
```

# CAVEATS

直接修改原文件。请谨慎使用选择表达式。属于 GNU recutils。

# HISTORY

recset 是 **Jose E. Marchesi** 开发的 **GNU recutils** 的组成部分，用于管理文本数据库。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recsel](/man/recsel)(1), [recins](/man/recins)(1), [recdel](/man/recdel)(1)
