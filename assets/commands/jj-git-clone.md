# TAGLINE

将 Git 仓库克隆到 Jujutsu 工作区

# TLDR

克隆仓库

```jj git clone [url]```

克隆到指定目录

```jj git clone [url] [directory]```

以 Git 共存模式克隆

```jj git clone --colocate [url]```

# SYNOPSIS

**jj git clone** [_options_] _url_ [_directory_]

# PARAMETERS

_URL_
> Git 仓库 URL。

_DIRECTORY_
> 目标目录。

**--colocate**
> 创建 jj/Git 共存（colocated）仓库。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj git clone** 将 Git 仓库克隆到 Jujutsu 工作区。它会抓取所有分支并创建 jj 的内部结构。

colocate 选项将 Git 与 jj 数据保存在一起。这样可以在同一个仓库上同时使用两种工具。

# CAVEATS

jj 的子命令。创建的是 jj 工作区。需要同时使用 Git 和 jj 时选择 colocate。

# HISTORY

jj git clone 是 **Jujutsu** 的一部分，可从任何 Git 托管服务无缝克隆。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git](/man/jj-git)(1), [git-clone](/man/git-clone)(1)
