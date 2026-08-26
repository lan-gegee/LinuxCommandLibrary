# TAGLINE

启用或禁用进程记账

# TLDR

**启用进程记账**并写入指定文件

```sudo accton [/var/log/account/pacct]```

**禁用进程记账**

```sudo accton off```

**查看当前记账状态**

```sudo accton```

# SYNOPSIS

**accton** [**off**] [_file_]

# PARAMETERS

**off**
> 禁用进程记账。

_file_
> 记账文件的路径，记录将写入该文件。通常为 **/var/log/account/pacct** 或 **/var/account/acct**。

# DESCRIPTION

**accton** 用于启用或禁用系统进程记账。这是一项内核功能，会记录系统中每个终止进程的信息。启用后，内核会为每个结束的进程写入一条紧凑的记录，包括命令名、占用的 CPU 时间、内存消耗和退出状态。

不带参数时，accton 显示当前记账状态。指定文件路径则启用记账并将记录写入该文件。参数 **off** 用于禁用记账。

记账数据可使用配套工具分析，例如 **sa**（汇总记账信息）和 **lastcomm**（显示最近执行的命令）。这些信息对系统审计、资源使用分析和故障排查很有价值。

# CAVEATS

进程记账文件会持续增长，必须定期轮转或截断，以防止磁盘空间耗尽。该功能会给进程终止带来轻微开销。启用或禁用需要 root 权限。记账文件格式与体系结构相关，可能无法在不同系统间移植。

# HISTORY

进程记账起源于 **20 世纪 70 年代** Bell Labs 的早期 Unix 系统，最初为多用户分时环境中的资源用量跟踪而设计。在商业 Unix 部署中，该功能曾被用于计费。**accton** 命令及相关工具自此一直是 Unix 和 Linux 系统的标准组件，如今主要用于安全审计而非计费。

# INSTALL

```apt: sudo apt install acct```

```aur: yay -S acct```

```apk: sudo apk add acct```

```zypper: sudo zypper install acct```

```nix: nix profile install nixpkgs#acct```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[sa](/man/sa)(8), [lastcomm](/man/lastcomm)(1), [ac](/man/ac)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/acct/)```

```[Documentation](https://www.gnu.org/software/acct/manual/)```

<!-- verified: 2026-06-10 -->
