# TAGLINE

Amazon Route 53 DNS 管理工具

# TLDR

**列出所有托管区域**

```cli53 list```

以 BIND 格式**导出某个域名的 DNS 记录**

```cli53 export [example.com]```

从 BIND 区域文件**导入 DNS 记录**

```cli53 import --file [zone.txt] [example.com]```

使用替换模式**导入**，覆盖现有记录

```cli53 import --file [zone.txt] --replace [example.com]```

**创建新的 DNS 记录**

```cli53 rrcreate [example.com] '[www 300 A 192.0.2.1]'```

**创建或替换**已有的 DNS 记录

```cli53 rrcreate --replace [example.com] '[www 60 CNAME other.example.com.]'```

**删除一条 DNS 记录**

```cli53 rrdelete [example.com] [www] [A]```

**创建新的托管区域**

```cli53 create [example.com]```

**清除区域内的所有记录**（保留 NS 和 SOA）

```cli53 rrpurge --confirm [example.com]```

# SYNOPSIS

**cli53** _command_ [_options_] [_arguments_]

# PARAMETERS

**list**
> 列出账户中的所有托管区域。

**export** _ZONE_
> 以 BIND 格式导出区域记录。

**import** _ZONE_
> 从 BIND 区域文件导入记录。

**rrcreate** _ZONE_ _RECORD_
> 创建资源记录。

**rrdelete** _ZONE_ _NAME_ _TYPE_
> 删除资源记录。

**create** _ZONE_
> 创建新的托管区域。

**delete** _ZONE_
> 删除托管区域。

**rrpurge** _ZONE_
> 删除区域内除 NS 和 SOA 之外的所有记录。

**validate** _ZONE_
> 校验 BIND 区域文件。

**--file** _FILE_
> 包含待导入或待校验区域记录的文件。

**--replace**
> 在导入或 rrcreate 时替换现有记录。

**--wait**
> 等待变更传播完成后再返回。

**--confirm**
> 不经提示直接确认破坏性操作。

**--dry-run**
> 预览变更而不实际应用。

**--full**
> 导出完全限定域名。

**--identifier** _ID_
> 加权/故障转移记录的路由策略标识符。

**--weight** _N_
> 加权路由策略的权重值。

**--profile** _NAME_
> 使用指定的 AWS 凭证 profile。

**--endpoint-url** _URL_
> 自定义 Route 53 端点 URL。

# DESCRIPTION

**cli53** 是一个用于管理 Amazon Web Services Route 53 DNS 服务的命令行工具。它提供直观的接口，可使用熟悉的 BIND 区域文件格式创建、修改、导出和导入 DNS 记录。

该工具支持全部 Route 53 记录类型，包括 A、AAAA、CNAME、MX、TXT、SRV 和别名记录。它可以将整个区域导出为 BIND 格式以便备份或迁移，也可以从区域文件导入记录进行批量更新。

cli53 使用标准的 AWS 凭证处理机制，支持环境变量、凭证文件和 IAM 角色。它对基础设施自动化、灾难恢复准备以及在 DNS 服务商之间迁移记录特别有用。

# CAVEATS

需要通过环境变量或 AWS 凭证文件配置具有 Route 53 权限的 AWS 凭证。**rrpurge** 命令具有破坏性且无法撤销。当同一域名存在多个区域时，可以使用区域 ID 代替域名来消除歧义。

# HISTORY

cli53 是一个为简化命令行下 Route 53 管理而创建的开源工具。其名称源于 Route 53 的端口关联（DNS 使用 53 端口），它提供了比 AWS CLI 的 Route 53 命令更友好的替代方案，尤其适合使用 BIND 区域文件格式的批量操作。

# INSTALL

```brew: brew install cli53```

```nix: nix profile install nixpkgs#cli53```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [dig](/man/dig)(1), [host](/man/host)(1), [nslookup](/man/nslookup)(1)
