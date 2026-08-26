# TAGLINE

开源的基础设施即代码工具

# TLDR

**初始化目录**

```tofu init```

**规划变更**

```tofu plan```

**应用变更**

```tofu apply```

**销毁资源**

```tofu destroy```

**格式化文件**

```tofu fmt```

**校验配置**

```tofu validate```

# SYNOPSIS

**tofu** _command_ [_options_]

# PARAMETERS

**init**
> 初始化工作目录。

**plan**
> 显示执行计划。

**apply**
> 应用变更。

**destroy**
> 移除资源。

**fmt**
> 格式化文件。

**validate**
> 检查配置。

**-auto-approve**
> 跳过审批。

# DESCRIPTION

**tofu**（OpenTofu）是一款从 Terraform 分叉而来的开源基础设施即代码工具，让你在声明式 HCL 配置文件中定义云端和本地资源。它通过提供者插件系统支持 AWS、GCP、Azure 等主要云服务商。

工作流程遵循 init-plan-apply 循环：**init** 下载提供者和模块，**plan** 预览提议的变更，**apply** 创建或修改实际基础设施。状态记录在一个状态文件中，该文件将配置映射到真实资源，从而支持增量更新以及使用 **destroy** 安全地销毁。

# CAVEATS

Terraform 的分支。注意提供者兼容性。状态文件非常重要。

# HISTORY

在 HashiCorp 更改 Terraform 许可证后，**OpenTofu** 于 2023 年从 **Terraform** 分叉而来，由 Linux 基金会维护。

# INSTALL

```dnf: sudo dnf install opentofu```

```pacman: sudo pacman -S opentofu```

```apk: sudo apk add opentofu```

```zypper: sudo zypper install opentofu```

```brew: brew install opentofu```

```nix: nix profile install nixpkgs#opentofu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1), [ansible](/man/ansible)(1)
