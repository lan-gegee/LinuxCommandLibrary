# TAGLINE

在把其余行传给其他命令的同时保留文件的第一行

# TLDR

**排序文件并保留表头**

```keep-header [file] -- sort```

**用 grep 过滤并保留表头**

```keep-header [file] -- grep [pattern]```

**通过管道串联多个命令**

```keep-header [file] -- sort | head -20```

# SYNOPSIS

**keep-header** _file_ **--** _command_ [_args_...]

# DESCRIPTION

**keep-header** 在将文件的其余行传给另一个命令处理时，保留文件的第一行（表头）。它适合处理 CSV 或 TSV 文件，让你在对数据排序或过滤时不会丢失列标题。

# SEE ALSO

[head](/man/head)(1), [tail](/man/tail)(1), [sort](/man/sort)(1)
