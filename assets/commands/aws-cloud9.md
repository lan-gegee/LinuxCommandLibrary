# TAGLINE

管理基于云的开发环境。

# TLDR

用 t2.micro 实例**创建新的 Cloud9 EC2 环境**

```aws cloud9 create-environment-ec2 --name [my-env] --instance-type t2.micro --image-id amazonlinux-2023-x86_64```

**列出账户中的所有 Cloud9 环境**

```aws cloud9 list-environments```

按 ID **描述特定环境**

```aws cloud9 describe-environments --environment-ids [env-id-1] [env-id-2]```

**获取环境的状态**

```aws cloud9 describe-environment-status --environment-id [env-id]```

以读写权限向环境**添加成员**

```aws cloud9 create-environment-membership --environment-id [env-id] --user-arn [arn:aws:iam::account:user/username] --permissions read-write```

**删除环境**及其关联的 EC2 实例

```aws cloud9 delete-environment --environment-id [env-id]```

# SYNOPSIS

**aws cloud9** _command_ [_options_]

# DESCRIPTION

**aws cloud9** 是 AWS Cloud9 的 AWS CLI 接口。AWS Cloud9 是一款基于云的集成开发环境（IDE），用于编写、运行和调试代码。Cloud9 提供基于浏览器的编辑器、调试器和终端，并预配置了主流编程语言所需的常用工具。

Cloud9 环境运行在 EC2 实例上，支持具备实时结对编程能力的协作开发。

# COMMANDS

**create-environment-ec2**
> 使用 EC2 实例创建新的开发环境

**delete-environment**
> 删除环境并终止其 EC2 实例

**describe-environments**
> 获取一个或多个环境的详细信息

**describe-environment-status**
> 检查环境的当前状态

**list-environments**
> 列出账户中的所有环境 ID

**create-environment-membership**
> 将用户添加到环境

**update-environment-membership**
> 更改成员的权限

**delete-environment-membership**
> 将用户从环境中移除

# CAVEATS

自 **2024 年**起，AWS Cloud9 不再对新客户开放；AWS 建议迁移到 AWS IDE Toolkits 或 AWS CloudShell。现有客户可以继续使用该服务。**create-environment-ec2** 现在需要 **--image-id**（例如 amazonlinux-2023-x86_64、ubuntu-22.04-x86_64；ubuntu-18.04 等较早的 AMI 已弃用）。除非配置了通过 **--automatic-stop-time-minutes** 实现的自动休眠，否则即使 IDE 未被主动使用，环境也会产生 EC2 费用。

# HISTORY

AWS Cloud9 于 **2010 年**作为独立公司创立，**2016 年**被 Amazon 收购。它被整合进 AWS 作为托管服务，提供基于浏览器的 IDE 能力。**2024 年**，AWS 宣布 Cloud9 不再接受新客户。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [aws-codecommit](/man/aws-codecommit)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/cloud9/index.html)```

<!-- verified: 2026-06-18 -->
