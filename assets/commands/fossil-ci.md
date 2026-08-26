# TAGLINE

fossil commit 的简写

# TLDR

**提交变更**

```fossil ci -m "[message]"```

**使用注释编辑器提交**

```fossil ci```

**提交特定文件**

```fossil ci [file1] [file2] -m "[message]"```

**提交到分支**

```fossil ci --branch [branch_name] -m "[message]"```

# SYNOPSIS

**fossil** **ci** [_options_] [_files_...]

# PARAMETERS

**-m**, **--comment** _text_
> 提交信息。

**--branch** _name_
> 创建新分支。

**--private**
> 使提交保持私有。

**--allow-empty**
> 允许空提交。

# DESCRIPTION

**fossil ci** 是 **fossil commit** 的简写别名。它把工作目录中的变更连同提交信息一起记录到仓库中。

提供此命令是为了方便熟悉其他使用类似缩写的版本控制系统的用户。所有选项和行为与 **fossil commit** 完全相同。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil-commit](/man/fossil-commit)(1), [fossil-add](/man/fossil-add)(1)

# RESOURCES

```[Homepage](https://fossil-scm.org/)```

```[Documentation](https://fossil-scm.org/home/help?cmd=commit)```

<!-- verified: 2026-07-15 -->
