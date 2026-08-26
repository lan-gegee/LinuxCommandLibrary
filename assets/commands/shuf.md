# TAGLINE

随机打乱输入行

# TLDR

**打乱文件的行序**

```shuf [file]```

**随机抽取 N 行**

```shuf -n [5] [file]```

**生成指定范围的随机数**

```shuf -i [1-100]```

**从范围内随机抽取 N 个数**

```shuf -i [1-100] -n [10]```

**打乱命令参数**

```shuf -e [item1] [item2] [item3]```

**以自定义分隔符输出**

```shuf -e -z [items] | xargs -0```

**重复输出**（有放回抽样）

```shuf -r -n [10] -e [a] [b] [c]```

**使用指定的随机源**

```shuf --random-source=[/dev/urandom] [file]```

# SYNOPSIS

**shuf** [_-n count_] [_-i range_] [_-e args_] [_-r_] [_options_] [_file_]

# PARAMETERS

**-n** _NUM_, **--head-count** _NUM_
> 最多输出 NUM 行。

**-i** _LO-HI_, **--input-range** _LO-HI_
> 生成 LO 到 HI 的数字。

**-e**, **--echo**
> 将参数视为输入行。

**-r**, **--repeat**
> 输出可以重复（有放回）。

**-z**, **--zero-terminated**
> 使用 NUL 作为行分隔符。

**-o** _FILE_, **--output** _FILE_
> 写入文件而不是标准输出。

**--random-source** _FILE_
> 从文件获取随机字节。

# DESCRIPTION

**shuf** 对输入行进行随机排列。它读取输入，打乱顺序，然后按随机序列输出所有行。

不带选项时，shuf 按随机顺序输出所有输入行。-n 选项将输出限制为打乱后的前 N 行，实际上相当于无放回的随机抽样。

输入范围模式（-i）生成连续数字并打乱它们。与 -n 组合即可从范围中选取随机数，适合生成彩票号码、随机 ID 或抽样。

回显模式（-e）对命令行参数而非文件行进行打乱，无需创建临时文件即可打乱小型列表。

重复模式（-r）支持有放回抽样，同一行可以在输出中多次出现，适合 bootstrap 抽样或模拟。

给定确定性的随机源时，random source 选项可以保证打乱结果可复现，便于测试。

# CAVEATS

会将全部输入载入内存，非常大的文件可能造成内存问题。默认随机性良好但非密码学安全。不加 -n 时会输出全部输入。与可能把相同行归为一组的 sort -R 不同。

# HISTORY

**shuf** 是 **GNU coreutils** 的一部分，提供命令行下的随机打乱功能。虽然 Unix 系统上早已有各种随机选取行的工具，shuf 凭借范围生成和抽样选项提供了更全面的打乱能力。

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

[sort](/man/sort)(1), [head](/man/head)(1), [tail](/man/tail)(1), [sample](/man/sample)(1)
