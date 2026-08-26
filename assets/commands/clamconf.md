# TAGLINE

ClamAV 配置显示与生成工具

# TLDR

**显示所有 ClamAV 配置**项

```clamconf```

**显示指定目录中的配置**

```clamconf -c [/etc/clamav]```

**生成 clamd.conf 示例文件**

```clamconf -g clamd.conf```

**生成 freshclam.conf 示例文件**

```clamconf -g freshclam.conf```

**只显示非默认设置**

```clamconf -n```

# SYNOPSIS

**clamconf** [_options_]

# PARAMETERS

**-c** _DIR_, **--config-dir**=_DIR_
> 在指定目录中查找 clamd.conf 和 freshclam.conf。

**-g** _NAME_, **--generate-config**=_NAME_
> 生成示例配置文件（clamd.conf 或 freshclam.conf）。

**-n**, **--non-default**
> 只显示非默认设置。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**clamconf** 是一个用于显示 ClamAV 配置设置、编译期取值、操作系统详情和病毒数据库信息的实用工具。它读取 clamd 和 freshclam 的配置文件并展示其当前值，非常适合核对设置和排查配置问题。

该工具同时显示显式设置的值和默认值，并突出标示哪些选项与默认值不同。它还会显示已加载病毒特征数据库的信息，包括数据库版本、特征数量和构建时间。其设计灵感来自 Postfix 的 **postconf** 工具。

系统管理员使用 clamconf 核实 ClamAV 安装配置是否正确、为新部署生成示例配置文件，以及通过检查生效的设置来排查扫描或更新问题。

# CONFIGURATION

**/etc/clamav/clamd.conf**
> ClamAV 守护进程配置文件。

**/etc/clamav/freshclam.conf**
> 病毒数据库更新配置文件。

# CAVEATS

clamconf 只读取配置文件，不会验证 clamd 或 freshclam 服务是否确实以这些设置运行。对配置文件的更改需要重启相应服务才能生效。

# HISTORY

clamconf 作为 **ClamAV** 套件的一部分引入，用于简化配置管理。ClamAV 起源于 **2001** 年，随着这款杀毒引擎的发展，配置选项日益复杂，clamconf 在后来加入以帮助管理员进行管理。

# INSTALL

```apt: sudo apt install clamav-daemon```

```apk: sudo apk add clamav-daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clamscan](/man/clamscan)(1), [clamd](/man/clamd)(8), [freshclam](/man/freshclam)(1), [clamav](/man/clamav)(1)
