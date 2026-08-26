# TAGLINE

管理 Amazon EC2 上的虚拟服务器和网络。

# TLDR

**启动新的 EC2 实例**

```aws ec2 run-instances --image-id [ami-0c55b159cbfafe1f0] --instance-type [t2.micro] --key-name [my-key]```

**列出所有实例及其状态**

```aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]" --output table```

**停止运行中的实例**

```aws ec2 stop-instances --instance-ids [i-1234567890abcdef0]```

**启动已停止的实例**

```aws ec2 start-instances --instance-ids [i-1234567890abcdef0]```

**永久终止实例**

```aws ec2 terminate-instances --instance-ids [i-1234567890abcdef0]```

**创建安全组并添加 SSH 规则**

```aws ec2 create-security-group --group-name [my-sg] --description "[My security group]" && aws ec2 authorize-security-group-ingress --group-name [my-sg] --protocol tcp --port 22 --cidr 0.0.0.0/0```

**创建密钥对并保存**

```aws ec2 create-key-pair --key-name [my-key] --query "KeyMaterial" --output text > [my-key.pem]```

**列出安全组及其规则**

```aws ec2 describe-security-groups --query "SecurityGroups[*].[GroupId,GroupName]" --output table```

# SYNOPSIS

**aws ec2** _command_ [_options_]

# DESCRIPTION

**aws ec2** 是 Amazon Elastic Compute Cloud（EC2）的 AWS CLI 接口，提供对可扩展计算容量的编程访问。通过 EC2 可以启动虚拟服务器、配置网络与安全以及管理存储。

EC2 命令涵盖实例生命周期管理、Amazon 系统镜像（AMI）、弹性块存储（EBS）卷、VPC 网络、安全组和密钥对。该服务支持按需、预留和竞价（Spot）三种定价模式。

# COMMANDS

**run-instances**
> 启动新的 EC2 实例

**describe-instances**
> 列出并描述实例

**start-instances**
> 启动已停止的实例

**stop-instances**
> 停止运行中的实例

**terminate-instances**
> 永久删除实例

**reboot-instances**
> 重启运行中的实例

**create-image**
> 从实例创建 AMI

**create-security-group**
> 创建安全组

**describe-security-groups**
> 列出并描述安全组

**authorize-security-group-ingress**
> 向安全组添加入站规则

**create-key-pair**
> 生成新密钥对

**create-vpc**
> 创建 Virtual Private Cloud

**create-volume**
> 创建 EBS 卷

**attach-volume**
> 将卷附加到实例

# CAVEATS

对于基于 EBS 的实例，只有终止（而非仅仅停止）后才会停止计费。安全组规则是有状态的，而 NACL 则不是。实例元数据服务（IMDS）v1 不安全，请改用 IMDSv2。Spot 实例可能只提前 2 分钟收到终止通知。

# HISTORY

Amazon EC2 于 **2006 年 8 月** 作为 AWS 最早的服务之一推出，彻底改变了云计算行业。VPC 于 **2013 年** 成为强制要求。实例类型持续扩充，从最初的 m1.small 发展到数百种针对计算、内存、GPU 和存储优化的专用类型。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-autoscaling](/man/aws-autoscaling)(1), [aws-elb](/man/aws-elb)(1), [aws-vpc](/man/aws-vpc)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html)```

<!-- verified: 2026-06-18 -->
