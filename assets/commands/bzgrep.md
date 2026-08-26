# TAGLINE

在 bzip2 压缩文件中搜索模式

# TLDR

在压缩文件中**搜索**

```bzgrep ["pattern"] [file.bz2]```

**不区分大小写**搜索

```bzgrep -i ["error"] [log.bz2]```

**统计**匹配数

```bzgrep -c ["pattern"] [file.bz2]```

**显示**行号

```bzgrep -n ["pattern"] [file.bz2]```

# SYNOPSIS

**bzgrep** [_grep-options_] [**-e**] _pattern_ [_filename_...]

# DESCRIPTION

**bzgrep** 对 bzip2 压缩文件调用 grep。如果未指定文件，则在必要时解压标准输入并将其送入 grep。否则，在必要时解压给定文件并送入 grep。

当以 **bzegrep** 或 **bzfgrep** 名称调用时，会分别使用 egrep 或 fgrep 代替 grep。也可以通过 **GREP** 环境变量覆盖 grep 程序。

# PARAMETERS

所有选项都直接传递给 grep：

**-i**
> 不区分大小写搜索

**-v**
> 反转匹配

**-n**
> 显示行号

**-c**
> 统计匹配数

**-l**
> 列出匹配的文件

**-e** _pattern_
> 使用 pattern 作为搜索模式（对以 - 开头的模式很有用）

**-H**
> 打印文件名

**-h**
> 不显示文件名

# RELATED COMMANDS

**bzegrep**
> 扩展正则表达式（egrep / grep -E）

**bzfgrep**
> 固定字符串（fgrep / grep -F）

# WORKFLOW

```bash
# Search for pattern
bzgrep "error" logfile.bz2

# Case-insensitive
bzgrep -i "warning" logfile.bz2

# Multiple files
bzgrep "pattern" *.bz2

# With context
bzgrep -C 3 "error" logfile.bz2

# Count occurrences
bzgrep -c "error" logfile.bz2

# Override grep with fgrep
GREP=fgrep bzgrep string files
```

# CAVEATS

比搜索未压缩文件慢。必须解压整个文件才能搜索。无法利用 grep 的并行特性。仅限于 bzip2 文件。

# HISTORY

自该工具集于 **1996 年**创建以来，**bzgrep** 就一直是 bzip2 实用工具的一部分。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [egrep](/man/egrep)(1), [fgrep](/man/fgrep)(1), [bzdiff](/man/bzdiff)(1), [bzmore](/man/bzmore)(1), [bzless](/man/bzless)(1), [bzip2](/man/bzip2)(1), [zgrep](/man/zgrep)(1)
