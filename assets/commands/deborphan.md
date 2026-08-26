# TAGLINE

在基于 Debian 的系统上查找孤儿软件包

# TLDR

显示**孤儿库**软件包

```deborphan```

列出**所有**分区中的孤儿软件包

```deborphan --all-packages```

用所有启发式规则列出包括**类库名称**在内的孤儿

```deborphan --guess-all```

查找仅被**推荐或建议**（非硬依赖）的软件包

```deborphan -n```

通过 apt **自动移除孤儿**

```deborphan | xargs apt-get -y remove --purge```

显示孤儿软件包及其**分区**和**大小**

```deborphan -sz```

# SYNOPSIS

**deborphan** [_options_] [_package_...]

# DESCRIPTION

**deborphan** 在基于 Debian 的系统上查找孤儿软件包。孤儿软件包通常是那些作为依赖安装、但已不再被任何已安装软件包需要的库。

默认只检查 "libs" 和 "oldlibs" 分区中的软件包。使用 **-a** 可检查所有分区。

# PARAMETERS

**-a**, **--all-packages**
> 检查所有软件包，而不仅是 libs/oldlibs 分区

**--guess-all**
> 启用所有启发式规则，在其他分区中查找名称类似库的软件包

**-n**, **--nice-mode**
> 显示仅被推荐或建议（而非硬依赖）的软件包

**-H**, **--show-section**
> 显示每个软件包的分区

**-s** _section_
> 仅检查指定的分区（可多次使用）

**-z**, **--show-size**
> 显示每个软件包的已安装大小

**-d**, **--show-deps**
> 显示依赖该孤儿的软件包

**-P**, **--show-priority**
> 显示每个软件包的优先级

**--no-show-section**
> 不显示分区（默认）

**-p** _file_, **--status-file** _file_
> 使用替代的状态文件而非 /var/lib/dpkg/status

# CAVEATS

默认只显示库；完整扫描请使用 **-a**。移除前应审查结果，因为某些软件包可能是手动安装且仍然需要的。如需自动清理未使用的依赖，**apt autoremove** 是更简单的选择。

# SEE ALSO

[apt](/man/apt)(8), [aptitude](/man/aptitude)(8), [dpkg](/man/dpkg)(1)
