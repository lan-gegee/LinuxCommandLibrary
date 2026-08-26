# TAGLINE

用于迭代的 Shell 循环结构

# TLDR

**遍历**显式列表

```for item in [a b c]; do echo "$item"; done```

**循环**处理匹配的文件

```for file in *.txt; do cat "$file"; done```

用花括号展开**循环**数值范围

```for i in {1..10}; do echo "$i"; done```

使用 C 风格计数器**循环**（bash、ksh、zsh）

```for ((i=0; i<10; i++)); do echo "$i"; done```

**遍历**位置参数

```for arg do echo "$arg"; done```

**遍历**数组元素（bash、ksh、zsh）

```for x in "${[array][@]}"; do echo "$x"; done```

**循环**处理命令输出，每次迭代取一个词

```for user in $(cut -d: -f1 [/etc/passwd]); do echo "$user"; done```

# SYNOPSIS

**for** _name_ [**in** _words_]; **do** _commands_; **done**

**for** **((** _init_; _condition_; _update_ **))**; **do** _commands_; **done**

# PARAMETERS

_name_
> 依次被赋予每个条目的变量。循环结束后它保持为最后一个值。

_words_
> 展开完成后要迭代的列表。如果省略 **in** _words_，则循环遍历位置参数，如同写了 **in "$@"** 一样。

_commands_
> 循环体，每处理一个条目执行一次。

**in**
> 引出单词列表。

**do**
> 开始循环体。

**done**
> 结束循环。

# DESCRIPTION

**for** 遍历一个单词列表，把每个词赋给一个变量并对每个词执行一次循环体。它是 Shell 解析器处理的保留字，而非外部命令。

单词列表由 Shell 的常规展开产生，这正是其灵活性的来源：花括号展开（**{1..10}**）生成序列，路径名展开（***.txt**）生成文件名，命令替换（**$(...)**）把其他程序的输出变成条目，而 **"${array[@]}"** 给出数组元素。关键在于列表在第一次迭代前就完全展开完毕，因此它是一组固定的单词而不是流。

完全省略 **in** 是一种有用的简写：**for arg do ... done** 会遍历 **"$@"**（脚本或函数的参数），并正确保留含空格的参数。

C 风格的 **for ((init; condition; update))** 形式是另一种独立结构，做的是算术运算而非单词迭代。它不是 POSIX 标准，但在 bash、ksh 和 zsh 中可用；当需要带计算边界的计数器时，这种写法更清晰。

循环的退出状态是最后执行的命令的状态；如果循环体从未执行，则为 **0**。**break** 跳出循环，**continue** 跳到下一个条目。

# CAVEATS

单词列表中未加引号的 **$(command)** 会按空白而非按行切分，且每个结果词还会再做通配符展开。这使得 **for line in $(cat file)** 对任何行中含空格或通配符的文件都是错误的：请用 **while IFS= read -r line; do ...; done < file** 逐行读取。

循环体内务必给变量加引号（**"$item"**），否则含空格的文件名在使用时会被再次拆分。

如果通配符匹配不到任何内容，Shell 默认会把模式本身留在列表里，因此在空目录中 **for f in *.txt** 会以字面字符串 ***.txt** 执行一次。可用 **[ -e "$f" ]** 加以防护，或在 bash 中设置 **shopt -s nullglob**。

由于列表是预先展开的，对超大 glob 或命令输出使用 **for** 循环会先把整个列表构建在内存中。输入非常大时请改用 **while read** 循环或 **find -exec** / **xargs**。

循环变量会泄漏：**done** 之后它仍然保留值，作用域并不限于循环内部。

# HISTORY

**for** 可追溯到 **Bourne shell**（**1977** 年），并被 POSIX 标准化。算术形式 **for ((...))** 来自 **Korn shell**，后来被 bash 在 **2.04** 版中采纳，为 C 程序员提供了熟悉的计数循环。

# SEE ALSO

[while](/man/while)(1), [until](/man/until)(1), [do](/man/do)(1), [done](/man/done)(1), [break](/man/break)(1), [continue](/man/continue)(1), [seq](/man/seq)(1), [xargs](/man/xargs)(1), [bash](/man/bash)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs)```

<!-- verified: 2026-07-16 -->
