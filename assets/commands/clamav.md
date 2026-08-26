# TAGLINE

开源杀毒工具套件

# TLDR

**扫描文件**中的病毒

```clamscan [path/to/file]```

**递归扫描**目录

```clamscan -r [path/to/directory]```

**扫描并删除**受感染的文件

```clamscan -r --remove [path/to/directory]```

**扫描并将**受感染的文件移至隔离区

```clamscan -r --move=[path/to/quarantine] [path/to/directory]```

**以详细输出扫描**并只显示受感染的文件

```clamscan -r -i -v [path/to/directory]```

**更新病毒定义库**（需要 freshclam）

```sudo freshclam```

**使用守护进程扫描**，适合频繁多次扫描

```clamdscan [path/to/file]```

# SYNOPSIS

**clamscan** [_options_] [_file/directory_]

# PARAMETERS

**-r**, **--recursive**
> 递归扫描目录及其子目录。

**-i**, **--infected**
> 输出中只打印受感染的文件。

**--remove**
> 删除受感染的文件。请谨慎使用。

**--move**=_DIR_
> 将受感染的文件移动到指定的隔离目录。

**--copy**=_DIR_
> 将受感染的文件复制到指定目录。

**-v**, **--verbose**
> 扫描时输出详细信息。

**-l** _FILE_, **--log**=_FILE_
> 将扫描报告保存到指定文件。

**--bell**
> 检测到病毒时发出铃声。

**--exclude**=_REGEX_
> 排除匹配正则表达式的文件。

**--include**=_REGEX_
> 只扫描匹配正则表达式的文件。

**--max-filesize**=_SIZE_
> 跳过超过指定大小的文件（默认 100M）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**ClamAV** 是一个用于检测木马、病毒、恶意软件及其他威胁的开源杀毒引擎。该套件包括用于按需扫描的 **clamscan**、作为多线程守护进程的 **clamd**、基于守护进程扫描的 **clamdscan**，以及用于自动更新特征库的 **freshclam**。

ClamAV 广泛应用于邮件网关扫描，尤其是在基于 Unix 的系统上。它支持扫描归档文件（ZIP、RAR、TAR、GZIP）、文档（PDF、Office 格式）、可执行文件及许多其他文件类型。特征数据库由 Cisco Talos 维护，每天更新多次。

对于大批量扫描，运行 **clamd** 守护进程的性能显著优于反复调用 clamscan，因为它将特征数据库常驻内存。

# CONFIGURATION

**/etc/clamav/clamd.conf**
> 守护进程主配置，包括套接字路径、扫描限制和日志选项。

**/etc/clamav/freshclam.conf**
> 病毒数据库更新设置，包括镜像、代理和更新频率。

# CAVEATS

ClamAV 主要设计用于对传入文件进行服务器端扫描，而非桌面实时防护。大型目录的扫描速度可能较慢。**--remove** 选项会在不经确认的情况下永久删除文件。请始终使用 **freshclam** 保持病毒定义库最新，以确保有效检测。

# HISTORY

ClamAV 由 Tomasz Kojm 于 **2001** 年创建，是一个采用 GPL 许可证的 Unix 杀毒工具包。它在邮件服务器扫描领域得到广泛采用。该项目于 **2007** 年被 Sourcefire 收购；在 Sourcefire 于 **2013** 年被思科收购后，项目继续由 Cisco Talos 安全情报团队维护。

# INSTALL

```dnf: sudo dnf install clamav```

```pacman: sudo pacman -S clamav```

```zypper: sudo zypper install clamav```

```brew: brew install clamav```

```nix: nix profile install nixpkgs#clamav```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[freshclam](/man/freshclam)(1), [clamd](/man/clamd)(8), [clamdscan](/man/clamdscan)(1)
