# TAGLINE

命令行病毒扫描器

# TLDR

**扫描单个文件**

```clamscan [file]```

**递归扫描目录**

```clamscan -r [/path/to/dir]```

**只显示受感染的文件**

```clamscan -ri [/path/to/dir]```

**移动受感染的文件**

```clamscan -r --move=[/quarantine] [/path/to/scan]```

**删除受感染的文件**

```clamscan -r --remove [/path/to/scan]```

**扫描并记录结果**

```clamscan -r -l [scan.log] [/path/to/dir]```

**排除目录**

```clamscan -r --exclude-dir=[backup] [/home]```

# SYNOPSIS

**clamscan** [_options_] [_file_|_directory_...]

# DESCRIPTION

**clamscan** 是来自 ClamAV 杀毒套件的独立命令行病毒扫描器。它使用 ClamAV 特征数据库扫描文件和目录中的病毒、木马、恶意软件及其他威胁。

每次调用都会将完整的病毒数据库加载到内存，因此适合一次性扫描，但反复使用时速度较慢。对于大批量或频繁的扫描，首选基于守护进程的 **clamdscan**，因为它避免了重复加载数据库的开销。

clamscan 支持递归目录扫描、基于模式的文件包含与排除、可配置的大小限制，以及针对受感染文件的多种处理方式，包括删除、隔离（移动）和复制。扫描结果可以记录到文件中以备审计。

# PARAMETERS

**-r**, **--recursive**
> 递归扫描目录

**-i**, **--infected**
> 只打印受感染的文件

**-o**, **--suppress-ok-results**
> 不打印干净的文件

**--remove**[=yes/no]
> 删除受感染的文件（危险；默认禁用）

**--move**=_dir_
> 将受感染的文件移动到指定目录

**--copy**=_dir_
> 将受感染的文件复制到指定目录

**-l** _file_, **--log**=_file_
> 将扫描报告写入文件

**-d** _path_, **--database**=_path_
> 从文件或目录加载病毒特征

**--exclude**=_REGEX_
> 跳过匹配正则表达式的文件

**--exclude-dir**=_REGEX_
> 跳过匹配正则表达式的目录

**--include**=_REGEX_
> 只扫描匹配正则表达式的文件

**--include-dir**=_REGEX_
> 只进入匹配正则表达式的目录

**--max-filesize**=_size_
> 跳过超过指定大小的文件

**--max-scansize**=_size_
> 每个容器最多扫描的数据量

**--bell**
> 检测到威胁时发出提示音

**--detect-pua**[=yes/no]
> 检测可能不需要的应用程序

**--quiet**
> 只打印错误消息

**--no-summary**
> 抑制最终的扫描摘要

**-v**, **--verbose**
> 详细输出

**--version**
> 打印版本信息

# DATABASE UPDATE

扫描前先更新特征库：

```sudo freshclam```

# CAVEATS

由于存在误报，--remove 很危险。请改用 --move 或 --copy。默认单线程。需要多线程扫描时，请配合 clamd 守护进程使用 clamdscan。

# INSTALL

```apt: sudo apt install clamav```

```dnf: sudo dnf install clamav```

```pacman: sudo pacman -S clamav```

```apk: sudo apk add clamav-scanner```

```zypper: sudo zypper install clamav```

```brew: brew install clamav```

```nix: nix profile install nixpkgs#clamav```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[freshclam](/man/freshclam)(1), [clamdscan](/man/clamdscan)(1), [clamd](/man/clamd)(8)
