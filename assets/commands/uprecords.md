# TAGLINE

显示历史系统在线时长记录

# TLDR

显示**前 10 条**在线时长记录

```uprecords```

显示**前 N 条**记录

```uprecords -m [25]```

显示重启之间的**停机时间**

```uprecords -d```

按**启动时间**排序（最新的在前）

```uprecords -B```

显示**全部**记录

```uprecords -a```

**循环持续**运行

```uprecords -f```

显示下一个**里程碑**

```uprecords -M```

# SYNOPSIS

**uprecords** [**-?abBcdfkKMsv**] [**-i** _interval_] [**-m** _count_]

# PARAMETERS

**-m** _N_
> 显示前 N 条记录，而非默认的 10 条。

**-a**
> 显示全部记录。

**-b**
> 按启动时间排序，最早的在前。隐含 -s。

**-B**
> 按启动时间排序，最新的在前。隐含 -s。

**-c**
> 若当前条目不在前排条目中则不显示它。

**-d**
> 显示重启之间的停机时间，而不是内核版本。

**-f**
> 循环持续运行（每 5 秒更新一次）。

**-i** _INTERVAL_
> 循环改用 INTERVAL 秒作为间隔，而非 5 秒。隐含 -f。

**-k**
> 按内核/系统名称排序。隐含 -s。

**-K**
> 按内核/系统名称排序并反转顺序。隐含 -s。

**-M**
> 显示下一个里程碑。

**-s**
> 不打印额外的统计信息。

**-w**
> 不截断输出。

**-v**
> 显示版本信息。

# DESCRIPTION

**uprecords** 显示由 uptimed(8) 守护进程收集的历史在线时长记录摘要。它在多次重启之间跟踪系统在线时长，并展示最长运行周期的相关统计。

该工具需要 uptimed 守护进程处于运行状态才能收集在线时长数据。默认情况下，它会显示前 10 条在线时长记录及附加统计信息。

# CAVEATS

需要 uptimed 守护进程处于运行状态。历史数据的多寡取决于 uptimed 已经运行了多久。新安装的系统没有任何历史数据。

# INSTALL

```apt: sudo apt install uptimed```

```dnf: sudo dnf install uptimed```

```pacman: sudo pacman -S uptimed```

```apk: sudo apk add uptimed```

```brew: brew install uptimed```

```nix: nix profile install nixpkgs#uptimed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uptime](/man/uptime)(1), [uptimed](/man/uptimed)(8)
