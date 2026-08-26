# TAGLINE

创建 Mercurial 仓库的副本

# TLDR

**克隆仓库**

```hg clone [url]```

**克隆到指定目录**

```hg clone [url] [directory]```

**克隆特定分支**

```hg clone -b [branch] [url]```

**以指定修订版本克隆**

```hg clone -r [revision] [url]```

**不带工作目录克隆**

```hg clone -U [url]```

# SYNOPSIS

**hg clone** [_options_] _source_ [_dest_]

# PARAMETERS

_SOURCE_
> 仓库 URL 或路径。

_DEST_
> 目标目录。

**-b**, **--branch** _BRANCH_
> 克隆特定分支。

**-r**, **--rev** _REV_
> 克隆到指定的修订版本为止。

**-U**, **--noupdate**
> 克隆但不创建工作目录。

**-u**, **--updaterev** _REV_
> 检出指定的修订版本、标签或分支，而不是 tip。

**--pull**
> 使用 pull 协议复制元数据。

**--stream**
> 以最少的数据处理方式克隆（更快，但会跳过 revlog 增量重建）。

**-e**, **--ssh** _CMD_
> 指定要使用的 ssh 命令。

**--insecure**
> 不验证服务器证书。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg clone** 创建 Mercurial 仓库的副本。它会下载完整历史并创建工作目录。

该命令支持多种协议，包括 SSH、HTTP 和本地路径。也可以只克隆特定的分支或修订版本。

# CAVEATS

默认下载完整历史。大型仓库耗时较长。远程仓库需要网络连接。

# HISTORY

clone 是 **Mercurial** 自 1.0 版本以来的核心命令，用于分布式仓库复制。

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

[hg](/man/hg)(1), [hg-pull](/man/hg-pull)(1), [hg-push](/man/hg-push)(1), [hg-init](/man/hg-init)(1)

# RESOURCES

```[Source code](https://foss.heptapod.net/mercurial/mercurial-devel)```

```[Documentation](https://wiki.mercurial-scm.org/)```

<!-- verified: 2026-07-19 -->
