# TAGLINE

智能地向 Linux 内核添加或移除模块

# TLDR

**试运行**加载模块

```sudo modprobe -n module_name```

向内核**加载**模块

```sudo modprobe module_name```

从内核**移除**模块

```sudo modprobe -r module_name```

移除模块及其**依赖它的模块**

```sudo modprobe -r --remove-holders module_name```

显示模块**依赖关系**

```sudo modprobe -D module_name```

显示**配置**

```modprobe -c```

# SYNOPSIS

**modprobe** [_-v_] [_-n_] [_-r_] [_modulename_] [_parameters_...]

# DESCRIPTION

**modprobe** 智能地向 Linux 内核添加或移除模块。它借助 modules.dep 自动处理模块依赖，并在 /lib/modules/$(uname -r) 中搜索模块。

# PARAMETERS

**-v, --verbose**
> 打印操作的详细信息

**-n, --dry-run**
> 预览操作而不实际执行

**-r, --remove**
> 移除模块而不是插入

**-f, --force**
> 即使版本不匹配也强制加载

**-q, --quiet**
> 抑制关于缺失模块的错误信息

**-b, --use-blacklist**
> 应用配置中的黑名单规则

**-c, --showconfig**
> 显示生效的配置

**-D, --show-depends**
> 列出模块依赖关系

**--first-time**
> 若模块已加载/未加载则失败

**-i, --ignore-install**
> 忽略配置中的 install 命令

**-w, --wait=TIMEOUT**
> 若模块忙（在移除时）则等待并重试

**-S, --set-version**
> 使用指定的内核版本

**--remove-holders**
> 同时移除依赖该模块的其他模块（配合 -r）

# CONFIGURATION

/etc/modprobe.d/ 中的配置文件控制模块行为，包括别名、选项、黑名单以及 install/remove 命令。

# CAVEATS

模块名中下划线和连字符可互换使用。某些模块需要参数才能正常工作。被列入黑名单的模块仍可显式加载。

# HISTORY

**modprobe** 是 **kmod** 的一部分，取代了较旧的 module-init-tools。它通过自动依赖解析提供智能的模块管理。

# INSTALL

```apt: sudo apt install kmod```

```dnf: sudo dnf install kmod```

```pacman: sudo pacman -S kmod```

```apk: sudo apk add kmod```

```zypper: sudo zypper install kmod```

```brew: brew install kmod```

```nix: nix profile install nixpkgs#kmod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsmod](/man/lsmod)(8), [rmmod](/man/rmmod)(8), [insmod](/man/insmod)(8), [modinfo](/man/modinfo)(8), [depmod](/man/depmod)(8)
