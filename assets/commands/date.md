# TAGLINE

显示或设置系统日期和时间

# TLDR

**显示**当前日期和时间

```date```

**自定义**格式

```date ["+%Y-%m-%d %H:%M:%S"]```

以 UTC **显示**日期

```date -u```

**设置**日期（需要 root）

```sudo date -s ["2024-01-15 10:30:00"]```

从时间戳**显示**日期

```date -d [@1234567890]```

# SYNOPSIS

**date** [_options_] [_+format_]

# DESCRIPTION

**date** 显示或设置系统日期和时间。它通过格式说明符支持丰富的输出格式，还支持时区转换、相对日期计算和 Unix 时间戳转换。该命令是打时间戳、记录日志、调度以及基于时间的操作中不可或缺的工具。

除了简单显示，date 还擅长日期运算：可以指定"tomorrow"、"next monday"、"2 days ago"或"+3 hours"等相对日期。它能解析字符串形式的日期、把 Unix 时间戳转换为人类可读的格式，并按 ISO 8601 标准或自定义格式输出。

该工具是最常用的 Unix 工具之一，自最早的 Unix 版本就已存在。在 shell 脚本中，它常用于生成带时间戳的文件名、计算时间差或实现基于日期的条件逻辑。

格式说明符可以精确控制输出，从简单的 "YYYY-MM-DD" 到复杂的本地化格式皆可。该工具遵循时区设置，可以显示 UTC 或任意指定时区的时间。

# PARAMETERS

**-d**, **--date=**_string_
> 显示指定的日期/时间

**-s**, **--set=**_string_
> 设置系统日期/时间（需要 root）

**-u**, **--utc**
> 输出/设置 UTC 时间

**-r**, **--reference=**_file_
> 显示文件的修改时间

**-I**[_timespec_]
> ISO 8601 格式

**-R**, **--rfc-email**
> RFC 5322 格式

# FORMAT SPECIFIERS

**日期：**
- **%Y** - 年份（2024）
- **%y** - 年份（24）
- **%m** - 月份（01-12）
- **%d** - 日（01-31）
- **%B** - 月份名（January）
- **%b** - 短月份名（Jan）
- **%A** - 星期名（Monday）
- **%a** - 短星期名（Mon）

**时间：**
- **%H** - 24 小时制小时（00-23）
- **%I** - 12 小时制小时（01-12）
- **%M** - 分钟（00-59）
- **%S** - 秒（00-59）
- **%p** - AM/PM
- **%Z** - 时区名称

**组合：**
- **%s** - Unix 纪元秒数
- **%F** - 完整日期（YYYY-MM-DD）
- **%T** - 完整时间（HH:MM:SS）
- **%c** - 本地化的日期和时间

# WORKFLOW

```bash
# Current date/time
date

# ISO 8601 format
date -I
date "+%Y-%m-%d"

# Custom format
date "+%Y-%m-%d %H:%M:%S"

# Unix timestamp
date +%s

# From timestamp
date -d @1234567890

# Relative dates
date -d "tomorrow"
date -d "next monday"
date -d "2 days ago"
date -d "+3 hours"

# UTC time
date -u

# File modification time
date -r file.txt

# RFC format
date -R
```

# RELATIVE DATES

```bash
date -d "1 day ago"
date -d "2 weeks ago"
date -d "next friday"
date -d "last month"
date -d "3 years ago"
date -d "+5 days"
```

# COMMON USES

**带时间戳的文件名：**
```bash
backup-$(date +%Y%m%d).tar.gz
log-$(date +%Y-%m-%d_%H-%M-%S).txt
```

**日志记录：**
```bash
echo "$(date): Starting backup" >> log.txt
```

**条件判断：**
```bash
if [ $(date +%u) -eq 1 ]; then
    echo "It's Monday"
fi
```

# CAVEATS

设置日期需要 root 权限。系统时钟与硬件时钟不同。时区会影响输出。闰秒不一定被处理。BSD 与 GNU 实现行为有差异。相对日期的解析可能有歧义。

# HISTORY

**date** 自 **1971 年** Unix Version 1 起就是 Unix 的一部分，是最早的一批 Unix 命令之一。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [hwclock](/man/hwclock)(8), [cal](/man/cal)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html)```

<!-- verified: 2026-07-11 -->
