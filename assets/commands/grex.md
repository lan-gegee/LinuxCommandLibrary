# TAGLINE

根据示例字符串生成正则表达式

# TLDR

**从示例生成正则表达式**

```grex [foo] [bar] [baz]```

**将数字转换为** `\d`

```grex -d [test1] [test2]```

**将空白转换为** `\s` **、单词转换为** `\w`

```grex -s -w [example1] [example2]```

**忽略大小写匹配**

```grex -i [example1] [example2]```

**启用重复检测生成**

```grex -r [aaab] [aaac]```

**生成不带首尾锚点的正则**

```grex --no-anchors [examples...]```

**从文件读取示例**（每行一个）

```grex -f [examples.txt]```

# SYNOPSIS

**grex** [_options_] _test-strings_

# PARAMETERS

_TEST-STRINGS_
> 用于生成正则表达式的示例字符串。

**-d**, **--digits**
> 将 Unicode 十进制数字转换为 \d。

**-D**, **--non-digits**
> 将非数字字符转换为 \D。

**-s**, **--spaces**
> 将 Unicode 空白字符转换为 \s。

**-S**, **--non-spaces**
> 将非空白字符转换为 \S。

**-w**, **--words**
> 将 Unicode 单词字符转换为 \w。

**-W**, **--non-words**
> 将非单词字符转换为 \W。

**-i**, **--ignore-case**
> 生成忽略大小写的正则表达式。

**-e**, **--escape**
> 将所有非 ASCII 字符替换为 unicode 转义序列。

**-r**, **--repetitions**
> 检测重复的子字符串并将其转换为量词记法。

**--no-anchors**
> 移除 ^ 和 $ 锚点（默认会添加锚点）。

**--no-start-anchor**
> 仅移除 ^ 起始锚点。

**--no-end-anchor**
> 仅移除 $ 结束锚点。

**-f**, **--file** _FILE_
> 从文件读取测试字符串（每行一个）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grex** 根据用户提供的测试字符串生成正则表达式。它会分析输入示例并产出一个能匹配所有示例的正则表达式。默认情况下，生成的正则包含 ^ 和 $ 锚点。

该工具支持多种字符类转换（\d、\s、\w 及其反向形式）、重复检测和忽略大小写匹配。它适合快速创建正则表达式，免去手工分析模式的麻烦。

# CAVEATS

生成的正则可能过于具体或过于宽泛。通常需要手动调整。复杂模式可能需要更多示例。

# HISTORY

grex 由 **Peter M. Stahl** 创建，是一款通过基于示例的学习来简化正则表达式编写的命令行工具。

# INSTALL

```pacman: sudo pacman -S grex```

```zypper: sudo zypper install grex```

```brew: brew install grex```

```nix: nix profile install nixpkgs#grex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [sed](/man/sed)(1), [regex](/man/regex)(7)
