# TAGLINE

比较 bzip2 压缩文件

# TLDR

**比较两个 bzip2 压缩文件**

```bzdiff [file1.bz2] [file2.bz2]```

**将压缩文件与未压缩版本进行比较**

```bzdiff [file.bz2]```

**带 diff 选项进行比较**

```bzdiff -u [file1.bz2] [file2.bz2]```

**改用 cmp 进行比较**

```bzcmp [file1.bz2] [file2.bz2]```

# SYNOPSIS

**bzdiff** [_diff_options_] _file1_ [_file2_]

**bzcmp** [_cmp_options_] _file1_ [_file2_]

# DESCRIPTION

**bzdiff** 通过解压 bzip2 压缩文件并将内容传给 diff 来进行比较。所有选项都会直接传递给底层的 diff 命令。

**bzcmp** 的工作方式类似，但使用 cmp 而不是 diff 进行逐字节比较。

# PARAMETERS

所有参数都直接传递给 **diff** 或 **cmp**：

**-u**
> Unified diff 格式

**-c**
> Context diff 格式

**-i**
> 忽略大小写差异

**-w**
> 忽略空白字符

**-q**
> 只报告文件是否不同

# BEHAVIOR

**单个文件**
> 将 file1 与 file1.bz2（未压缩版本）进行比较

**两个文件**
> 如有需要则先解压再比较

# EXIT STATUS

返回 diff 或 cmp 的退出状态，保留比较结果。

# CAVEATS

错误消息引用的是临时文件名而不是原始文件名。比较期间文件会被解压到临时存储。

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

[diff](/man/diff)(1), [cmp](/man/cmp)(1), [bzgrep](/man/bzgrep)(1), [bzmore](/man/bzmore)(1), [bzip2](/man/bzip2)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
