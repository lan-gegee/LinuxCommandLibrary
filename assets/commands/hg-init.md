# TAGLINE

在指定目录或当前目录创建新的 Mercurial 仓库

# TLDR

**在当前目录创建仓库**

```hg init```

**在新目录中创建仓库**

```hg init [project-name]```

# SYNOPSIS

**hg** **init** [_options_] [_dest_]

# PARAMETERS

_DEST_
> 创建仓库的目录；不存在时会自动创建。默认为当前目录。

**-e**, **--ssh** _CMD_
> 指定要使用的 ssh 命令（针对远程目标）。

**--remotecmd** _CMD_
> 指定在远端运行的 hg 命令。

**--insecure**
> 不验证服务器证书。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg init** 在指定目录中创建新的 Mercurial 仓库，未指定目录时使用当前目录。它会创建一个包含全部版本控制数据的 **.hg** 子目录。初始化后，使用 **hg add** 跟踪文件，用 **hg commit** 保存变更集。工作目录存放源文件，而 **.hg** 保存仓库历史。

# CAVEATS

如果目标位置已是一个非空且非仓库的目录，则会失败。在现有仓库内执行初始化会创建嵌套仓库，这通常不是想要的结果。

# HISTORY

init 是 **Mercurial** 的核心命令，自该项目 2005 年首次发布以来一直存在。

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

[hg](/man/hg)(1), [hg-add](/man/hg-add)(1), [hg-commit](/man/hg-commit)(1), [hg-clone](/man/hg-clone)(1)

# RESOURCES

```[Source code](https://foss.heptapod.net/mercurial/mercurial-devel)```

```[Documentation](https://wiki.mercurial-scm.org/)```

<!-- verified: 2026-07-19 -->
