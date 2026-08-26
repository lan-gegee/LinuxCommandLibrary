# TAGLINE

在 Linux 上对 NVIDIA GPU 进行超频（X11 与 Wayland）

# TLDR

**应用**功耗上限和频率偏移

```nvidia_oc set --index [0] --power-limit [200000] --freq-offset [160] --mem-offset [850] --min-clock [0] --max-clock [2000]```

**显示帮助**

```nvidia_oc --help```

# SYNOPSIS

**nvidia_oc** **set** [*options*]

# DESCRIPTION

**nvidia_oc** 是一款 Rust 编写的命令行工具，通过 NVML 在 Linux 上对 NVIDIA GPU 进行超频。它同时支持 X11 和 Wayland，而许多旧的超频工具只支持 X11。

典型工作流程：下载发行版二进制文件，使用 GPU 索引和功耗/时钟参数运行 **set**，可选地安装 systemd 单元，以便在启动时重新应用设置。

# PARAMETERS

**set**

> 应用超频 / 电源设置。

**--index** *n*

> GPU 索引（第一个设备为 0）。

**--power-limit** *milliwatts*

> 以毫瓦为单位的功耗上限（例如：**200000** 表示 200 W；请确认你的构建版本所用单位）。

**--freq-offset** *mhz*

> GPU 核心频率偏移量。

**--mem-offset** *mhz*

> 显存频率偏移量。

**--min-clock** / **--max-clock** *mhz*

> 时钟范围边界。

完整的选项集请参阅 **nvidia_oc --help** 和 **nvidia_oc set --help**。

# CAVEATS

需要 NVIDIA 驱动程序以及更改设备时钟的权限（通常需要 root）。错误的设置可能导致 GPU/驱动崩溃或降低稳定性，请谨慎逐步调高数值。厂商和 OEM 的功耗限制可能会约束你的设置。超频可能导致保修失效并增加发热和功耗。Wayland/X11 会话的具体表现仍取决于驱动支持情况。

# INSTALL

```nix: nix profile install nixpkgs#nvidia_oc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [nvidia-settings](/man/nvidia-settings)(1)

# RESOURCES

```[Source code](https://github.com/Dreaming-Codes/nvidia_oc)```

<!-- verified: 2026-07-19 -->
