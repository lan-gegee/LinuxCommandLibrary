# TAGLINE

从文档中剥离 LaTeX 命令

# TLDR

**从文件中移除 LaTeX 命令**

```detex [document.tex]```

**处理并输出到文件**

```detex [document.tex] > [output.txt]```

**只处理单个文件**，不跟随 \\input 和 \\include

```detex -n [document.tex]```

**无论内容如何都强制使用 LaTeX 模式**

```detex -l [document.tex]```

**用占位词替换数学公式**，保持句子可读

```detex -r [document.tex]```

**输出单词列表**（每行一个单词，例如用于统计）

```detex -w [document.tex] | wc -l```

# SYNOPSIS

**detex** [**-clnstw**] [**-e** _environment-list_] [_file_...]

# PARAMETERS

**-c**
> 在 LaTeX 模式下，回显 \\cite、\\ref 和 \\pageref 宏的参数。

**-e** _environment-list_
> 要忽略的环境列表（逗号分隔），替代默认值：array、eqnarray、equation、longtable、picture、tabular、verbatim。

**-l**
> 强制按 LaTeX 模式处理。

**-n**
> 不跟随 \\input 和 \\include 命令（仅处理单个文件）。

**-r**
> 用占位词 "noun" 和 "verbs" 替换数学公式，保持句子可读。

**-s**
> 用空格替换控制序列（旧行为；可能破坏带变音符的单词）。

**-t**
> 强制按 plain TeX 模式处理。

**-w**
> 每行输出一个单词。

# DESCRIPTION

**detex** 从文档中剥离 LaTeX 和 TeX 命令，留下纯文本。这对拼写检查、字数统计、文本分析以及从 LaTeX 源文件中提取可读内容很有用。

该工具能处理标准 LaTeX 结构：命令、环境、注释和特殊字符。数学模式的内容会被移除（可用 **-r** 替换为可读的占位词）。默认情况下 detex 会跟随 \\input 和 \\include 指令处理多文件文档，并借助 TEXINPUTS 环境变量定位这些文件；**-n** 可禁用此行为。

输出为不含标记的文档文本，适合通过管道交给拼写检查器、文字处理器或文本分析工具。

# CAVEATS

复杂或非标准的 LaTeX 可能无法正确处理。某些宏包定义的命令 detex 无法识别。移除数学内容可能影响技术文档的上下文。该工具不会对参考文献或索引条目做特殊处理。

# HISTORY

detex 最初由普渡大学计算机科学系的 **Daniel Trinkle** 编写。自 **20 世纪 80 年代**起它就是 TeX 发行版中的标准工具，如今以 **OpenDetex** 的名义维护。虽然年代久远，它在基础的 LaTeX 转文本场景中仍然实用。

# INSTALL

```apt: sudo apt install texlive-binaries```

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [aspell](/man/aspell)(1), [pandoc](/man/pandoc)(1), [tex](/man/tex)(1)

# RESOURCES

```[Source code](https://github.com/pkubowicz/opendetex)```

<!-- verified: 2026-07-11 -->
