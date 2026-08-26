# TAGLINE

从 akmod 软件包重建树外内核模块

# TLDR

为当前运行的内核**检查并重建**缺失或过期的模块

```sudo akmods```

即使构建失败或看似最新也**强制重建**所有模块

```sudo akmods --rebuild --force```

只为**特定内核**（与 `uname -r` 格式相同）构建并安装模块

```sudo akmods --kernels [kernel_version]```

只重建一个 **akmod** 软件包

```sudo akmods --akmod [akmod_name]```

查看后台 **akmods 服务**的状态

```systemctl status akmods```

# SYNOPSIS

**akmods** [_options_]

# DESCRIPTION

**akmods** 检查已安装的 **akmod** 软件包，并在树外内核模块缺失、过期或对给定内核失效时重建它们。它是 Fedora/RHEL 系对 DKMS 这类框架的对等物：**akmod** 软件包附带模块源码和构建元数据；每当新内核出现时，**akmods** 就在本地系统上编译它们（通常编译成匹配的 **kmod-*** RPM）。

典型用法是在从 RPM Fusion 安装或更新驱动之后（例如通过 **akmod-nvidia** 安装 NVIDIA）。systemd 单元可以在启动时运行 **akmods**，使当前内核的模块在需要之前就准备就绪。当某次构建失败、之前的尝试缺少 **kernel-devel**，或你需要为非当前运行的内核提供模块时，手动运行很常见。

构建需要编译工具链以及每个目标内核匹配的内核头文件/devel 软件包。Secure Boot 配置可能还需要 **/etc/pki/akmods** 下的模块签名密钥。

# OPTIONS

**--force**

> 尝试所有 akmod，包括之前运行中失败的那些。

**--kernels** _kernel_

> 只为给定的内核版本字符串（与 **uname -r** 格式相同）构建并安装。

**--rebuild**

> 即使模块看起来已是最新，也全部重建。

**--akmod** _akmod_

> 只构建并安装指定名称的 akmod 软件包。

**--quiet**

> 减少输出。

**--verbose**

> 增加输出。

# CAVEATS

构建失败后往往没有可用的 **kmod**，直到头文件、编译工具和足够的磁盘空间就绪后再重新运行 **akmods --force** 或 **--rebuild**。在基于 ostree 的系统（Silverblue/Kinoite）上，模块签名和重建时机可能与传统软件包安装不同。man page 内容较少；**akmods** 服务下的日志输出和 journal 通常是最好的诊断线索。

# INSTALL

```dnf: sudo dnf install akmods```

<!-- packages: 2026-08-10 -->

# SEE ALSO

[dkms](/man/dkms)(1), [modprobe](/man/modprobe)(8), [uname](/man/uname)(1)

# RESOURCES

```[Documentation](https://rpmfusion.org/Packaging/KernelModules/Akmods)```

<!-- verified: 2026-08-10 -->
