# TAGLINE

过滤或统计相邻的重复行

# TLDR

**移除相邻的重复行**

```sort [file] | uniq```

**仅显示重复行**

```sort [file] | uniq -d```

**仅显示不重复的行**

```sort [file] | uniq -u```

**统计出现次数**

```sort [file] | uniq -c```

**比较时忽略大小写**

```sort [file] | uniq -i```

比较时**跳过前 N 个字段**

```sort [file] | uniq -f [N]```

比较时**跳过前 N 个字符**

```sort [file] | uniq -s [N]```

# SYNOPSIS

**uniq** [_options_] [_input_ [_output_]]

# PARAMETERS

**-c**, **--count**
> 在行首加上出现次数

**-d**, **--repeated**
> 仅打印重复行，每组一行

**-D**
> 打印所有重复行

**-u**, **--unique**
> 仅打印不重复的行（只出现一次）

**-i**, **--ignore-case**
> 比较时忽略大小写

**-f** _N_, **--skip-fields**=_N_
> 比较时跳过前 N 个字段

**-s** _N_, **--skip-chars**=_N_
> 比较时跳过前 N 个字符

**-w** _N_, **--check-chars**=_N_
> 只比较前 N 个字符

**-z**, **--zero-terminated**
> 行分隔符为 NUL 而不是换行符

# DESCRIPTION

**uniq** 从输入中过滤相邻的匹配行，将不重复的行写入输出。它只比较连续的行，因此输入通常需要先排序。

常与 **sort** 在管道中配合使用：**sort file | uniq** 可移除所有重复项。加上 **-c** 会显示频次计数，便于分析日志文件或查找常见模式。

**-d** 选项只显示出现超过一次的行，而 **-u** 只显示恰好出现一次的行。这是对数据的两种互斥视角。

字段和字符跳过选项允许在比较唯一性时忽略前缀（如时间戳或行号）。

# CAVEATS

uniq 只移除**相邻的**重复行。若不先排序，不相邻的重复项会保留。要进行真正的去重，请始终使用 **sort | uniq** 或 **sort -u**。

**sort -u** 通常比 **sort | uniq** 更高效，因为它在排序过程中就去除了重复项，而不是单独再处理一遍。

计数选项（**-c**）会在行首添加空格和计数值，后续使用可能需要再处理。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sort](/man/sort)(1), [comm](/man/comm)(1), [cut](/man/cut)(1), [wc](/man/wc)(1)
