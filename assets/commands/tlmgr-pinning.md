# TAGLINE

将 TeX Live 软件包固定到指定仓库

# TLDR

**列出已固定的软件包**

```tlmgr pinning show```

**将软件包固定到仓库**

```tlmgr pinning add [repo] [package]```

**解除固定**

```tlmgr pinning remove [repo] [package]```

# SYNOPSIS

**tlmgr pinning** _action_ [_repo_] [_glob_...]

# PARAMETERS

**show**
> 显示当前的固定规则。

**add** _repo_ _glob_
> 将匹配 glob 的软件包固定到仓库。

**remove** _repo_ _glob_
> 解除固定。

# DESCRIPTION

**tlmgr pinning** 管理软件包到特定仓库的固定。确保某些软件包始终来自首选来源。TeX Live Manager 的组成部分，用于多仓库控制。

# SEE ALSO

[tlmgr-repository](/man/tlmgr-repository)(1), [tlmgr](/man/tlmgr)(1)
