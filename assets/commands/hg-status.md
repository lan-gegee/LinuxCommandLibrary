# TAGLINE

显示工作目录中文件的状态

# TLDR

**显示所有已变更的文件**

```hg status```

**仅显示已修改的文件**

```hg status -m```

**仅显示已添加的文件**

```hg status -a```

**显示未跟踪的文件**

```hg status -u```

**显示特定修订版本中的变更**

```hg status --change [rev]```

**显示未变更的文件**

```hg status -c```

# SYNOPSIS

**hg** **status** [_options_] [_file_...]

# PARAMETERS

**-m**, **--modified**
> 仅显示已修改的文件。

**-a**, **--added**
> 仅显示已添加的文件。

**-r**, **--removed**
> 仅显示已移除的文件。

**-d**, **--deleted**
> 仅显示已删除（缺失）的文件。

**-c**, **--clean**
> 仅显示未变更（干净）的文件。

**-u**, **--unknown**
> 仅显示未跟踪的文件。

**--change** _rev_
> 显示指定修订版本中的变更。

# DESCRIPTION

**hg status** 显示工作目录中文件的状态。状态代码：**M**（已修改）、**A**（已添加）、**R**（已移除）、**C**（干净）、**!**（缺失）、**?**（未跟踪）、**I**（已忽略）。使用 **hg diff** 可查看实际的内容变化。

# INSTALL

```apt: sudo apt install mercurial```

```dnf: sudo dnf install mercurial```

```pacman: sudo pacman -S mercurial```

```apk: sudo apk add mercurial```

```zypper: sudo zypper install mercurial```

```brew: brew install mercurial```

```nix: nix profile install nixpkgs#mercurial```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hg](/man/hg)(1), [hg-commit](/man/hg-commit)(1)
