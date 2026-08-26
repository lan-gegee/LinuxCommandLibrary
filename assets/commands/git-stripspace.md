# TAGLINE

清理 Git 消息中的空白字符

# TLDR

**去除行尾空白**

```git stripspace < [file]```

**去除注释行**

```git stripspace -s < [file]```

**将行注释掉**

```git stripspace -c < [file]```

# SYNOPSIS

**git** **stripspace** [_options_]

# PARAMETERS

**-s**, **--strip-comments**
> 去除注释行。

**-c**, **--comment-lines**
> 将行注释掉。

# DESCRIPTION

**git stripspace** 对来自 stdin 的文本进行过滤，去掉行尾空白并将多个连续空行合并为一个。Git 内部就用它来清理提交信息。

该命令还可以去除或添加注释行，因此也适合处理 Git 格式的消息和模板。

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

[git-commit](/man/git-commit)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-stripspace)```

<!-- verified: 2026-07-17 -->
