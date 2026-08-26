# TAGLINE

将补丁应用到文件和索引

# TLDR

**应用一个补丁**

```git apply [patch.diff]```

**检查补丁是否可应用**

```git apply --check [patch.diff]```

**应用并显示统计信息**

```git apply --stat [patch.diff]```

**反向应用补丁**

```git apply --reverse [patch.diff]```

仅**应用到索引**

```git apply --cached [patch.diff]```

**应用并把被拒绝的 hunk** 保存到 .rej 文件

```git apply --reject [patch.diff]```

**应用到子目录**

```git apply --directory=[modules/subdir] [patch.diff]```

# SYNOPSIS

**git apply** [_options_] _patches_

# PARAMETERS

_PATCHES_
> 要应用的补丁文件。

**--check**
> 检查补丁是否能干净地应用。

**--stat**
> 显示 diffstat 而不实际应用。

**--reverse**, **-R**
> 反向应用补丁。

**--cached**
> 仅应用到索引。

**--3way**, **-3**
> 当补丁无法干净应用时尝试三方合并。隐含 --index。

**--reject**
> 应用可以应用的 hunk，把被拒绝的留在 .rej 文件中，而不是让整个补丁失败。

**--numstat**
> 以机器可读格式显示新增/删除行数，而不实际应用。

**--directory** _DIR_
> 在所有文件名前添加根目录前缀。

**--exclude** _PATTERN_
> 跳过匹配给定路径模式的文件。

**--include** _PATTERN_
> 只应用于匹配给定路径模式的文件。

**--whitespace** _ACTION_
> 处理空白错误（nowarn、warn、fix、error、error-all）。

**-v**, **--verbose**
> 报告进度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git apply** 将补丁应用到文件和/或索引。与 git am 不同，它处理的是原始 diff 输出而不带电子邮件格式，因此适合 git diff 生成的补丁。

该命令可以将补丁应用到工作树、索引或两者。它支持在不应用的情况下检查补丁（--check）和显示统计信息（--stat）。反向应用（--reverse）可用于撤销补丁。

与 **git am** 不同，此命令不创建提交，因此适合将补丁作为工作目录修改来应用，以便在提交前进行评审。

# CAVEATS

不创建提交。处理补丁系列请使用 git am。未做相应处理时对二进制文件可能失败。

# HISTORY

git apply 是 **Git** 用于应用补丁的核心命令，提供的功能层级比 git am 更低。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-am](/man/git-am)(1), [git-diff](/man/git-diff)(1), [patch](/man/patch)(1)
