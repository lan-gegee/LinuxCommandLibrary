# TAGLINE

检测 CPU 推测执行漏洞

# TLDR

检查当前**运行的内核**

```sudo spectre-meltdown-checker```

检查并给出缓解措施的**解释说明**

```sudo spectre-meltdown-checker --explain```

检查**特定变体**

```sudo spectre-meltdown-checker --variant [1|2|3|3a|4|l1tf|msbds|taa]```

以**机器可读格式**输出

```sudo spectre-meltdown-checker --batch [text|json|nrpe|prometheus|short]```

检查**未运行的内核**

```sudo spectre-meltdown-checker --kernel [path/to/kernel]```

跳过 **/sys 接口**

```sudo spectre-meltdown-checker --no-sysfs```

**更新**微码数据库

```sudo spectre-meltdown-checker --update-fwdb```

# SYNOPSIS

**spectre-meltdown-checker** [_OPTIONS_]

# PARAMETERS

**--kernel** _file_
> 指定要检查的内核映像文件

**--config** _file_
> 指定内核配置文件

**--map** _file_
> 指定 System.map 文件

**--live**
> 指定文件时强制使用实时模式

**--variant** _variant_
> 检查特定的漏洞变体（可重复）

**--cve** _cve_
> 检查特定的 CVE（可重复）

**--explain**
> 提供人类可读的缓解措施说明

**--batch** _format_
> 机器可读输出：text, short, json, nrpe, prometheus

**--no-color**
> 禁用彩色输出

**-v, --verbose**
> 提高详细程度（可重复）

**--paranoid**
> 应用更严格的缓解措施判定标准

**--hw-only**
> 仅检查 CPU 信息

**--no-sysfs**
> 跳过 /sys 接口

**--sysfs-only**
> 仅使用 /sys 接口

**--update-fwdb**
> 更新本地 CPU 微码数据库

# DESCRIPTION

**spectre-meltdown-checker** 检测 CPU 漏洞并验证针对 Spectre、Meltdown 及相关推测执行攻击的缓解措施。它可以在实时模式（分析正在运行的内核）或离线模式（检查内核文件）下运行。

该工具检查多种漏洞变体，包括 Spectre v1/v2、Meltdown（v3）、SSB（v4）、L1TF、MDS 变体（MSBDS、MFBDS、MLPDS）、TAA 等。它报告漏洞状态以及是否已部署正确的缓解措施。

# RETURN CODES

**0**: 不存在漏洞
**2**: 存在漏洞
**3**: 状态未知
**255**: 发生错误

# CAVEATS

完整分析需要 root 权限。结果取决于内核版本、CPU 微码和配置。在特殊配置下可能出现误报/漏报。缓解措施可能影响性能。请保持工具更新以获得新的漏洞检查能力。

# HISTORY

**spectre-meltdown-checker** 由 **Stephane Lesimple** 创建，用于应对 **2018 年 1 月**披露的 Spectre 和 Meltdown 漏洞。这些 CPU 漏洞影响了大多数现代处理器，需要与 Intel、AMD 和 ARM 协调披露。该工具持续更新，以检测新的推测执行漏洞。

# INSTALL

```dnf: sudo dnf install spectre-meltdown-checker```

```zypper: sudo zypper install spectre-meltdown-checker```

```nix: nix profile install nixpkgs#spectre-meltdown-checker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lscpu](/man/lscpu)(1), [dmesg](/man/dmesg)(1), [uname](/man/uname)(1)
