# TAGLINE

从柏林工业大学的 ISIS/Moodle 平台下载课程资料

# TLDR

**下载所有课程**

```isisdl```

**下载指定课程**

```isisdl -c [course_id]```

**列出可用课程**

```isisdl -l```

**以同步方式下载**

```isisdl -s```

**设置下载目录**

```isisdl -d [/path/to/dir]```

# SYNOPSIS

**isisdl** [_options_]

# PARAMETERS

**-c** _ID_
> 指定课程 ID。

**-l**, **--list**
> 列出可用课程。

**-d** _PATH_
> 下载目录。

**-s**, **--sync**
> 同步模式（跳过已存在的文件）。

**--config**
> 显示配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**isisdl** 用于从柏林工业大学（TU Berlin）的 ISIS/Moodle 平台下载课程资料。它会完成身份验证并批量下载文件。

该工具按课程结构组织下载内容。它支持同步模式以避免重复下载已有文件。

# CAVEATS

仅适用于柏林工业大学。需要 ISIS 账号。遵守速率限制。

# HISTORY

isisdl 的创建目的是帮助**柏林工业大学**的学生从 ISIS 学习管理系统中下载课程资料。

# INSTALL

```nix: nix profile install nixpkgs#isisdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [youtube-dl](/man/youtube-dl)(1)
