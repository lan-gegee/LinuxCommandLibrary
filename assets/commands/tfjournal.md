# TAGLINE

记录 Terraform 运行，附带 git 上下文和耗时信息

# TLDR

**记录一次 Terraform apply**

```tfjournal -- terraform apply```

**记录时附加 workspace 标签**

```tfjournal -w [prod] -- tofu plan```

**列出最近的失败运行**

```tfjournal list --since 7d --status failed```

# SYNOPSIS

**tfjournal** [_options_] **--** _terraform-command_

# DESCRIPTION

**tfjournal** 包装 terraform、tofu 和 terragrunt 命令，以捕获输出、耗时、退出码和 git 上下文（提交、分支、用户、CI 提供商）。它解析资源级事件并能将其显示为甘特图，还可选用 S3 后端在团队间共享运行历史。

# HISTORY

**tfjournal** 由 **Owloops** 创建，使用 **Go** 编写。

# SEE ALSO

[terraform](/man/terraform)(1), [tofu](/man/tofu)(1), [terragrunt](/man/terragrunt)(1)
