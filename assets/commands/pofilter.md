# TAGLINE

过滤 PO 文件中的翻译错误

# TLDR

**检查常见错误**

```pofilter -t [check] [input.po] [output.po]```

**列出可用的检查项**

```pofilter --list```

**检查快捷键**

```pofilter -t accelerators [input.po] [output.po]```

**检查 printf 格式**

```pofilter -t printf [input.po] [output.po]```

**多项检查**

```pofilter -t escapes -t variables [input.po] [output.po]```

# SYNOPSIS

**pofilter** [_options_] _input_ _output_

# PARAMETERS

**-t**, **--test** _test_
> 要运行的测试。

**-l**, **--language** _lang_
> 目标语言。

**--excludefilter** _filter_
> 排除特定测试。

**--list**
> 列出可用的测试。

**-i**, **--input** _path_
> 输入文件或目录。

**-o**, **--output** _path_
> 输出文件或目录。

# DESCRIPTION

**pofilter** 用于过滤 PO 文件以找出翻译错误。它会检查缺失变量、标点不一致、编码问题等常见问题。

它是 Translate Toolkit 的一部分。

# EXAMPLES

```bash
# List all available checks
pofilter --list

# Check for variables
pofilter -t variables translations.po errors.po

# Check escapes and printf
pofilter -t escapes -t printf input.po output.po

# Exclude specific check
pofilter --excludefilter=blank input.po output.po

# Process directory
pofilter -t all locale/ errors/
```

# COMMON CHECKS

```
variables   - Check variable placeholders
printf      - Check printf format strings
accelerators - Check keyboard accelerators
escapes     - Check escape sequences
newlines    - Check newline consistency
```

# CAVEATS

输出只包含有问题的条目。是 Translate Toolkit 的一部分。

# HISTORY

pofilter 由 **Translate House** 开发，是用于翻译质量保证的 **Translate Toolkit** 的组成部分。

# SEE ALSO

[msgfmt](/man/msgfmt)(1), [pocount](/man/pocount)(1)
