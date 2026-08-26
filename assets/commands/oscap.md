# TAGLINE

基于 SCAP 的安全合规 OpenSCAP 命令行扫描器

# TLDR

**显示内容文件中的配置文件和元数据**

```oscap info [content.xml]```

**按 XCCDF 配置文件扫描系统**并生成 XML + HTML 报告

```oscap xccdf eval --profile [profile_id] --results [results.xml] --report [report.html] [ssg-content.xml]```

**扫描并自动修复**未通过的规则

```oscap xccdf eval --remediate --profile [profile_id] [ssg-content.xml]```

**允许下载 XCCDF 引用的远程 OVAL 内容**

```oscap xccdf eval --fetch-remote-resources --profile [profile_id] [ssg-content.xml]```

**使用定制（tailoring）文件中的裁剪版配置文件**

```oscap xccdf eval --tailoring-file [tailoring.xml] --profile [tailored_profile_id] [ssg-content.xml]```

**运行 OVAL 定义文件**（例如 CVE 订阅源）

```oscap oval eval --results [results.xml] --report [report.html] [oval-definitions.xml]```

**生成修复脚本**（Bash、Ansible 或 Puppet）

```oscap xccdf generate fix --fix-type [bash|ansible|puppet] --profile [profile_id] --output [fix.sh] [content.xml]```

# SYNOPSIS

**oscap** [_global_options_] _module_ _operation_ [_operation_options_] _content_file_

# MODULES

**info**
> 打印有关 SCAP 文件的元数据（配置文件、数据流、OVAL 数量）。

**xccdf**
> XCCDF（Extensible Configuration Checklist Description Format，可扩展配置检查表描述格式）操作：**eval**、**resolve**、**validate**、**export-oval-variables**、**generate** _subcommand_。

**oval**
> OVAL（Open Vulnerability and Assessment Language，开放漏洞与评估语言）操作：**eval**、**collect**、**analyse**、**validate**、**list-probes**、**generate report**。

**ds**
> 数据流操作：**sds-compose**、**sds-split**、**sds-validate**、**rds-create**、**rds-split**、**rds-validate**。

**cpe**
> CPE（Common Platform Enumeration，通用平台枚举）操作。

**cvss**
> 从向量字符串计算 CVSS 评分。

# COMMON OPTIONS

**--profile** _ID_
> 要评估的 XCCDF 配置文件。

**--results** _FILE_
> 写入机器可读的 XCCDF/ARF 结果文件。

**--report** _FILE_
> 写入人类可读的 HTML 报告。

**--oval-results**
> 除 **--results** 外，同时为每个 OVAL 定义写出结果文件。

**--cpe** _FILE_
> 使用给定的 CPE 字典或语言进行适用性检查。

**--tailoring-file** _FILE_
> 应用定制 XML 文件以自定义配置文件。

**--tailoring-id** _ID_
> 使用嵌入在数据流中的定制组件。

**--fetch-remote-resources**
> 允许 OpenSCAP 下载 XCCDF 引用的远程 OVAL 内容。

**--remediate**
> 对评估未通过的规则执行 XCCDF 修复脚本。**请谨慎使用——会修改系统。**

**--rule** _ID_
> 将评估限制到指定规则（可重复）。

**--skip-rule** _ID_
> 跳过指定规则（可重复）。

**--datastream-id** _ID_, **--xccdf-id** _ID_, **--benchmark-id** _ID_
> 当文件是多流数据流时，选择特定的组件。

**--fix-type** _TYPE_
> 用于 **generate fix**：bash（默认）、ansible、puppet、kubernetes、anaconda、ignition、blueprint。

**-V**, **--version**
> 打印版本、支持的功能及探针列表。

# DESCRIPTION

**oscap** 是 OpenSCAP 的命令行工具，用于依据 SCAP（Security Content Automation Protocol，安全内容自动化协议）内容评估系统。它可以运行 XCCDF 基准、针对漏洞或配置问题评估 OVAL 定义、生成人类可读的报告，甚至自动应用修复。

典型内容来自 **scap-security-guide**（SSG）项目发布的数据流文件，例如 **/usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml**，其中提供 **xccdf_org.ssgproject.content_profile_cis** 或 **_pci-dss** 等配置文件。

# CAVEATS

需要 SCAP 内容（通常来自 **scap-security-guide**）。完整的系统扫描通常必须以 root 身份运行。**--remediate** 会修改实际运行的系统——使用前请审查配置文件并在测试环境中验证。**--fetch-remote-resources** 会访问网络；在物理隔离环境中请避免使用。完整 RHEL 配置文件的报告可能非常大。

# HISTORY

**OpenSCAP** 由 **Red Hat** 于 **2008 年**启动，并于 **2014 年**成为通过 NIST 认证的 SCAP 扫描器。它是 RHEL、Fedora、CentOS、Ubuntu、SUSE 和 Oracle Linux 用于合规审计（CIS、PCI-DSS、STIG、HIPAA 等）的 SCAP 标准参考实现。

# INSTALL

```apt: sudo apt install openscap-scanner```

```dnf: sudo dnf install openscap-scanner```

```apk: sudo apk add openscap```

```zypper: sudo zypper install openscap```

```nix: nix profile install nixpkgs#openscap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scap-workbench](/man/scap-workbench)(1), [lynis](/man/lynis)(1)
