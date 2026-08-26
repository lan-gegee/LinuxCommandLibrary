# TAGLINE

扫描系统中的 rootkit 和漏洞

# TLDR

**检查**系统中的 rootkit

```sudo rkhunter --check```

**非交互式检查**（无需按键确认）

```sudo rkhunter --check --sk```

**更新**数据库

```sudo rkhunter --update```

在合法变更后**更新**文件属性数据库

```sudo rkhunter --propupd```

**列出**所有测试项

```sudo rkhunter --list tests```

检查**版本**

```sudo rkhunter --versioncheck```

从 **cron** 运行且只报告警告

```sudo rkhunter --cronjob --report-warnings-only```

# SYNOPSIS

**rkhunter** [**--check**] [**--update**] [**--propupd**] [**--list**] [_options_]

# PARAMETERS

**-c**, **--check**
> 执行系统检查，查找 rootkit、后门和漏洞利用。

**--update**
> 更新数据文件和恶意软件签名。

**--propupd**
> 用当前值更新文件属性数据库（在合法的系统变更之后运行）。

**--list** [_tests|rootkits|lang|perl|propfiles_]
> 列出支持的功能。

**--versioncheck**
> 检查是否有更新版本的 rkhunter。

**-C**, **--config-check**
> 校验配置文件。

**--sk**, **--skip-keypress**
> 在测试组之间不等待按键确认。

**--rwo**, **--report-warnings-only**
> 只显示警告。

**--cronjob**
> 针对 cron 执行优化输出（无颜色、无需按键）。

**--configfile** _file_
> 使用其他配置文件。

**-l**, **--logfile** _file_
> 将日志输出写入指定文件。

**--appendlog**
> 追加到已有的日志文件而不是覆盖。

**--disable** _tests_
> 禁用特定测试（逗号分隔列表）。

**--enable** _tests_
> 只启用指定的测试。

**--pkgmgr** _type_
> 使用软件包管理器校验（RPM、DPKG、BSD、SOLARIS、NONE）。

**-q**, **--quiet**
> 抑制所有输出。

**--nocolors**
> 禁用彩色输出。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**rkhunter**（Rootkit Hunter）扫描 Linux 系统中的 rootkit、后门和本地漏洞利用。它会检查隐藏文件、可疑的内核模块、被修改的二进制文件以及其他入侵迹象。

该工具维护着一个包含已知恶意软件签名和文件校验和的数据库，并将当前系统状态与已知良好的基准值进行比较。

# CONFIGURATION

**/etc/rkhunter.conf**
> 主配置文件，控制扫描行为、白名单文件、更新镜像源和通知设置。

**/var/lib/rkhunter/db/**
> 数据库目录，包含恶意软件签名、文件属性哈希以及扫描时用于比对的已知良好校验和。

**/var/log/rkhunter.log**
> 默认日志文件，记录扫描结果和警告。

# CAVEATS

需要定期更新才能保持有效性。在定制化的系统上可能产生误报。合法的系统变更后请运行 --propupd。建议在每次检查后查看日志。

# HISTORY

**rkhunter** 由 **Michael Boelen** 创建，用于帮助系统管理员检测 rootkit 和潜在安全问题。自 2003 年以来一直活跃维护。

# INSTALL

```dnf: sudo dnf install rkhunter```

```pacman: sudo pacman -S rkhunter```

```brew: brew install rkhunter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chkrootkit](/man/chkrootkit)(1), [aide](/man/aide)(1), [tripwire](/man/tripwire)(8)
