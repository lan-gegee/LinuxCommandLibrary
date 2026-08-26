# TAGLINE

动态内核模块支持框架

# TLDR

列出**已安装的模块**

```dkms status```

为当前内核**重建模块**

```sudo dkms autoinstall```

**安装**某个模块版本

```sudo dkms install -m module_name -v 1.2.1```

从所有内核中**移除**模块

```sudo dkms remove -m module_name -v 1.2.1 --all```

**添加**模块源码

```sudo dkms add -m module_name -v 1.2.1```

为当前内核**构建**模块

```sudo dkms build -m module_name -v 1.2.1```

# SYNOPSIS

**dkms** _action_ [_options_] [_module/module-version_]

# DESCRIPTION

**dkms**（Dynamic Kernel Module Support）是一个框架，可为系统上的每个内核版本动态构建内核模块。安装新内核时会自动重新构建模块。

# ACTIONS

**add**
> 将模块源码添加到 DKMS 树

**remove**
> 从 DKMS 树中移除模块

**build**
> 为特定内核构建模块

**install**
> 为内核安装已构建的模块

**uninstall**
> 从内核卸载模块

**autoinstall**
> 为当前内核安装所有模块

**status**
> 显示 DKMS 管理的模块状态

**mkdriverdisk**
> 创建驱动盘镜像

**mktarball**
> 创建模块源码的 tar 包

# PARAMETERS

**-m, --module**
> 指定模块名

**-v, --version**
> 指定模块版本

**-k, --kernelver**
> 指定内核版本

**--all**
> 应用于所有内核版本

**-c, --config**
> 指定 dkms.conf 的位置

# CONFIGURATION

**/etc/dkms/framework.conf**
> DKMS 框架的全局配置。

**/usr/src/MODULE-VERSION/dkms.conf**
> 各模块的构建配置、依赖关系和安装说明。

# CAVEATS

DKMS 需要已安装内核头文件。模块源码存放在 /usr/src/ 中。配置得当时，内核升级会触发模块自动重建。

# HISTORY

**dkms** 由 Dell 开发，用于在内核更新后维护树外内核模块而无需手动重新构建。

# INSTALL

```dnf: sudo dnf install dkms```

```pacman: sudo pacman -S dkms```

```zypper: sudo zypper install dkms```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[modprobe](/man/modprobe)(8), [insmod](/man/insmod)(8), [make](/man/make)(1)

# RESOURCES

```[Source code](https://github.com/dell/dkms)```

<!-- verified: 2026-07-11 -->
