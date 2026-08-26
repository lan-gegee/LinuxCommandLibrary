# TAGLINE

删除旧的 Nix profile 世代并运行垃圾回收

# TLDR

**清理用户 profile**

```nh clean user```

**清理所有 profile**

```nh clean all```

**按时长限制进行清理**

```nh clean all --keep [30d]```

**试运行**

```nh clean all --dry```

# SYNOPSIS

**nh clean** _target_ [_options_]

# PARAMETERS

**user**
> 清理用户 profile。

**all**
> 清理所有 profile。

**--keep** _period_
> 保留晚于该时段的世代。

**--keep-since** _date_
> 保留该日期之后的世代。

**--dry**
> 试运行。

# DESCRIPTION

**nh clean** 删除旧的 Nix profile 世代并执行垃圾回收，是 nix-collect-garbage 的友好封装。属于 nh（nix helper）工具集。

# SEE ALSO

[nh](/man/nh)(1), [nix-collect-garbage](/man/nix-collect-garbage)(1)
