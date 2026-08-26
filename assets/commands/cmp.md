# TAGLINE

逐字节比较文件

# TLDR

**比较两个文件**

```cmp [file1] [file2]```

**静默比较（仅返回退出码）**

```cmp -s [file1] [file2]```

**显示所有差异**

```cmp -l [file1] [file2]```

**打印不同的字节**

```cmp -b [file1] [file2]```

**比较前 N 个字节**

```cmp -n [1024] [file1] [file2]```

**跳过开头的字节**

```cmp -i [100] [file1] [file2]```

# SYNOPSIS

**cmp** [_option_]... _file1_ [_file2_ [_skip1_ [_skip2_]]]

# DESCRIPTION

**cmp** 逐字节比较两个文件并报告第一处差异的位置。默认情况下，它会打印文件开始分歧的字节号和行号；如果两者完全相同，则不产生任何输出。

与基于文本行操作的 **diff** 不同，cmp 工作在字节层面，因此对二进制文件而言更高效、更合适。**-s**（静默）模式常用于只关心退出状态的脚本中：0 表示文件相同，1 表示存在差异，2 表示发生错误。

**-l** 选项列出所有存在差异的字节位置，以及以八进制表示的不同字节值。该工具还可以跳过一个或两个文件开头的一定字节，并将比较限制在指定数量的字节内。

# PARAMETERS

**-b**, **--print-bytes**
> 打印不同的字节

**-i** _skip_, **--ignore-initial** _skip_
> 跳过两个文件开头指定数量的字节

**-i** _skip1:skip2_
> 为每个文件跳过不同数量

**-l**, **--verbose**
> 输出所有字节差异

**-n** _limit_, **--bytes** _limit_
> 最多比较 limit 个字节

**-s**, **--quiet**, **--silent**
> 抑制输出，仅返回退出码

**--help**
> 显示帮助

**-v**, **--version**
> 显示版本

# EXIT STATUS

**0**: 文件完全相同

**1**: 文件存在差异

**2**: 发生错误

# SKIP SUFFIXES

K (1024), M (1048576), G (1073741824)

kB (1000), MB (1000000), GB (1000000000)

# CAVEATS

不能比较目录，只能比较文件。文本文件的差异请改用 diff。从 stdin 读取时，使用 - 作为文件名。

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

[diff](/man/diff)(1), [comm](/man/comm)(1), [md5sum](/man/md5sum)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/diffutils.git)```

```[Documentation](https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html)```

<!-- verified: 2026-06-22 -->
