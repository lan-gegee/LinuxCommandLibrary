# TAGLINE

跳到循环的下一次迭代

# TLDR

在 for 循环中**跳到下一次迭代**

```for i in 1 2 3; do if [ "$i" -eq 2 ]; then continue; fi; echo "$i"; done```

在 while 循环中**根据条件跳过迭代**

```while read line; do [[ "$line" == "#"* ]] && continue; echo "$line"; done < [file.txt]```

**从外层循环继续**（跳过 2 层）

```for i in 1 2; do for j in a b; do [ "$j" = "a" ] && continue 2; echo "$i$j"; done; done```

**跳过对空行的处理**

```for file in *; do [ -z "$file" ] && continue; process "$file"; done```

# SYNOPSIS

**continue** [_n_]

# PARAMETERS

**n**
> 要跳出的外层循环层数。默认为 1（最内层循环）。必须是正整数。

# DESCRIPTION

**continue** 是一条 shell 内建命令，它会跳过外层 **for**、**while**、**until** 或 **select** 循环当前迭代中剩余的命令，直接进入该循环的下一次迭代。

不带参数调用时，continue 作用于最内层的循环。若给定数字参数 **n**，则从第 **n** 层外层循环继续，由内向外计数。这样可以跨越多层嵌套循环。

这条命令是控制循环流程的重要手段，尤其适合在某些条件下需要跳过处理但不想终止整个循环的场景。与完全退出循环的 **break** 不同，continue 只是移动到下一次迭代。

# CAVEATS

参数必须大于或等于 1。如果 **n** 大于外围循环的层数，continue 会作用于最外层循环。在循环之外使用 continue 会产生错误。该命令只影响紧邻的循环结构，不影响函数调用。

# HISTORY

continue 是自 **1979** 年最初的 Bourne shell 就存在的基本 shell 控制流语句。它沿袭了 C 等早期编程语言的惯例。指定循环层级的功能是为了在嵌套循环场景中提供更灵活的控制而加入的。

# SEE ALSO

[break](/man/break)(1), [for](/man/for)(1), [while](/man/while)(1), [bash](/man/bash)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)```

<!-- verified: 2026-07-11 -->
