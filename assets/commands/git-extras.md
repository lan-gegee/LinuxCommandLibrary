# TAGLINE

实用的 Git 工具与命令合集

# TLDR

**显示 git-extras 版本**

```git extras --version```

**将 git-extras 更新**到最新版本

```git extras update```

**列出所有 git-extras 命令**

```git extras --help```

**显示仓库摘要**

```git summary```

**根据标签生成变更日志**

```git changelog```

# SYNOPSIS

**git** **extras** [**--version**] [**--help**] [**update**]

# PARAMETERS

**--version**
> 打印已安装的 git-extras 版本。

**--help**
> 打印 git-extras 提供的额外子命令列表。

**update**
> 从上游获取并安装最新的 git-extras 版本。

# DESCRIPTION

**git extras** 是一套全面的 Git 实用命令合集，将 Git 的功能扩展到其核心特性之外。该软件包包含数十个辅助命令，旨在简化常见的 Git 工作流并为重复性任务提供捷径。

其中值得关注的命令包括：用于仓库统计的 git-summary、用于生成变更日志的 git-changelog、用于跟踪开发活动的 git-effort、用于安全清理分支的 git-delete-branch、基于模板创建 .gitignore 的 git-ignore，以及撤销近期改动的 git-undo。

安装方式因平台而异，可通过 Homebrew、apt、yum 安装软件包，也可从源码手动安装。这些工具主要以 shell 脚本实现，因此具有良好的可移植性且易于定制。

# INSTALL

```dnf: sudo dnf install git-extras```

```brew: brew install git-extras```

```nix: nix profile install nixpkgs#git-extras```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-summary](/man/git-summary)(1), [git-changelog](/man/git-changelog)(1), [git-effort](/man/git-effort)(1), [git-ignore](/man/git-ignore)(1), [git-undo](/man/git-undo)(1)
