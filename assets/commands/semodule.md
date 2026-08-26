# TAGLINE

管理 SELinux 策略模块

# TLDR

**列出**所有已安装的策略模块

```sudo semodule -l```

**安装**新的策略模块

```sudo semodule -i path/to/module.pp```

**移除**策略模块

```sudo semodule -r module_name```

**启用**策略模块

```sudo semodule -e module_name```

**禁用**策略模块

```sudo semodule -d module_name```

**重新加载**所有策略模块

```sudo semodule -R```

**列出**模块并显示详细的版本信息

```sudo semodule -l -v```

# SYNOPSIS

**semodule** [_options_]

# PARAMETERS

**-l**, **--list**
> 列出已安装的模块

**-i**, **--install** _file_
> 安装策略模块（.pp 文件）

**-r**, **--remove** _name_
> 移除模块

**-e**, **--enable** _name_
> 启用模块

**-d**, **--disable** _name_
> 禁用模块

**-R**, **--reload**
> 强制重新加载策略。

**-B**, **--build**
> 强制重建策略（除非使用 -n，否则也会重新加载）。

**-X**, **--priority** _PRIORITY_
> 为后续操作设置优先级（1-999）。

**-s**, **--store** _NAME_
> 要操作的存储库名称。

**-n**, **--noreload**
> 提交后不重新加载策略。

**-D**, **--disable_dontaudit**
> 从策略中临时移除 dontaudit 规则。

**-v**, **--verbose**
> 显示详细输出。

# DESCRIPTION

**semodule** 管理 SELinux 策略模块。它负责安装、移除、启用和禁用扩展基础 SELinux 策略的模块化策略组件。

策略模块允许在不修改基础策略的情况下自定义 SELinux 规则。

# CAVEATS

模块变更需要重新加载策略。安装不兼容的模块可能导致策略错误。

# HISTORY

属于 **policycoreutils** 的一部分，提供模块化的 SELinux 策略管理。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[audit2allow](/man/audit2allow)(1), [semanage](/man/semanage)(8)
