# TAGLINE

汇总各类服务日志的日志分析与报告工具

# TLDR

按**日期范围**和详细程度分析日志

```logwatch --range [yesterday|today|all] --detail [low|medium|high]```

针对**特定服务**生成报告

```logwatch --range all --service [apache|sshd|pam_unix]```

# SYNOPSIS

**logwatch** [_options_]

# DESCRIPTION

**logwatch** 是一款日志分析与报告工具，将来自各种服务的日志汇总成一份报告。它解析 Apache、SSH、PAM 以及许多其他服务的日志，突出重要事件。

# PARAMETERS

**--range RANGE**
> 日期范围：yesterday、today、all 或具体日期

**--detail LEVEL**
> 详细程度：low、medium、high 或 0-10

**--service SERVICE**
> 仅分析特定服务

**--output FORMAT**
> 输出方式：stdout、file、mail

**--mailto ADDRESS**
> 将报告发送到指定邮箱

**--filename FILE**
> 输出到指定文件

# CAVEATS

需要各服务专用的过滤脚本。高详细级别下输出量可能很大。

# INSTALL

```dnf: sudo dnf install logwatch```

```pacman: sudo pacman -S logwatch```

```apk: sudo apk add logwatch```

```zypper: sudo zypper install logwatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [logrotate](/man/logrotate)(8)
