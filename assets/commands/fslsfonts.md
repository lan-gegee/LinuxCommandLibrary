# TAGLINE

列出 X 字体服务器中的字体

# TLDR

**列出所有字体**

```fslsfonts```

**列出匹配模式的字体**

```fslsfonts -fn '[*-courier-*]'```

**显示长格式列表**

```fslsfonts -l```

从特定服务器**列出字体**

```fslsfonts -server [hostname:7100]```

**多列显示字体**

```fslsfonts -C```

# SYNOPSIS

**fslsfonts** [_options_] [_pattern_]

# PARAMETERS

_PATTERN_
> 要匹配的字体模式。

**-fn** _PATTERN_
> 要列出的字体的 XLFD 模式（默认为 **\***）。

**-l**
> 长格式列表 —— 显示字体属性。可用 **-ll** 或 **-lll** 逐级获得更多细节。

**-m**
> 在长格式列表中包含字符的最小和最大边界。

**-C**
> 多列输出。

**-1**
> 单列输出（每行一个字体）。

**-w** _WIDTH_
> 设置 **-C** 使用的列宽（默认 79）。

**-n** _COLUMNS_
> 强制输出使用 _COLUMNS_ 列（隐含 **-C**）。

**-u**
> 输出不排序。

**-server** _HOST:PORT_
> 查询指定的字体服务器（如 **tcp/host:7100**、**unix/:7100**），而不是 **FONTSERVER** 环境变量指定的服务器。

# DESCRIPTION

**fslsfonts** 列出 X 字体服务器提供的字体。它查询字体服务器并以 XLFD（X Logical Font Description）格式显示匹配的字体名。

该工具有助于确定 X 应用可用的字体。模式可以匹配特定的字体家族、字重或字号。长格式会显示额外的字体属性。

fslsfonts 相当于字体服务器版的 xlsfonts（后者针对本地 X 字体）。

# CAVEATS

需要正在运行的 X 字体服务器。XLFD 模式可能比较复杂。在有了现代 fontconfig 之后用处有所下降。

# HISTORY

fslsfonts 是 **X Window System** 字体服务器工具的一部分。它查询 xfs 字体服务器 —— 这曾是跨 X 终端和工作站共享字体的标准方式。

# INSTALL

```apt: sudo apt install x11-xfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xlsfonts](/man/xlsfonts)(1), [xfs](/man/xfs)(1), [fc-list](/man/fc-list)(1)
