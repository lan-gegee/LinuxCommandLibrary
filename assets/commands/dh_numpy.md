# TAGLINE

管理 NumPy ABI 依赖的 debhelper addon

# TLDR

**为软件包添加 NumPy 依赖**

```dh_numpy```

**以详细输出模式**处理

```dh_numpy -v```

**处理指定软件包**

```dh_numpy -p [package_name]```

# SYNOPSIS

**dh_numpy** [_debhelper-options_]

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

**-p** _PACKAGE_, **--package** _PACKAGE_
> 只处理指定软件包。

**-N** _PACKAGE_
> 排除指定软件包。

**-a**, **--arch**
> 处理架构相关的软件包。

**-i**, **--indep**
> 处理架构无关的软件包。

# DESCRIPTION

**dh_numpy** 是面向使用 NumPy 的 Debian 软件包的 debhelper addon。它会自动为包含针对 NumPy 编译扩展的软件包添加正确的 NumPy ABI 依赖。

NumPy 扩展针对某个版本编译后，可能因 ABI 变化而无法在其他版本上工作。dh_numpy 检查已安装的扩展，并添加相应的 numpy-abiN 依赖以确保二进制兼容性。

这种自动化避免了 NumPy 升级后因缺失或错误的 ABI 依赖而导致扩展失效这一常见问题。

# CAVEATS

只对包含编译型 NumPy 扩展的软件包有意义。构建时需要 NumPy 开发头文件。NumPy 的 ABI 版本策略会影响依赖生成。

# HISTORY

dh_numpy 为 Debian Python 生态而创建，用于应对 NumPy 二进制兼容性的复杂性。它解决了在 NumPy 版本更新时维护正确依赖关系的难题。

# SEE ALSO

[dh](/man/dh)(1)
