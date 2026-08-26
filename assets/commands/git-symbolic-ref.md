# TAGLINE

读取和修改 HEAD 之类的符号引用

# TLDR

**查看 HEAD 指向的目标**

```git symbolic-ref HEAD```

**将 HEAD 设置为某分支**

```git symbolic-ref HEAD refs/heads/main```

**获取短名称**

```git symbolic-ref --short HEAD```

**删除符号引用**

```git symbolic-ref -d HEAD```

# SYNOPSIS

**git symbolic-ref** [_options_] _name_ [_ref_]

# PARAMETERS

_NAME_
> 符号引用名（通常是 HEAD）。

_REF_
> 要设置的目标引用。

**--short**
> 显示短名称。

**-d**, **--delete**
> 删除符号引用。

**-q**, **--quiet**
> 安静模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git symbolic-ref** 用于读取和修改符号引用。HEAD 是最常见的符号引用，指向当前检出的分支。这个底层（plumbing）命令可以显示 HEAD 指向哪个分支，或以编程方式改变它。

当 HEAD 处于分离状态（直接指向某个提交而非分支）时，该命令会报错，这也是它与 `git rev-parse` 的区别之一。

# CAVEATS

底层（plumbing）命令。最常用于 HEAD。分离状态的 HEAD 不是符号引用。

# HISTORY

git symbolic-ref 是管理符号引用的核心 **Git** 底层（plumbing）命令，是分支跟踪机制的基础。

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

[git-checkout](/man/git-checkout)(1), [git-rev-parse](/man/git-rev-parse)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-symbolic-ref)```

<!-- verified: 2026-07-17 -->
