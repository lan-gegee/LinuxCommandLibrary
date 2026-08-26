# TAGLINE

利用索引数据库快速查找文件

# TLDR

**按名称查找文件**

```plocate [filename]```

**不区分大小写搜索**

```plocate -i [filename]```

**统计匹配数量**

```plocate -c [pattern]```

**限制结果数量**

```plocate -l [10] [pattern]```

**使用正则模式**

```plocate --regex "[.*\.pdf$]"```

**只显示仍然存在的文件**

```plocate -e [pattern]```

**显示数据库统计信息**

```plocate -S```

**更新数据库**（需要 root）

```sudo updatedb```

# SYNOPSIS

**plocate** [_-icle_] [_--regex_] [_-l limit_] [_pattern_]

# PARAMETERS

**-i**, **--ignore-case**
> 不区分大小写匹配。

**-c**, **--count**
> 打印匹配数量。

**-l** _N_, **--limit** _N_
> 将输出限制为 N 条。

**-e**, **--existing**
> 只显示仍然存在的文件。

**-b**, **--basename**
> 仅匹配文件名（basename），而非完整路径。

**-w**, **--wholename**
> 匹配完整路径（默认）。

**-r**, **--regex**
> 使用 POSIX 扩展正则表达式。

**--regex**
> 将模式视为正则表达式。

**-d** _PATH_, **--database** _PATH_
> 使用指定的数据库文件。

**-0**, **--null**
> 输出以空字符结尾。

**-S**, **--statistics**
> 显示数据库统计信息。

**-q**, **--quiet**
> 安静模式，仅返回退出状态。

**-N**, **--literal**
> 按字面意义匹配模式。

# DESCRIPTION

**plocate** 是比 mlocate 快得多的替代品，它通过搜索预先构建的数据库查找文件，而不是实时扫描文件系统。

数据库由 updatedb 更新（通常通过 cron 定时执行），索引了系统上的所有文件名。无论文件系统大小如何，搜索几乎都是瞬间完成的——即使面对数百万个文件也是如此。

模式匹配默认为子串匹配："foo" 会匹配 "/path/to/foobar.txt"。需要精确匹配请使用 --regex，或用 -b 仅匹配文件名。大小写敏感可用 -i 切换。

-e 选项会在显示前验证文件是否仍然存在，从而过滤掉已删除文件的过期条目。这会带来一些开销，但能确保结果准确。

plocate 使用比 mlocate 更紧凑的数据库格式，并采用倒排表（posting lists）实现快速搜索。同一份 updatedb 数据库可供两种工具共用。

# CONFIGURATION

**/var/lib/plocate/plocate.db**
> 默认的数据库文件，包含索引后的文件系统。

**/etc/updatedb.conf**
> updatedb 的配置文件，控制要索引哪些路径和文件系统。

# CAVEATS

数据库必须定期更新才能反映变化。updatedb 通常每天通过 cron 运行一次。新文件要到下次更新后才会出现。用户只能看到自己有权限访问的文件。首次创建数据库可能较慢。

# HISTORY

**plocate** 由 **Steinar H. Gunderson** 于 **2020 年前后**创建，作为 mlocate 的更快速替代方案。它借鉴了信息检索领域的技术（倒排表、SIMD 加速），实现了 10-100 倍的搜索提速。虽然是一次完全重写，但它保持了对 mlocate 数据库的兼容。

# INSTALL

```apt: sudo apt install plocate```

```dnf: sudo dnf install plocate```

```pacman: sudo pacman -S plocate```

```apk: sudo apk add plocate```

```zypper: sudo zypper install plocate```

```nix: nix profile install nixpkgs#plocate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[locate](/man/locate)(1), [mlocate](/man/mlocate)(1), [updatedb](/man/updatedb)(8), [find](/man/find)(1)
