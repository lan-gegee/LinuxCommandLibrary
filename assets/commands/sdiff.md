# TAGLINE

并排比较与合并文件

# TLDR

**并排比较文件**

```sdiff [file1] [file2]```

**交互式合并**

```sdiff -o [output] [file1] [file2]```

**设置输出宽度**

```sdiff -w [120] [file1] [file2]```

**不显示相同行**

```sdiff -s [file1] [file2]```

**忽略大小写差异**

```sdiff -i [file1] [file2]```

**忽略空白字符变化**

```sdiff -b [file1] [file2]```

**忽略所有空白字符**

```sdiff -W [file1] [file2]```

**将制表符展开为空格输出**

```sdiff -t [file1] [file2]```

# SYNOPSIS

**sdiff** [_-o output_] [_-w width_] [_-sbBiW_] [_options_] _file1_ _file2_

# PARAMETERS

**-o** _FILE_, **--output** _FILE_
> 交互式合并并输出到指定文件。

**-w** _NUM_, **--width** _NUM_
> 输出宽度（列数）。

**-s**, **--suppress-common-lines**
> 不显示相同的行。

**-l**, **--left-column**
> 相同行只显示左列。

**-b**, **--ignore-space-change**
> 忽略空白字符数量的变化。

**-B**, **--ignore-blank-lines**
> 忽略空白行的变化。

**-i**, **--ignore-case**
> 不区分大小写进行比较。

**-W**, **--ignore-all-space**
> 忽略所有空白字符。

**-t**, **--expand-tabs**
> 将制表符展开为空格。

**--strip-trailing-cr**
> 去除行尾的回车符。

**-a**, **--text**
> 将所有文件视为文本文件。

**-d**, **--minimal**
> 寻找最小的变更集合。

**-H**, **--speed-large-files**
> 针对大文件使用启发式算法。

# DESCRIPTION

**sdiff** 并排比较两个文件。它以并列的两列显示对应的行，并用符号标记差异。

输出符号表示行之间的关系：空白（相同）、|（不同）、<（仅存在于左侧）、>（仅存在于右侧）。这种可视化格式让差异一目了然。

交互式合并模式（-o）从两个输入创建一个合并后的文件。在每个差异处，你可以选择：左侧（l）、右侧（r）、编辑左侧（el）、编辑右侧（er）或两者都保留（b）。这样可以手动解决差异。

宽度设置（-w）控制输出的列数。较窄的宽度会截断行；较宽的宽度显示更多内容。通常使用终端宽度（例如 -w 80 或 -w $COLUMNS）。

抑制相同行（-s）只显示差异，适合关注大部分内容相同的文件中的变化。

空白和大小写选项有助于比较那些存在格式差异但并无实质区别的文件。

# CAVEATS

二进制文件的显示效果不佳。非常长的行可能被截断。交互模式需要终端。宽文件需要宽终端或滚动查看。在脚本化方面功能不如 diff 丰富。

# HISTORY

**sdiff** 是 GNU diffutils 的一部分，由自由软件基金会开发。并排比较起源于 Unix 研究领域，在图形化 diff 工具出现之前就提供了直观的比较方式。GNU 版本增加了交互式合并模式和多种比较选项。

# INSTALL

```apt: sudo apt install diffutils```

```dnf: sudo dnf install diffutils```

```pacman: sudo pacman -S diffutils```

```apk: sudo apk add diffutils```

```zypper: sudo zypper install diffutils```

```brew: brew install diffutils```

```nix: nix profile install nixpkgs#diffutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [diff3](/man/diff3)(1), [cmp](/man/cmp)(1), [vimdiff](/man/vimdiff)(1)
