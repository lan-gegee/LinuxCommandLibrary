# TAGLINE

在 Arch Linux 上切换已安装的 Java 环境

# TLDR

**列出**已安装的 Java 环境

```archlinux-java status```

**获取**当前的默认 Java 环境

```archlinux-java get```

**设置**默认 Java 环境

```archlinux-java set java-17-openjdk```

**取消设置**默认 Java 环境

```archlinux-java unset```

**修复**无效或损坏的默认 Java 配置

```archlinux-java fix```

# SYNOPSIS

**archlinux-java** _command_ [_arguments_]

# DESCRIPTION

**archlinux-java** 是 Arch Linux 上用于切换已安装 Java 环境的工具。它管理 /usr/lib/jvm/default 和 /usr/lib/jvm/default-runtime 处的符号链接，从而系统级地设定默认 Java 版本。该工具由 **java-runtime-common** 软件包提供。

# PARAMETERS

**status**
> 列出所有已安装的 Java 环境并显示哪个是默认项

**get**
> 返回当前默认 Java 环境的短名称

**set JAVA_ENV**
> 将指定的 Java 环境设为默认

**unset**
> 移除默认 Java 环境设置

**fix**
> 修复无效或损坏的默认 Java 环境配置。若未设置默认值，则查找有效环境并自动设置一个，优先选择 OpenJDK。

# CAVEATS

**set**、**unset** 和 **fix** 命令需要 root 权限。Java 环境安装在 /usr/lib/jvm/ 下。更改对新 Shell 会话生效。**set** 的 JAVA_ENV 参数必须与 /usr/lib/jvm/ 下的目录名一致（如 java-17-openjdk、java-21-openjdk）。

# HISTORY

**archlinux-java** 是 Arch Linux 特有的多 Java 安装管理工具，类似于基于 Debian 系统上的 update-alternatives。

# SEE ALSO

[java](/man/java)(1), [update-alternatives](/man/update-alternatives)(1)
