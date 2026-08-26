# TAGLINE

在命令行使用 CSS 选择器解析和查询 HTML

# TLDR

从 stdin **按选择器过滤元素**

```cat [file.html] | pup '[selector]'```

**提取**匹配元素的**文本内容**

```cat [file.html] | pup '[selector] text{}'```

**提取属性值**（如 `href`）

```cat [file.html] | pup '[selector] attr{href}'```

**从文件而非 stdin 读取**

```pup -f [file.html] '[selector]'```

**解析从 URL 获取的 HTML**

```curl -s [url] | pup '[selector]'```

**以 JSON 输出匹配的元素**

```cat [file.html] | pup '[selector] json{}'```

**为匹配的元素编号**

```cat [file.html] | pup -n '[selector]'```

**以 4 空格缩进和彩色输出美化打印**

```cat [file.html] | pup -c --indent 4 '[selector]'```

**限制打印的嵌套深度**

```cat [file.html] | pup -l [2] '[selector]'```

# SYNOPSIS

**pup** [_options_] ['_selectors_ [_display-function_]']

# PARAMETERS

**-f**, **--file** _FILE_
> 从 _FILE_ 而非 stdin 读取 HTML。

**-c**, **--color**
> 为输出着色。

**-p**, **--plain**
> 不对输出进行 HTML 转义。

**--pre**
> 保留空白字符（在 `<pre>`/`<code>` 内很有用）。

**-i**, **--indent** _N_|_CHAR_
> 以 _N_ 个空格（或指定字符）缩进。

**-l**, **--limit** _N_
> 将输出的嵌套深度限制为 _N_ 层。

**-n**, **--number**
> 打印匹配元素的数量而不是元素本身。

**--charset** _ENCODING_
> 强制指定输入的字符编码（默认：自动检测）。

**-h**, **--help**
> 显示帮助。

**--version**
> 显示版本。

# SELECTORS AND DISPLAY FUNCTIONS

**CSS selectors**
> 标准 CSS 语法——`div.class`、`#id`、`a[href^="http"]`、`ul > li:first-child`、`tr:nth-child(even)` 等。多个选择器可用空格串联，以深入嵌套结构。

**text{}**
> 按深度优先顺序输出每个匹配元素的文本内容。

**attr{**_NAME_**}**
> 输出每个匹配元素的 _NAME_ 属性值。

**json{}**
> 将匹配的元素输出为 `{tag, attrs, children, text}` 对象组成的 JSON 数组。

**slice{**_N_**}** / **slice{**_N:M_**}**
> 仅返回第 _N_ 个匹配元素（或第 _N_ 到第 _M_-1 个）。

# DESCRIPTION

**pup** 是 **jq** 在 HTML 领域的对等工具——它从 stdin（或通过 `-f` 从文件）读取 HTML 文档，应用 CSS 风格的选择器来过滤元素，并可选地运行显示函数（`text{}`、`attr{…}`、`json{}`、`slice{…}`）将匹配结果投影成你想要的形式。它是一个没有运行时依赖的单个静态 Go 二进制文件，非常适合抓取流水线和 Makefile。

由于它支持大部分 CSS3（包括常见伪类），许多抓取问题可以简化为一条管道：`curl | pup 'selector json{}' | jq`。

# CAVEATS

pup 会将全部输入读入内存——不适合处理数十 GB 的 HTML。上游最后一次发布是在 2016 年；分支 `eiriklv/pup` 以及若干可直接替代的工具（`htmlq`、`xq`、`xidel`）提供了 XPath 或 CSS4 选择器等更新的特性。

# HISTORY

**pup** 由 **Eric Chiang** 使用 **Go** 编写。其语法明确仿照 **jq** 设计：将同样的"查询字符串 + 可选显示函数"思维模型应用于 HTML。

# INSTALL

```apt: sudo apt install pup```

```apk: sudo apk add pup```

```brew: brew install pup```

```nix: nix profile install nixpkgs#pup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [htmlq](/man/htmlq)(1), [xidel](/man/xidel)(1), [curl](/man/curl)(1)
