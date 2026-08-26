# TAGLINE

显示 pip 环境的调试信息

# TLDR

**显示调试信息**

```pip debug```

**显示详细的调试信息**

```pip debug --verbose```

# SYNOPSIS

**pip** **debug** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 显示详细的调试信息，包括所有平台标签和已解析的兼容性规范。

**--platform** _platform_
> 显示给定平台的兼容性标签。

**--python-version** _version_
> 显示给定 Python 版本的兼容性标签。

**--implementation** _impl_
> 显示给定 Python 实现的兼容性标签（例如 **cp**、**pp**）。

**--abi** _abi_
> 显示给定 ABI 的兼容性标签。

# DESCRIPTION

**pip debug** 打印关于 pip 和当前 Python 环境的调试信息。输出包括 pip 版本、安装位置、sys.path、正在使用的 Python 解释器、支持的 wheel 兼容性标签以及已配置的索引。

该命令用于诊断 wheel 选择问题（例如 "no matching distribution found"）、索引配置问题以及 SSL/证书配置错误。它**不是**稳定接口——输出格式可能在 pip 各版本间变化，不应被脚本解析。

# CAVEATS

被标记为不稳定：pip 明确警告"此命令仅用于调试"，且格式可能变化。配合 **--verbose** 使用可查看完整的标签枚举。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-config](/man/pip-config)(1), [pip-list](/man/pip-list)(1)
