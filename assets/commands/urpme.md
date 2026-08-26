# TAGLINE

在 Mageia Linux 上移除软件包

# TLDR

**卸载**软件包

```sudo urpme [package]```

移除不再需要的**孤儿**软件包

```sudo urpme --auto-orphans```

移除软件包并**自动确认**

```sudo urpme --auto [package]```

**模拟**移除软件包而不实际移除

```urpme --test [package]```

移除软件包并清理**孤立的依赖**

```sudo urpme --auto-orphans [package]```

# SYNOPSIS

**urpme** [_OPTIONS_] _PACKAGE_...

# PARAMETERS

**--auto-orphans**
> 移除孤儿软件包（不再被任何依赖关系需要的包）。

**--auto**
> 自动确认移除，不再询问。

**--test**
> 模拟移除过程，不实际更改系统。

**--justdb**
> 只更新 RPM 数据库，不删除文件。

**--noscripts**
> 移除过程中不执行软件包的脚本片段。

**-a**
> 当名称存在歧义时，移除所有匹配的软件包。

**-v, --verbose**
> 详细输出。

# DESCRIPTION

**urpme** 用于卸载 Mageia Linux 上的软件包。它会处理软件包移除过程中的依赖检查，还能自动清除不再被任何已安装软件包需要的孤儿软件包。

属于 Mageia（前身为 Mandriva Linux）的 urpmi 软件包管理套件。

# CAVEATS

这是 Mageia 专用工具。使用 --auto-orphans 时务必小心，它可能会移除你仍然间接需要的软件包。实际移除需要 root 权限。建议先使用 --test 预览将要进行的更改。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmq](/man/urpmq)(8), [urpmi.update](/man/urpmi.update)(8), [rpm](/man/rpm)(8)
