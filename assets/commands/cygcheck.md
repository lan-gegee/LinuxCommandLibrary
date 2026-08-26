# TAGLINE

Cygwin 诊断与软件包查询工具

# TLDR

**生成完整系统诊断报告**

```cygcheck -s```

**检查可执行文件的依赖**

```cygcheck [program.exe]```

**查找文件所属的软件包**

```cygcheck -f [/usr/bin/bash.exe]```

**列出软件包安装的文件**

```cygcheck -l [coreutils]```

**检查软件包问题**

```cygcheck -c```

**显示 Cygwin 版本信息**

```cygcheck -V```

**详细依赖检查**

```cygcheck -v [program.exe]```

# SYNOPSIS

**cygcheck** [_options_] [_program_|_package_]

# PARAMETERS

**-s**, **--sysinfo**
> 生成全面的系统信息报告。

**-c** [_PACKAGE_], **--check-setup**
> 检查已安装的软件包是否存在问题。

**-f** _FILE_, **--find-package**
> 查找某个文件是由哪个软件包安装的。

**-l** _PACKAGE_, **--list-package**
> 列出软件包安装的文件。

**-p** _PATTERN_, **--package-query**
> 按模式搜索软件包。

**-v**, **--verbose**
> 详细输出（显示完整路径）。

**-r**, **--registry**
> 在报告中包含注册表信息。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**cygcheck** 是 Cygwin（Windows 上的类 Unix 环境）的诊断工具。它提供系统信息、检查可执行文件的依赖，并管理软件包信息。

系统报告（**-s**）对排查 Cygwin 问题极有价值，它会收集已安装软件包、DLL 版本、挂载点、环境变量和 Windows 系统信息的详细信息。寻求支持时通常会被要求提供这份报告。

依赖检查有助于找出导致程序无法运行的缺失 DLL。软件包管理查询则帮助追踪文件归属并验证安装完整性。

# CAVEATS

只能在 Windows 的 Cygwin 环境中使用。系统报告可能很长；提交 bug 报告时请重定向到文件。软件包检查需要 Cygwin 安装时的 setup 数据库。

# HISTORY

cygcheck 是 **Cygwin** 项目的一部分。该项目由 Cygnus Solutions 于 **1995 年**启动，旨在为 Windows 提供 Unix 工具。该工具已成为诊断常见 Cygwin 配置与依赖问题的利器。

# SEE ALSO

[ldd](/man/ldd)(1), [dpkg](/man/dpkg)(1)
