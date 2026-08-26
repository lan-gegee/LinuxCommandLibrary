# TAGLINE

逐词比较文件

# TLDR

**逐词比较两个文件**

```dwdiff [file1.txt] [file2.txt]```

**使用彩色输出**

```dwdiff -c [file1.txt] [file2.txt]```

**只显示更改**，抑制两个文件共有的词

```dwdiff -3 [file1.txt] [file2.txt]```

**显示行号**

```dwdiff -L [file1.txt] [file2.txt]```

**忽略大小写**差异

```dwdiff -i [file1.txt] [file2.txt]```

**将标点视为分隔符**，使词语切分更细

```dwdiff -P [file1.txt] [file2.txt]```

**打印变更统计**

```dwdiff -s [file1.txt] [file2.txt]```

**用 less 风格的高亮分页查看差异**

```dwdiff -l [file1.txt] [file2.txt] | less -R```

# SYNOPSIS

**dwdiff** [_options_] _file1_ _file2_

# PARAMETERS

**-c**[_spec_], **--color**[**=**_spec_]
> 为输出着色。可选的 _spec_ 可覆盖删除和插入的颜色。

**-l**, **--less-mode**
> 使用重叠打印（删除加下划线，插入加粗），适合通过管道传给 less -R。

**-L**[_width_], **--line-numbers**[**=**_width_]
> 在每行开头显示行号。

**-s**, **--statistics**
> 完成后打印词数和变更百分比。

**-i**, **--ignore-case**
> 比较词语时忽略大小写差异。

**-I**, **--ignore-formatting**
> 忽略粗体或下划线标记等格式变化。

**-d** _chars_, **--delimiters=**_chars_
> 视为词语分隔符的字符。

**-P**, **--punctuation**
> 使用标点字符作为分隔符。

**-W** _chars_, **--white-space=**_chars_
> 视为空白符的字符。

**-1**, **--no-deleted**
> 抑制从第一个文件中删除的词。

**-2**, **--no-inserted**
> 抑制在第二个文件中插入的词。

**-3**, **--no-common**
> 抑制两个文件共有的词，只留下更改。

**-C** _num_, **--context=**_num_
> 在每处更改周围显示 _num_ 行上下文。

**-A** _algo_, **--algorithm=**_algo_
> 比较算法：best、normal 或 fast。

**-w** _string_, **--start-delete=**_string_
> 标记删除文本开始的字符串（默认 `[-`）。

**-x** _string_, **--stop-delete=**_string_
> 标记删除文本结束的字符串（默认 `-]`）。

**-y** _string_, **--start-insert=**_string_
> 标记插入文本开始的字符串（默认 `{+`）。

**-z** _string_, **--stop-insert=**_string_
> 标记插入文本结束的字符串（默认 `+}`）。

**--diff-input**
> 读取 unified diff 输出而不是两个文件。

**--wdiff-output**
> 生成与 wdiff 兼容的输出。

# DESCRIPTION

**dwdiff** 逐词而非逐行地比较文件，更容易发现散文或文档中的细微变化。它会突出显示被删除的词（来自第一个文件）和新插入的词（在第二个文件中）。

该工具特别适合比较文本文档、译文或任何基于行的 diff 会产生混乱输出的内容。它能准确显示版本之间哪些词发生了变化。

# OUTPUT FORMAT

```
[-removed-] {+added+}
```

删除的文本用带减号的方括号显示，插入的文本用带加号的花括号显示。

# CAVEATS

最适合处理散文而非代码。大文件处理可能较慢。词边界取决于分隔符设置。对非英文文本或特殊字符可能需要调整。

# HISTORY

dwdiff 由 **G.P. Halkes** 编写，是较老的 wdiff 工具的改进替代品。它提供了更好的 Unicode 处理、彩色输出以及更灵活的词语分隔选项。

# INSTALL

```apt: sudo apt install dwdiff```

```brew: brew install dwdiff```

```nix: nix profile install nixpkgs#dwdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wdiff](/man/wdiff)(1), [diff](/man/diff)(1), [colordiff](/man/colordiff)(1), [vimdiff](/man/vimdiff)(1)

# RESOURCES

```[Homepage](https://os.ghalkes.nl/dwdiff.html)```

<!-- verified: 2026-07-14 -->
