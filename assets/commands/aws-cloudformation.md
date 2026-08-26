# TAGLINE

从声明式模板配置基础设施。

# TLDR

从模板文件**创建新堆栈**

```aws cloudformation create-stack --stack-name [my-stack] --template-body file://[template.yaml]```

用新模板**更新现有堆栈**

```aws cloudformation update-stack --stack-name [my-stack] --template-body file://[template.yaml]```

**删除堆栈**及其所有资源

```aws cloudformation delete-stack --stack-name [my-stack]```

**描述堆栈状态**和输出值

```aws cloudformation describe-stacks --stack-name [my-stack]```

在部署前**校验模板**

```aws cloudformation validate-template --template-body file://[template.yaml]```

**创建变更集**，在应用前预览改动

```aws cloudformation create-change-set --stack-name [my-stack] --change-set-name [my-changes] --template-body file://[template.yaml]```

**部署模板**（通过变更集创建或更新堆栈）

```aws cloudformation deploy --template-file [template.yaml] --stack-name [my-stack] --capabilities CAPABILITY_IAM```

**列出所有堆栈**及其状态

```aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE```

**打包模板**中的本地工件并上传到 S3

```aws cloudformation package --template-file [template.yaml] --s3-bucket [my-bucket] --output-template-file [packaged.yaml]```

# SYNOPSIS

**aws cloudformation** _command_ [_options_]

# DESCRIPTION

**aws cloudformation** 是 AWS CloudFormation 的 AWS CLI 接口。CloudFormation 是一项基础设施即代码服务，让你使用模板对 AWS 资源进行建模和配置。模板以 YAML 或 JSON 格式声明式地定义资源，由 CloudFormation 负责配置和管理。

CloudFormation 将资源作为**堆栈（stack）**管理，把所有资源的创建、更新和删除作为整体处理，并自动处理依赖关系。变更集允许你在应用之前预览修改内容。

# COMMANDS

**create-stack**
> 从模板创建新堆栈

**update-stack**
> 用变更更新现有堆栈

**delete-stack**
> 删除堆栈及其资源

**describe-stacks**
> 获取堆栈信息、状态和输出值

**validate-template**
> 检查模板的语法和结构

**create-change-set**
> 创建堆栈变更的预览

**execute-change-set**
> 将变更集应用到堆栈

**package**
> 上传本地工件并重写模板中的引用

**deploy**
> 部署模板，自动创建变更集

**list-stacks**
> 列出堆栈，可按状态过滤

**detect-stack-drift**
> 检查实际配置与模板之间的漂移

# CAVEATS

如果资源启用了删除保护或存在 CloudFormation 之外的依赖，堆栈删除可能失败。失败时回滚会自动进行，但可能使堆栈停留在 UPDATE_ROLLBACK_FAILED 状态而需要人工干预。大型模板可能触及 API 上限，需要改用嵌套堆栈。

# HISTORY

AWS CloudFormation 于 **2011 年 2 月**上线，是最早的基础设施即代码服务之一。它于 **2016 年**引入变更集以实现更安全的更新，于 **2018 年**引入漂移检测，并持续扩展资源类型覆盖范围。该服务现已支持超过 700 种 AWS 资源类型。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [aws-s3](/man/aws-s3)(1), [aws-iam](/man/aws-iam)(1), [terraform](/man/terraform)(1)
