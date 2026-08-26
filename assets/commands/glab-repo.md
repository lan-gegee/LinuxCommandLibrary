# TAGLINE

从命令行管理 GitLab 仓库

# TLDR

**克隆仓库**

```glab repo clone [owner/repo]```

**创建新仓库**

```glab repo create [name]```

**复刻（fork）仓库**

```glab repo fork [owner/repo]```

**查看仓库详情**

```glab repo view [owner/repo]```

**归档仓库**

```glab repo archive [owner/repo]```

**搜索仓库**

```glab repo search [query]```

**列出仓库**

```glab repo list```

**删除仓库**

```glab repo delete [owner/repo]```

# SYNOPSIS

**glab** **repo** _command_ [_options_]

# SUBCOMMANDS

**clone**
> 克隆仓库。

**create**
> 创建新仓库。

**fork**
> 复刻（fork）仓库。

**view**
> 查看仓库详情。

**archive**
> 下载仓库归档。

**search**
> 搜索仓库。

**list**
> 列出仓库。

**delete**
> 删除仓库。

# PARAMETERS

**--public**
> 创建为公开仓库。

**--private**
> 创建为私有仓库。

**--description** _text_
> 仓库描述。

**--clone**
> 复刻后克隆到本地。

**--group** _name_
> 在指定的组/命名空间中创建仓库。

**-y**, **--yes**
> 跳过确认提示。

# DESCRIPTION

**glab repo** 用于从命令行管理 GitLab 仓库。它提供克隆、创建、复刻、搜索和查看仓库等子命令，无需离开终端。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab](/man/glab)(1), [glab-mr](/man/glab-mr)(1), [glab-issue](/man/glab-issue)(1), [git-clone](/man/git-clone)(1)
