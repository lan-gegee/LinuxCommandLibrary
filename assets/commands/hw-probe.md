# TAGLINE

探测 Linux 硬件并将报告上传到 Linux 硬件数据库

# TLDR

**探测所有硬件**并将报告上传到 linux-hardware.org

```sudo -E hw-probe -all -upload```

**探测并运行可操作性检查**（显卡、硬盘、CPU、内存）

```sudo -E hw-probe -all -check -upload```

仅本地**探测**而不上传（保存在 `/root/HW_PROBE/` 下）

```sudo -E hw-probe -all```

**禁用**指定的日志收集器

```sudo -E hw-probe -all -upload -disable [xdpyinfo,xorg.conf]```

用资产标识符为探测结果打**标签**

```sudo -E hw-probe -all -upload -i [INVENTORY_ID]```

**生成**一个与你的邮箱关联的新资产 ID

```sudo -E hw-probe -generate-inventory -email [you@example.com]```

**安装每日 cron 任务**，探测系统并在失败时告警

```sudo -E hw-probe -start```

**转储并解码** ACPI 表（需要 `acpica-tools`）

```sudo -E hw-probe -all -dump-acpi -decode-acpi -upload```

# SYNOPSIS

**hw-probe** [_options_]

# PARAMETERS

**-all**
> 探测所有硬件。相当于启用每一个单独的探测收集器。

**-probe**
> 探测硬件（比 **-all** 更轻量的探测）。

**-logs**
> 收集系统日志（dmesg、journal、lspci、lsusb 等）。

**-log-level** _N_
> 设置日志收集详细程度：`mini`、`default` 或 `maximal`。

**-upload**
> 将生成的探测报告上传到 linux-hardware.org 并打印公开 URL。

**-check**
> 对显卡、硬盘、CPU 和内存运行可操作性测试。

**-check-graphics**
> 使用 **glxgears** 测试集成显卡和独立显卡。

**-check-hdd**
> 使用 **hdparm** 测试硬盘读取速度。

**-check-cpu**
> 使用 **dd** 和 **md5sum** 测试 CPU。

**-check-memory**
> 使用 **memtester** 测试内存。

**-id** _DESC_, **-name** _DESC_
> 为探测结果设置自定义名称或描述。

**-i** _ID_
> 用资产标识符为探测结果打标签。

**-generate-inventory**, **-generate-inventory-id**
> 申请一个新的资产 ID，与 **-email** 关联。

**-email** _ADDR_
> 与生成的资产 ID 关联的电子邮箱地址。

**-disable** _A,B,C_
> 禁用指定的日志收集器（例如 `xdpyinfo,xorg.conf`）。

**-enable** _A,B,C_
> 强制启用默认被禁用的特定日志收集器。

**-dump-acpi**
> 转储 ACPI 表。

**-decode-acpi**
> 解码已转储的 ACPI 表（需要 **acpica-tools**）。

**-show**
> 在控制台上显示探测数据摘要。

**-verbose**
> 在探测过程中打印详细的日志输出。

**-pci-ids** _PATH_, **-usb-ids** _PATH_, **-sdio-ids** _PATH_, **-pnp-ids** _PATH_
> 解码设备 ID 时使用自定义的 ID 数据库文件。

**-import** _DIR_
> 从保存有先前探测数据的目录重新创建探测报告。

**-start**
> 安装每日 cron 任务，探测系统并在硬件故障时发送邮件。

**-stop**
> 移除由 **-start** 创建的每日 cron 任务。

**-debug**
> 启用调试输出并保留临时文件。

**-help**
> 打印完整的用法信息。

# DESCRIPTION

**hw-probe** 收集机器硬件配置及相关内核/用户态日志的快照，然后可选择将其上传到 linux-hardware.org 上的公共 **Linux Hardware Database**。上传的探测报告会获得一个永久 URL，可以分享到缺陷跟踪系统、邮件列表或厂商支持请求中。

一次探测会将标准工具的输出（lspci、lsusb、lscpu、dmidecode、smartctl、lshw、edid、dmesg、Xorg.log 等）整合成一个结构化且匿名化的数据包。该数据库聚合这些报告，用于跟踪各 Linux 发行版之间的硬件兼容性、为不受支持的设备寻找合适的驱动程序，以及推荐已知能与给定配置配合工作的内核。

该工具还兼具自我监控代理的功能：通过 **-start** 会添加一个每日运行的 cron 任务，将新探测结果与前一次比较，一旦出现磁盘 SMART 错误、设备缺失或其他异常就向用户发送邮件。发行版、厂商和最终用户广泛使用它来诊断驱动问题、规划升级以及盘点机器资产。

# CAVEATS

大多数探测需要 **root** 权限才能读取 SMART 数据、DMI 表和 X 会话日志——请通过 `sudo -E` 调用，以保留环境变量（尤其是 `DISPLAY`）。带 **-check** 的完整探测由于 memtester 和磁盘计时测试可能耗时一分钟或更久。上传的探测报告是公开的；虽然经过匿名化处理，但资产标签和机器名称会原样保留，因此不要在 **-id** 或 **-i** 中包含敏感标识信息。

# CONFIGURATION

本地探测结果写入 `/root/HW_PROBE/LATEST/`（非 root 探测则写入 `~/HW_PROBE/LATEST/`）。由 **-start** 创建的 cron 任务位于 `/etc/cron.daily/hw-probe`。解码 ACPI 需要 **acpica-tools** 软件包；读取 SMART 需要 **smartmontools**；显卡检查需要 **mesa-utils** 才能运行 **glxgears**。

# HISTORY

**hw-probe** 由 **Andrey Ponomarenko** 创建，是 Linux Hardware Database 项目的前端客户端，于 **2018 年**首次发布。它用 Perl 编写，收录于 AUR、Debian/Ubuntu、Fedora、openSUSE 和 FreeBSD ports。其配套网站 linux-hardware.org 至今已收集了数百万份公开探测报告，供内核开发者和发行版维护者跟踪 Linux 硬件支持的长期变化。

# INSTALL

```dnf: sudo dnf install hw-probe```

```zypper: sudo zypper install hw-probe```

```nix: nix profile install nixpkgs#hw-probe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lshw](/man/lshw)(1), [lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8), [dmidecode](/man/dmidecode)(8), [hwinfo](/man/hwinfo)(8), [smartctl](/man/smartctl)(8), [inxi](/man/inxi)(1)
