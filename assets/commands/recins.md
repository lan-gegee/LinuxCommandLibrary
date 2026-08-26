# TAGLINE

向 GNU recutils 数据库插入记录

# TLDR

**插入记录**

```recins -f [Name] -v "[John]" -f [Email] -v "[john@example.com]" [file.rec]```

**带类型插入**

```recins -t [Contact] -f [Name] -v "[Jane]" [file.rec]```

**从模板插入**

```echo "Name: John" | recins [file.rec]```

**存在则替换**

```recins -r -f [Name] -v "[John]" [file.rec]```

# SYNOPSIS

**recins** [_options_] [_file_]

# PARAMETERS

**-t**, **--type** _type_
> 记录类型。

**-f**, **--field** _name_
> 字段名。

**-v**, **--value** _value_
> 字段值。

**-r**, **--replace**
> 替换已有记录。

**-n**, **--name** _name_
> 设置记录描述符。

**-S**, **--sort** _field_
> 插入后排序。

# DESCRIPTION

**recins** 向 GNU recutils 纯文本数据库文件中添加新记录。字段和值可以在命令行上通过重复的 **-f** 和 **-v** 标志指定，也可以从标准输入以标准 recfile 格式（以空行分隔的键值对）通过管道传入。

**-t** 标志指定记录类型，**-r** 替换已有记录而不是追加，**-S** 在插入后对记录排序。文件不存在时会自动创建。属于 GNU recutils 工具集。

# EXAMPLES

```bash
# Insert single record
recins -f Name -v "Alice" -f Email -v "alice@example.com" contacts.rec

# With record type
recins -t Book -f Title -v "1984" -f Author -v "Orwell" library.rec

# Multiple fields
recins -t Product \
  -f Name -v "Widget" \
  -f Price -v "9.99" \
  -f Stock -v "100" \
  inventory.rec

# From stdin
cat << EOF | recins contacts.rec
Name: Bob
Email: bob@example.com
Phone: 555-1234
EOF
```

# CAVEATS

文件不存在时会创建。默认追加。属于 GNU recutils。

# HISTORY

recins 是 **Jose E. Marchesi** 开发的 **GNU recutils** 的组成部分，用于基于文本的数据库管理。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recsel](/man/recsel)(1), [recdel](/man/recdel)(1), [recset](/man/recset)(1)
