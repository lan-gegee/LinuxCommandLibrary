# TAGLINE

使用 CSS 选择器从 HTML 中提取数据

# TLDR

**按选择器提取元素**

```cat [page.html] | htmlq [.class-name]```

**获取属性值**

```htmlq -a href [a.link] < [page.html]```

**获取文本内容**

```htmlq -t [p] < [page.html]```

**美化输出 HTML**

```htmlq -p [body] < [page.html]```

**提取前先移除节点**

```htmlq --remove-nodes [.unwanted] [div.content] < [page.html]```

**通过 curl 从 URL 获取**

```curl -s [url] | htmlq [selector]```

# SYNOPSIS

**htmlq** [_options_] _selector_

# PARAMETERS

_SELECTOR_
> CSS 选择器。

**-a**, **--attribute** _ATTR_
> 仅返回所选元素的该属性值。

**-t**, **--text**
> 仅输出所选元素的文本内容。

**-p**, **--pretty**
> 美化输出的序列化 HTML。

**-b**, **--base** _URL_
> 将该 URL 作为相对链接的基准。

**-B**, **--detect-base**
> 从文档的 `<base>` 标签检测基准 URL。

**-f**, **--filename** _FILE_
> 输入文件（默认为标准输入）。

**-o**, **--output** _FILE_
> 输出文件（默认为标准输出）。

**-r**, **--remove-nodes** _SELECTOR_
> 在输出前移除匹配的节点。可多次指定。

**-w**, **--ignore-whitespace**
> 打印文本节点时，忽略仅含空白字符的节点。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**htmlq** 使用 CSS 选择器从 HTML 中提取数据。它就像 HTML 版的 jq，提供命令行下的 HTML 解析能力。

该工具从标准输入或文件读取 HTML，并输出匹配的元素。它支持提取文本、属性以及格式化后的 HTML。

# CAVEATS

不校验 HTML；格式错误的输入可能产生意外结果。CSS 选择器支持涵盖大多数常见模式，但可能不支持所有 CSS4 伪类选择器。输入会被完整读入内存，因此非常大的 HTML 文档处理起来可能较慢。

# HISTORY

htmlq 是一款命令行 HTML 查询工具，其灵感来自用于 JSON 处理的 jq。

# INSTALL

```pacman: sudo pacman -S htmlq```

```apk: sudo apk add htmlq```

```brew: brew install htmlq```

```nix: nix profile install nixpkgs#htmlq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pup](/man/pup)(1), [jq](/man/jq)(1), [xmllint](/man/xmllint)(1), [curl](/man/curl)(1)
