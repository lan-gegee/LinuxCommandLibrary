# TAGLINE

比较两个统一 diff 文件并生成表示差异的 diff

# TLDR

**显示两个补丁之间的差异**

```interdiff [old.patch] [new.patch]```

**创建用于从一个版本转换为另一个版本的补丁**

```interdiff [version1.patch] [version2.patch] > [upgrade.patch]```

**从补丁文件名中剥离前导路径组件**

```interdiff -p 1 [old.patch] [new.patch]```

**显示额外的上下文行**

```interdiff -U [3] [old.patch] [new.patch]```

**比较 gzip/bzip2 压缩的补丁**

```interdiff -z [old.patch.gz] [new.patch.gz]```

# SYNOPSIS

**interdiff** [_-U N_] [_-p N_] [_-d PAT_] [_-q_] [_-i_] [_-w_] [_-b_] [_-B_] [_-z_] _patch1_ _patch2_

# PARAMETERS

**-U** _N_, **--unified=**_N_
> 显示 N 行上下文（默认：3）。

**-p** _N_, **--strip-match=**_N_
> 匹配文件名时忽略前 N 个路径组件。

**-d** _PAT_, **--drop-context=**_PAT_
> 排除名称匹配模式 PAT 的文件的上下文。

**-i**, **--ignore-case**
> 比较时忽略大小写差异。

**-w**, **--ignore-all-space**
> 比较时忽略所有空白字符。

**-b**, **--ignore-space-change**
> 忽略空白字符数量的变化。

**-B**, **--ignore-blank-lines**
> 忽略仅由空行增删构成的变化。

**-z**, **--decompress**
> 自动解压 .gz 和 .bz2 补丁。

**-q**, **--quiet**
> 减少输出中的警告。

**--no-revert-omitted**
> 不还原第一个补丁中被第二个补丁省略的部分。

**--help**
> 显示用法信息。

**--version**
> 显示版本号。

# DESCRIPTION

**interdiff** 比较两个统一 diff 文件（补丁），并生成表示二者之间差异的 diff。这有助于了解一个补丁的两个版本之间改了什么，或用于创建增量补丁。

给定把 A 变为 B 的 patch1 和把 A 变为 C 的 patch2，interdiff 会生成把 B 变为 C 的补丁。这在审阅补丁修订版或在软件版本之间构建升级路径时很有用。

# CAVEATS

两个输入补丁必须是统一 diff 格式，不支持上下文 diff 格式。要获得有意义的结果，两个补丁必须作用于相同的基础文件。结构变化较大的复杂补丁可能产生令人困惑的输出。

# HISTORY

**interdiff** 是 **patchutils** 软件包的一部分，由 Tim Waugh 编写，约 **2001 年**首次发布。patchutils 工具集提供操作补丁文件的工具，满足软件开发和分发工作流中的常见需求。

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

[combinediff](/man/combinediff)(1), [diff](/man/diff)(1), [patch](/man/patch)(1)
