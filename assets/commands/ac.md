# TAGLINE

显示用户连接时间统计

# TLDR

以小时为单位输出**当前用户**的连接时长

```ac```

以小时为单位输出**所有用户**的连接时长

```ac -p```

输出**特定用户**的连接时长

```ac -p [username]```

按**天**显示连接时长并给出合计

```ac -d -p [username]```

显示额外的**兼容性**细节

```ac --compatibility```

# SYNOPSIS

**ac** [_-d_] [_-p_] [_-y_] [_-f filename_] [_-a_] [_--compatibility_] [_people_]

# DESCRIPTION

**ac** 根据系统 **wtmp** 文件中记录的登录和登出事件生成以小时为单位的连接时间报告。它通过计算登录与登出时间戳之差来确定每个用户的连接时长。输出可以按单个用户或按天细分，也可以呈现为汇总总计。wtmp 文件由 **login**、**sshd**、**init** 等与登录相关的系统工具自动维护。

# PARAMETERS

**-d, --daily-totals**
> 按每个自然日显示合计，而不是单一的汇总总计

**-p, --individual-totals**
> 分别显示每个用户的连接时长以及总时长

**people**
> 计算指定用户名（以空格分隔的列表）的合计连接时长

**-f, --file filename**
> 从指定文件而非系统 wtmp 读取记账数据

**-a, --all-days**
> 即使某天没有登录活动也包含该日的记录

**-y, --print-year**
> 在日期信息旁显示年份

**-z, --print-zeros**
> 输出等于零的分类合计

**--complain**
> 当 wtmp 文件存在异常时显示错误

**--reboots**
> 包含用户登录到系统重启事件之间累积的时间

**--supplants**
> 在缺少登出记录时，计入从登录到下一次登录的时间

**--timewarps**
> 包含 wtmp 中出现时序不一致时的时间

**--compatibility**
> 同时启用全部三个兼容性标志（reboots、supplants、timewarps）

# CAVEATS

连接时间的计算依赖于准确的 wtmp 记录。系统崩溃或不当关机可能导致数据不完整或不准确。

# HISTORY

属于 **GNU Accounting Utilities**，源自传统 UNIX 记账工具。GNU 版本相比传统实现提供了增强的功能。

# INSTALL

```apt: sudo apt install acct```

```aur: yay -S acct```

```apk: sudo apk add acct```

```zypper: sudo zypper install acct```

```nix: nix profile install nixpkgs#acct```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[last](/man/last)(1), [lastlog](/man/lastlog)(8), [login](/man/login)(1), [sa](/man/sa)(8), [accton](/man/accton)(8), [lastcomm](/man/lastcomm)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/acct/)```

```[Documentation](https://www.gnu.org/software/acct/manual/)```

<!-- verified: 2026-06-10 -->
