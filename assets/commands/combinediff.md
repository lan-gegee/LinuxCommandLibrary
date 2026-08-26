# TAGLINE

将两个增量补丁合并为一个

# TLDR

**合并两个补丁**

```combinediff [patch1.diff] [patch2.diff]```

**以自定义上下文行数合并**

```combinediff -U [5] [patch1.diff] [patch2.diff]```

**剥离路径组成部分**

```combinediff -p [1] [patch1.diff] [patch2.diff]```

**忽略空白变化**

```combinediff -w [patch1.diff] [patch2.diff]```

**解压 gzip 压缩的补丁**

```combinediff -z [patch1.diff.gz] [patch2.diff.gz]```

# SYNOPSIS

**combinediff** [_options_] _diff1_ _diff2_

# DESCRIPTION

**combinediff** 创建一个表示两个 diff 之和的统一 diff。第二个补丁必须是相对于应用第一个补丁之后的文件。属于 patchutils 软件包的一部分。

# PARAMETERS

**-p** _n_, **--strip-match** _n_
> 比较文件名时忽略前 n 个路径组成部分

**-U** _n_, **--unified** _n_
> 显示 n 行上下文

**-d** _pat_, **--drop-context** _pat_
> 匹配模式的文件不保留上下文

**-q**, **--quiet**
> 抑制输出

**-i**, **--ignore-case**
> 忽略大小写进行比较

**-w**, **--ignore-all-space**
> 忽略空白变化

**-b**, **--ignore-space-change**
> 忽略空白数量的变化

**-B**, **--ignore-blank-lines**
> 忽略空行的变化

**-z**, **--decompress**
> 解压 .gz 和 .bz2 文件

**--interpolate**
> 改为以 interdiff 方式运行

**--help**
> 显示帮助

**--version**
> 显示版本

# REQUIREMENTS

输入的补丁必须严格按增量顺序排列。要获得最佳结果至少需要 3 行上下文。输出始终是统一格式。

# CAVEATS

需要干净的 GNU diff 输出。属于 patchutils 软件包（非预装）。手工编辑过的补丁请先用 recountdiff 修正。

# INSTALL

```apt: sudo apt install patchutils```

```dnf: sudo dnf install patchutils```

```pacman: sudo pacman -S patchutils```

```apk: sudo apk add patchutils```

```zypper: sudo zypper install patchutils```

```brew: brew install patchutils```

```nix: nix profile install nixpkgs#patchutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [patch](/man/patch)(1), [interdiff](/man/interdiff)(1)

# RESOURCES

```[Source code](https://github.com/twaugh/patchutils)```

<!-- verified: 2026-06-22 -->
