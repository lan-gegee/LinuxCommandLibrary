# TAGLINE

在已安装的 Java 版本之间切换

# TLDR

**列出所有已安装的 Java 版本**

```update-java-alternatives --list```

**切换到特定的 Java 版本**

```sudo update-java-alternatives --set [java-17-openjdk-amd64]```

**将所有 Java 候选项设为自动模式**

```sudo update-java-alternatives --auto```

**仅切换 JRE**（运行时，不含开发工具包）

```sudo update-java-alternatives --jre --set [java-17-openjdk-amd64]```

**预演将要执行的操作**而不实际更改

```update-java-alternatives --test --set [java-17-openjdk-amd64]```

# SYNOPSIS

**update-java-alternatives** [**-l**|**--list**] [**-s**|**--set** _jname_] [**-a**|**--auto**] [**--jre**] [**--jre-headless**] [**--plugin**]

# PARAMETERS

**-l**, **--list** [_jname_]
> 列出所有已安装的 Java 软件包，或某个特定安装的详细信息。

**-s**, **--set** _jname_
> 将所有候选项设置为指定的 Java 安装。

**-a**, **--auto**
> 将所有候选项切换到自动模式，由系统选择优先级最高的版本。

**--jre**
> 将操作范围限制为运行时环境候选项，不含开发工具包工具。

**--jre-headless**
> 将操作范围限制为 headless 运行时候选项（无 GUI 支持）。

**--plugin**
> 将操作范围限制为浏览器插件候选项。

**-t**, **--test**
> 试运行模式。显示将要执行的操作但不实际更改。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**update-java-alternatives** 管理 Debian 和 Ubuntu 系统上的多个 Java 安装。它是专为 Java 打造的 update-alternatives 封装，能同时更新所有与 Java 相关的二进制文件（java、javac、jar、javadoc 等）。

切换 Java 版本时，该工具确保所有关联命令都指向同一安装，避免 JRE 与 JDK 工具之间出现版本不一致。对于需要特定 Java 版本的开发环境来说，这一点至关重要。

jname 参数对应 /usr/lib/jvm/ 下该 Java 安装所在的目录名。使用 **--list** 可查看可用的安装及其名称。

该工具属于基于 Debian 系统上的 java-common 软件包。

# CAVEATS

修改系统候选项需要 root 权限。只能管理由软件包管理器安装且已向 alternatives 系统注册的 Java 安装。手动安装的 Java 必须单独向 update-alternatives 注册。JAVA_HOME 环境变量可能需要在用户配置文件中另行设置。

# HISTORY

**update-java-alternatives** 为 **Debian** 和 Ubuntu 而开发，旨在简化 Java 版本管理。它要解决的问题是：多个 Java 二进制文件（java、javac、jar、keytool 等）必须同时切换，单独处理十分繁琐。自 **2000 年代初**起，该工具就是 java-common 软件包的一部分，至今仍是 Debian 系系统上管理 Java 版本的标准方式。

# SEE ALSO

[update-alternatives](/man/update-alternatives)(1), [java](/man/java)(1), [javac](/man/javac)(1)
