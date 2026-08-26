# TAGLINE

管理 AWS 上的 Docker 容器镜像仓库。

# TLDR

**向 ECR 注册表认证 Docker**

```aws ecr get-login-password | docker login --username AWS --password-stdin [account-id].dkr.ecr.[region].amazonaws.com```

**创建新仓库**

```aws ecr create-repository --repository-name [my-repo]```

**列出注册表中的所有仓库**

```aws ecr describe-repositories```

**列出仓库中的镜像**

```aws ecr list-images --repository-name [my-repo]```

**查看镜像详情**（含漏洞信息）

```aws ecr describe-images --repository-name [my-repo] --image-ids imageTag=[latest]```

**按标签删除镜像**

```aws ecr batch-delete-image --repository-name [my-repo] --image-ids imageTag=[v1.0]```

**设置生命周期策略以过期旧镜像**

```aws ecr put-lifecycle-policy --repository-name [my-repo] --lifecycle-policy-text file://[policy.json]```

# SYNOPSIS

**aws ecr** _command_ [_options_]

# DESCRIPTION

**aws ecr** 是 Amazon Elastic Container Registry（ECR）的 AWS CLI 接口。ECR 是一项全托管的 Docker 容器注册表，与 Amazon ECS 和 EKS 集成，可轻松存储、管理和部署 Docker 容器镜像。

ECR 提供带基于 IAM 访问控制的私有仓库，支持自动镜像漏洞扫描、跨区域和跨账户复制，以及用于管理镜像保留的生命周期策略。

# COMMANDS

**get-login-password**
> 获取用于 Docker 登录的认证令牌

**create-repository**
> 创建新的镜像仓库

**describe-repositories**
> 列出仓库详情

**list-images**
> 列出仓库中的镜像

**describe-images**
> 获取镜像的详细信息

**batch-delete-image**
> 删除一个或多个镜像

**put-lifecycle-policy**
> 设置镜像保留规则

**start-image-scan**
> 发起漏洞扫描

**describe-image-scan-findings**
> 获取扫描结果

**put-replication-configuration**
> 配置跨区域复制

# CAVEATS

认证令牌 12 小时后过期。镜像标签默认是可变的；生产环境建议启用标签不可变性。生命周期策略异步执行，删除镜像可能需要一些时间。镜像扫描需要在每个仓库或注册表级别启用。

# HISTORY

Amazon ECR 于 **2015 年 12 月** 随 Amazon ECS 一同推出。跨区域复制于 **2020 年** 加入，由 Amazon Inspector 提供支持的增强扫描于 **2021 年** 推出。面向公共容器镜像的 ECR Public 于 **2020 年** 上线。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [docker](/man/docker)(1), [aws-ecs](/man/aws-ecs)(1), [aws-eks](/man/aws-eks)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/index.html)```

<!-- verified: 2026-06-18 -->
