# TAGLINE

SCAP 安全合规扫描的图形界面

# TLDR

**启动 SCAP Workbench**

```scap-workbench```

**打开指定的 SCAP 内容文件**

```scap-workbench [/usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml]```

**以指定 profile 打开**

```scap-workbench --profile [xccdf_org.ssgproject.content_profile_pci-dss]```

# SYNOPSIS

**scap-workbench** [_options_] [_SCAP_content_]

# PARAMETERS

**--profile** _id_
> 从内容中选择特定的 profile

**--tailoring** _file_
> 加载用于自定义 profile 的 tailoring 文件

**--skip-valid**
> 跳过内容校验

**-h**, **--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**SCAP Workbench** 是一款基于安全内容自动化协议（SCAP）的安全合规扫描图形化工具。它提供直观的界面，可依据 PCI-DSS、HIPAA、OSPP 等安全策略评估系统。

该工具使用 XCCDF（Extensible Configuration Checklist Description Format，可扩展配置检查清单描述格式）和 OVAL（Open Vulnerability and Assessment Language，开放漏洞与评估语言）来定义和检查安全配置。它可以扫描本地或远程系统、生成 HTML 报告并应用修复脚本。

安全内容通常由 **scap-security-guide** 软件包提供，安装在 /usr/share/xml/scap/ssg/content/ 中。结果可以导出为 XCCDF、ARF（Asset Reporting Format）或 HTML 格式。

# CAVEATS

SCAP Workbench 只能处理数据流文件，相比 **oscap** 命令行工具某些功能受限。修复过程中的系统修改需要 root 权限。在应用到生产系统之前务必先审查修复操作。

# HISTORY

SCAP Workbench 是 **OpenSCAP** 生态系统的一部分，旨在提供对 SCAP 合规扫描的图形化访问。OpenSCAP 通过了 NIST 认证，在企业环境中被广泛用于安全自动化与合规验证。

# INSTALL

```aur: yay -S scap-workbench```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oscap](/man/oscap)(8), [lynis](/man/lynis)(8)
