# TAGLINE

在托管基础设施上运行批处理计算工作负载

# TLDR

向现有的作业队列**提交作业**

```aws batch submit-job --job-name [my-job] --job-queue [my-queue] --job-definition [my-definition]```

**列出队列中**具有特定状态的**所有作业**

```aws batch list-jobs --job-queue [my-queue] --job-status [RUNNING|SUBMITTED|PENDING|SUCCEEDED|FAILED]```

按 ID **描述具体作业**的详细信息

```aws batch describe-jobs --jobs [job-id-1] [job-id-2]```

用指定的实例类型**创建托管计算环境**

```aws batch create-compute-environment --compute-environment-name [my-env] --type MANAGED --compute-resources type=EC2,minvCpus=0,maxvCpus=256,instanceTypes=optimal```

从 JSON 文件**注册作业定义**

```aws batch register-job-definition --cli-input-json file://[job-definition.json]```

创建关联到计算环境的**作业队列**

```aws batch create-job-queue --job-queue-name [my-queue] --priority [1] --compute-environment-order order=1,computeEnvironment=[my-env]```

按 ID **取消处于 PENDING 或 RUNNABLE 状态的作业**

```aws batch cancel-job --job-id [job-id] --reason "[cancellation reason]"```

按 ID **终止正在运行的作业**

```aws batch terminate-job --job-id [job-id] --reason "[termination reason]"```

# SYNOPSIS

**aws batch** _command_ [_options_]

# DESCRIPTION

**aws batch** 是 AWS Batch 的 AWS CLI 接口。AWS Batch 是一项完全托管的服务，用于在 AWS 云上运行批处理计算工作负载，它会自动配置计算资源并根据工作负载的数量和规模优化分配。

AWS Batch 免去了安装或管理批处理计算软件的需要，消除了容量限制并降低了总体计算成本。它支持任意规模的批处理工作负载，从简单的 shell 脚本到复杂的多节点并行作业。

# COMMANDS

**submit-job**
> 将作业定义中的批处理作业提交到作业队列

**cancel-job**
> 取消队列中处于待处理或运行状态的作业

**terminate-job**
> 终止正在运行的作业

**describe-jobs**
> 描述一个或多个作业

**list-jobs**
> 按队列和状态过滤列出作业

**register-job-definition**
> 注册新的作业定义

**describe-job-definitions**
> 描述作业定义

**create-compute-environment**
> 创建托管或非托管的计算环境

**describe-compute-environments**
> 描述计算环境

**create-job-queue**
> 创建与计算环境关联的作业队列

**describe-job-queues**
> 描述作业队列

# CAVEATS

AWS Batch 要求为计算环境、作业队列和作业执行角色配置正确的 IAM 权限。如果容器镜像不可访问或超出资源限制，作业可能静默失败。请始终使用 **describe-jobs** 监控作业状态，因为作业失败可能不会立即显现。

# HISTORY

AWS Batch 于 **2016 年 12 月**上线，是一项托管的批处理服务，旨在简化大规模运行批处理作业的过程而无需管理基础设施。该服务后来演进为支持 Fargate 计算、多节点并行作业，并与用于工作流编排的 AWS Step Functions 集成。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [aws-ecs](/man/aws-ecs)(1), [aws-lambda](/man/aws-lambda)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/batch/)```

<!-- verified: 2026-06-17 -->
