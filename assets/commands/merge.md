# TAGLINE

执行三方文件合并

# TLDR

**三方合并**

```merge [file] [base] [other]```

**输出到其他文件**

```merge -p [file] [base] [other] > [merged]```

**安静模式**

```merge -q [file] [base] [other]```

使用 diff3 风格**显示冲突标记**

```merge -A [file] [base] [other]```

为冲突标记**使用自定义标签**

```merge -L [mine] -L [base] -L [theirs] [file] [base] [other]```

# SYNOPSIS

**merge** [_options_] _file1_ _file2_ _file3_

# PARAMETERS

_FILE1_
> 接收变更的文件。

_FILE2_
> 共同祖先文件。

_FILE3_
> 含有变更的文件。

**-p**
> 打印到标准输出。

**-q**
> 安静模式。

**-A**
> 以 diff3 -A 风格输出冲突（最详细）。

**-E**
> 以 diff3 -E 风格输出冲突（默认）。

**-e**
> 类似 -E，但不就冲突发出警告。

**-L** _LABEL_
> 在冲突标记中使用标签代替文件名。最多可指定三次。

**-V**
> 打印 RCS 版本号。

# DESCRIPTION

**merge** 执行三方文件合并，将 _file3_ 相对于 _file2_ 的变更合入 _file1_。共同祖先 _file2_ 用于判定每个版本各自做了哪些修改。

该工具是 RCS（版本控制系统）套件的一部分。发生冲突时，merge 会将冲突标记写入 _file1_ 供手动解决。退出状态码：0 表示无冲突，1 表示发现冲突，2 表示出错。

# CAVEATS

属于 RCS 套件。冲突需要手动解决。退出码指示是否存在冲突。

# HISTORY

merge 是 **RCS**（版本控制系统）的一部分，提供三方文件合并能力。

# INSTALL

```apt: sudo apt install rcs```

```dnf: sudo dnf install rcs```

```pacman: sudo pacman -S rcs```

```apk: sudo apk add rcs```

```zypper: sudo zypper install rcs```

```brew: brew install rcs```

```nix: nix profile install nixpkgs#rcs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff3](/man/diff3)(1), [diff](/man/diff)(1), [patch](/man/patch)(1), [rcs](/man/rcs)(1), [sdiff](/man/sdiff)(1), [git-merge](/man/git-merge)(1)
