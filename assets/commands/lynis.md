# TAGLINE

面向 Unix 系统的安全审计工具

# TLDR

检查**更新**

```sudo lynis update info```

运行**完整系统审计**

```sudo lynis audit system```

以**静默方式**运行审计（非交互式）

```sudo lynis audit system --quick```

审计一个 **Dockerfile**

```lynis audit dockerfile [path/to/Dockerfile]```

只运行**特定类别**的测试

```sudo lynis audit system --tests-from-category [networking]```

# SYNOPSIS

**lynis** [_mode_] [_options_]

# DESCRIPTION

**lynis** 是一款面向 Unix 系统的安全审计工具。它执行广泛的健康扫描，涵盖系统加固、漏洞扫描和合规性测试。

# PARAMETERS

**audit system**
> 执行完整的系统安全审计。

**audit dockerfile** _FILE_
> 审计 Dockerfile 中的安全问题。

**update info**
> 检查 lynis 是否有更新。

**show profiles**
> 列出可用的审计 profile。

**show settings**
> 显示当前设置。

**show categories**
> 列出可用的测试类别。

**show commands**
> 显示可用的 lynis 命令。

**-c**, **--cronjob**
> 以 cron 任务方式运行（非交互式，并自动轮转日志文件）

**-Q**, **--quick**
> 快速模式，不等待用户输入。

**-q**, **--quiet**
> 不向屏幕输出。隐含 --quick。

**--no-colors**
> 禁用彩色输出。

**--pentest**
> 非特权扫描，显示渗透测试的关注点。

**--forensics**
> 对正在运行或已挂载的系统进行取证分析。

**--tests** _TEST-IDs_
> 只运行指定的测试。

**--tests-from-category** _CATEGORY_
> 只运行属于指定类别的测试。

**--profile** _FILE_
> 使用替代的审计 profile。

**--logfile** _FILE_
> 指定其他日志文件位置。

**--report-file** _FILE_
> 指定其他报告文件位置。

# CAVEATS

完整审计需要 root 权限。报告保存在 /var/log/lynis-report.dat。部分测试可能仅适用于特定发行版。

# HISTORY

由 CISOfy 开发的开源安全审计工具，其理念源自 rkhunter，但安全覆盖范围更广。

# INSTALL

```dnf: sudo dnf install lynis```

```pacman: sudo pacman -S lynis```

```zypper: sudo zypper install lynis```

```brew: brew install lynis```

```nix: nix profile install nixpkgs#lynis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rkhunter](/man/rkhunter)(8), [chkrootkit](/man/chkrootkit)(8)
