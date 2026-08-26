# TAGLINE

从 PPD 文件中提取可翻译字符串

# TLDR

**提取字符串到 PO 文件**

```ppdpo -o [messages.po] [driver.drv]```

**指定包含目录进行提取**

```ppdpo -I [/path/to/includes] -o [strings.po] [file.drv]```

**提取为 macOS strings 格式**

```ppdpo -o [strings.strings] [file.drv]```

# SYNOPSIS

**ppdpo** [_options_] _source-file_

# PARAMETERS

_source-file_
> 输入的 PPDC 源文件（.drv）。

**-o** _output-file_
> 输出文件。支持的扩展名：GNU gettext 格式为 .po 或 .po.gz，macOS strings 格式为 .strings。

**-D** _name[=value]_
> 设置源文件中使用的命名变量，等同于 #define 指令。

**-I** _include-directory_
> 指定备用的包含目录。可以多次使用。

# DESCRIPTION

**ppdpo** 从 PPDC 源文件中提取 UI 字符串，生成用于本地化的 GNU gettext PO（Portable Object）文件或 macOS strings 文件。提取的字符串包括选项名称、组标签和其他用户可见文本，翻译人员可以将它们本地化为不同语言。

生成的 PO 文件遵循标准 gettext 格式，可以用 poedit 或 Weblate 等翻译工具编辑。翻译完成后，本地化字符串会使用 ppdc 和 ppdmerge 重新编译回 PPD 文件。

# CAVEATS

仅适用于 CUPS。已弃用，将在未来的 CUPS 版本中移除。

# HISTORY

ppdpo 是 **CUPS** 的组成部分，用于支持 PPD 本地化。

# INSTALL

```apt: sudo apt install cups-ppdc```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppdc](/man/ppdc)(1), [ppdmerge](/man/ppdmerge)(1), [ppdhtml](/man/ppdhtml)(1), [ppdi](/man/ppdi)(1), [gettext](/man/gettext)(1)
