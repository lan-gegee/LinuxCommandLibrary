# TAGLINE

管理多账户 AWS 环境

# TLDR

**描述组织**

```aws organizations describe-organization```

**列出组织中的所有账户**

```aws organizations list-accounts```

**列出**某个父节点下的**组织单元**

```aws organizations list-organizational-units-for-parent --parent-id [r-xxxx|ou-xxxx-xxxxxxxx]```

**创建新账户**

```aws organizations create-account --account-name "[Account Name]" --email [admin@example.com]```

将**账户移动到**另一个 OU

```aws organizations move-account --account-id [123456789012] --source-parent-id [ou-source] --destination-parent-id [ou-dest]```

**列出**特定类型的**策略**

```aws organizations list-policies --filter SERVICE_CONTROL_POLICY```

将**策略附加到**账户或 OU

```aws organizations attach-policy --policy-id [p-xxxxxxxx] --target-id [account-id|ou-id]```

**列出**父 OU 下的**账户**

```aws organizations list-accounts-for-parent --parent-id [ou-xxxx-xxxxxxxx]```

# SYNOPSIS

**aws organizations** _subcommand_ [_options_]

# DESCRIPTION

**aws organizations** 是 AWS CLI 的一个子命令，用于管理 AWS Organizations。这项服务用于集中管理多个 AWS 账户，支持合并账单、账户创建和基于策略的治理。

组织采用层级结构：根（root）下包含组织单元（OU）和账户。服务控制策略（SCP）设置权限防护栏，作用于目标账户或 OU 中的所有主体，限制可执行的操作。

管理账户（旧称 master）负责创建和控制组织。成员账户可以在组织内创建，也可以邀请现有账户加入。

# PARAMETERS

**describe-organization**
> 获取组织详情和功能状态。

**list-accounts**
> 列出组织中的所有账户。

**list-roots**
> 列出组织的根。

**list-organizational-units-for-parent**
> 列出某个父节点下的 OU。

**list-accounts-for-parent**
> 列出直接位于某 OU 中的账户。

**create-account**
> 创建新的成员账户。

**create-organizational-unit**
> 创建新的 OU。

**move-account**
> 在 OU 之间移动账户。

**list-policies**
> 列出指定类型的策略。

**create-policy**
> 创建新策略。

**attach-policy**
> 将策略附加到目标。

**detach-policy**
> 从目标移除策略。

**describe-account**
> 获取账户详情。

**--parent-id** _id_
> 根或 OU 的标识符。

**--account-id** _id_
> 12 位 AWS 账户 ID。

**--policy-id** _id_
> 策略标识符。

**--target-id** _id_
> 要作为目标的账户、OU 或根。

**--filter** _type_
> 策略类型过滤器：SERVICE_CONTROL_POLICY、TAG_POLICY、BACKUP_POLICY、AISERVICES_OPT_OUT_POLICY。

# CAVEATS

Organizations 命令必须从管理账户运行。SCP 不授予权限，只做限制。管理账户不受 SCP 影响。账户创建是异步的；可用 describe-create-account-status 检查状态。将账户从组织中移除时，该账户必须已配置支付方式才能独立结算。

# HISTORY

**AWS Organizations** 于 **2017 年 2 月**上线，用于实现多账户管理。**Service Control Policies** 提供了集中式治理。**Consolidated Billing** 由早期的合并账单功能合并而来。功能随后扩展至**标签策略**、**备份策略**和 **AI 服务退出策略**。于 **2019 年**发布的 AWS Control Tower 基于 Organizations 实现着陆区自动化。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-iam](/man/aws-iam)(1), [aws-sts](/man/aws-sts)(1), [aws-sso](/man/aws-sso)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/organizations/index.html)```

<!-- verified: 2026-06-18 -->
