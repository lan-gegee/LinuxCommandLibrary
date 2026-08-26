# TAGLINE

使用模板格式化 GNU recutils 记录

# TLDR

**用内联模板格式化记录**

```recsel [file.rec] | recfmt "{{Name}}: {{Email}}"```

**用模板文件格式化记录**

```recsel [file.rec] | recfmt -f [template.fmt]```

**选择并格式化特定记录类型**

```recsel -t [Type] [file.rec] | recfmt "{{Title}} by {{Author}}"```

# SYNOPSIS

**recfmt** [_options_] [_template_]

# PARAMETERS

**-f**, **--file** _FILENAME_
> 从文件而非命令行参数加载模板。

**--help**
> 打印帮助并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**recfmt** 将模板应用到从标准输入读取的记录上。字段通过 **{{FieldName}}** 这样的双花括号槽位引用。对每条输入记录，都会生成一份字段值替换后的模板副本。通常将 **recsel** 的输出通过管道传入 **recfmt** 使用。

属于 GNU recutils。

# EXAMPLES

```bash
# Simple format from recsel output
recsel contacts.rec | recfmt "Name: {{Name}}, Email: {{Email}}"

# From template file
recsel data.rec | recfmt -f report.fmt

# Specific record type with selection
recsel -t Book library.rec | recfmt "{{Title}} by {{Author}}"

# Combine with expression filtering
recsel -e "Status = 'active'" items.rec | recfmt "- {{Name}}"
```

# TEMPLATE SYNTAX

```
{{FieldName}}          - Substituted with field value
```

# TEMPLATE FILE

```
# report.fmt
=== {{Name}} ===
Email: {{Email}}
Phone: {{Phone}}
---
```

# CAVEATS

模板语法与其他模板系统不同。属于 GNU recutils。

# HISTORY

recfmt 是 **Jose E. Marchesi** 开发的 **GNU recutils** 的组成部分，用于灵活的记录格式化。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recsel](/man/recsel)(1), [rec2csv](/man/rec2csv)(1), [recins](/man/recins)(1), [recdel](/man/recdel)(1), [recset](/man/recset)(1)
