# TAGLINE

导出 TeX Live 软件包数据库

# TLDR

**导出本地数据库**

```tlmgr dump-tlpdb --local```

**导出远程数据库**

```tlmgr dump-tlpdb --remote```

**以 JSON 输出**

```tlmgr dump-tlpdb --local --json```

# SYNOPSIS

**tlmgr dump-tlpdb** [_options_]

# PARAMETERS

**--local**
> 导出本地安装数据库。

**--remote**
> 导出远程仓库数据库。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**tlmgr dump-tlpdb** 输出 TeX Live 软件包数据库。可用于脚本编写、调试和比较不同安装。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-info](/man/tlmgr-info)(1), [tlmgr](/man/tlmgr)(1)
