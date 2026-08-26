# TAGLINE

Shell 条件语句

# TLDR

**基本 if 语句**

```if [[ condition ]]; then command; fi```

**If-else**

```if [[ -f file ]]; then echo "exists"; else echo "missing"; fi```

**If-elif-else**

```if [[ $x -eq 1 ]]; then cmd1; elif [[ $x -eq 2 ]]; then cmd2; else cmd3; fi```

**测试文件是否存在**

```if [[ -e file ]]; then echo "found"; fi```

**测试字符串相等**

```if [[ "$a" == "$b" ]]; then echo "equal"; fi```

**测试命令退出状态**

```if grep -q "pattern" file; then echo "found"; fi```

**数值比较**

```if [[ $count -gt 10 ]]; then echo "more than 10"; fi```

# SYNOPSIS

**if** _test-commands_; **then** _commands_; [**elif** _test-commands_; **then** _commands_;] [**else** _commands_;] **fi**

# PARAMETERS

_test-commands_
> 一组命令，其退出状态决定分支走向。退出状态为 0（成功）表示条件为真。

**then**
> 引出在前一条件为真时要执行的命令。

**elif**
> else-if 子句；在之前的条件均为假时测试另一个条件。

**else**
> 在所有之前的条件均为假时执行的命令。

**fi**
> if 块的结束。

# DESCRIPTION

**if** 是 Shell 内建的条件语句。它执行 _test-commands_ 列表，若退出状态为零（成功），则运行对应的 **then** 子句。若非零，则依次测试每个 **elif** 子句。如果没有任何条件成立且存在 **else** 子句，则执行其中的命令。

虽然 **if** 最常与 **test** 或 **[[ ]]** 表达式搭配使用，但任何命令都可以作为条件，因为判断依据是退出状态。例如，**if grep -q pattern file** 会根据 grep 是否找到匹配来分支。

# CAVEATS

Shell 内建命令。**[ ]** 和 **[[ ]]** 内部的空格必不可少（如 **[ "$a" = "$b" ]**，而非 **["$a"="$b"]**）。POSIX 兼容的测试语法是 **[ ]**，而 **[[ ]]** 是 bash/zsh 的扩展，额外支持模式匹配和正则表达式等特性。

# HISTORY

**if** 是标准的 **Unix shell** 构件，自最初的 Bourne shell 起就存在于所有符合 POSIX 的 Shell 中。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[test](/man/test)(1), [bash](/man/bash)(1), [while](/man/while)(1), [for](/man/for)(1)
