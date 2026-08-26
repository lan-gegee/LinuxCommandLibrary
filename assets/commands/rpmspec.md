# TAGLINE

查询和解析 RPM spec 文件

# TLDR

列出 spec 文件中的**二进制软件包**

```rpmspec --query [path/to/rpm.spec]```

列出所有**查询格式标签**

```rpmspec --querytags```

获取软件包的**概要信息**

```rpmspec --query --queryformat "%{name}: %{summary}\n" [path/to/rpm.spec]```

获取**源码软件包**的信息

```rpmspec --query --srpm [path/to/rpm.spec]```

**解析**并展开 spec 文件，输出到 stdout

```rpmspec --parse [path/to/rpm.spec]```

列出 spec 文件中的**构建依赖**

```rpmspec --query --buildrequires [path/to/rpm.spec]```

带**宏定义**进行查询

```rpmspec --define "[dist .el9]" --query [path/to/rpm.spec]```

# SYNOPSIS

**rpmspec** {**--query** | **--parse**} [_options_] _specfile_

# PARAMETERS

**--query**, **-q**
> 查询 spec 文件中的软件包信息。

**--querytags**
> 列出可用的查询格式标签。

**--queryformat** _format_
> 使用 rpm 头部标签（如 %{name}、%{version}）自定义输出格式。

**--srpm**
> 查询源码软件包而非二进制软件包的信息。

**--buildrequires**
> 列出 spec 文件中的构建依赖。

**--parse**
> 解析并展开 spec 文件的宏，把处理后的 spec 输出到 stdout。

**--define** _"macro value"_
> 为 spec 文件处理定义一个宏。

**--target** _platform_
> 设置查询的目标平台。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**rpmspec** 查询 RPM spec 文件以提取软件包信息，无需真正构建软件包。它可以列出将会生成的软件包、显示软件包元数据、展开宏以及解析 spec 文件内容。

这对于校验 spec 文件、提取构建依赖以及在软件包开发过程中调试宏展开非常有用。

# CAVEATS

某些 spec 文件特性可能需要额外的宏或定义才能被正确解析。条件块（%if/%endif）在解析时求值，结果可能因所定义的宏不同而不同。需要使用 --define 标志来模拟目标发行版的设置。

# HISTORY

属于 **RPM** 包管理器工具链。提供独立于完整构建流程之外的 spec 文件内省功能。

# INSTALL

```apt: sudo apt install rpm```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [rpmbuild](/man/rpmbuild)(8), [dnf](/man/dnf)(8)
