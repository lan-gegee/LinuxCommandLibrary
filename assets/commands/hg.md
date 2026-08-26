# TAGLINE

分布式版本控制系统

# TLDR

**初始化仓库**

```hg init```

**克隆仓库**

```hg clone [url]```

**显示状态**

```hg status```

**添加文件**

```hg add [files]```

**提交更改**

```hg commit -m "[message]"```

**查看日志**

```hg log```

**拉取更改**

```hg pull```

**推送更改**

```hg push```

# SYNOPSIS

**hg** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Mercurial 命令。

**init**
> 创建仓库。

**clone**
> 克隆仓库。

**status**
> 显示工作目录状态。

**add**
> 添加文件。

**commit**
> 提交更改。

**log**
> 显示历史。

**pull**
> 从远程拉取。

**push**
> 推送到远程。

**-R**, **--repository** _REPO_
> 以给定仓库为起点运行。

**-v**, **--verbose**
> 增加输出量。

**-q**, **--quiet**
> 抑制输出。

**--version**
> 输出版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Mercurial**（hg）是一个分布式版本控制系统。它跟踪源代码的变更，支持分支、合并和协作。

Mercurial 与 Git 类似，但命令语法和设计理念不同。它强调界面的简洁与一致性。

# CONFIGURATION

Mercurial 会按顺序读取多个 **hgrc** 配置文件：系统级文件（例如 **/etc/mercurial/hgrc**）、用户级文件（**~/.hgrc**）和仓库级文件（**.hg/hgrc**）。后面的文件会覆盖前面的配置。常见配置节包括用于设置用户名和编辑器的 **[ui]**、用于设置远程别名的 **[paths]**，以及用于启用内置或第三方扩展的 **[extensions]**。

# CAVEATS

不如 Git 流行。工作流有所差异。通过扩展系统提供更多功能。

# HISTORY

Mercurial 由 **Matt Mackall** 于 **2005 年**创建，仅晚于 Git，是针对 Linux 内核开发的另一种解决方案。

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

[git](/man/git)(1), [svn](/man/svn)(1), [hg-clone](/man/hg-clone)(1), [hg-commit](/man/hg-commit)(1), [hg-init](/man/hg-init)(1)

# RESOURCES

```[Source code](https://foss.heptapod.net/mercurial/mercurial-devel)```

```[Homepage](https://www.mercurial-scm.org/)```

```[Documentation](https://wiki.mercurial-scm.org/)```

<!-- verified: 2026-07-19 -->
