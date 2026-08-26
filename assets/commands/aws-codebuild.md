# TAGLINE

运行托管的持续集成构建。

# TLDR

**为项目启动构建**

```aws codebuild start-build --project-name [my-project]```

**启动构建并覆盖环境变量**

```aws codebuild start-build --project-name [my-project] --environment-variables-override name=MY_VAR,value=myvalue```

**从 JSON 配置创建项目**

```aws codebuild create-project --cli-input-json file://[project.json]```

**生成项目模板 JSON**

```aws codebuild create-project --generate-cli-skeleton > [project.json]```

**列出所有项目**

```aws codebuild list-projects```

**列出账户中最近的构建 ID**

```aws codebuild list-builds```

**获取构建详情**

```aws codebuild batch-get-builds --ids [build-id]```

**停止正在运行的构建**

```aws codebuild stop-build --id [build-id]```

**查看构建日志**

```aws codebuild batch-get-builds --ids [build-id] --query "builds[0].logs"```

# SYNOPSIS

**aws codebuild** _command_ [_options_]

# PARAMETERS

**start-build**
> 为项目启动一次构建

**start-build-batch**
> 启动批量构建

**stop-build**
> 停止正在运行的构建

**create-project**
> 创建新的构建项目

**update-project**
> 修改项目配置

**delete-project**
> 删除构建项目

**list-projects**
> 列出所有构建项目

**batch-get-builds**
> 获取一个或多个构建的详细信息

**batch-get-projects**
> 获取一个或多个项目的详细信息

**list-builds**
> 列出整个账户的构建 ID，最新的在前

**list-builds-for-project**
> 列出特定项目的构建

**--project-name** _name_
> 构建项目的名称

**--id** _build-id_
> 构建标识符

**--ids** _build-ids_
> 以空格分隔的构建 ID 列表

**--source-version** _ref_
> 源版本（分支、标签、提交 ID）

**--environment-variables-override** _vars_
> 覆盖环境变量（name=KEY,value=VAL）

**--buildspec-override** _path_
> 覆盖 buildspec 文件

**--cli-input-json** _file_
> 从 JSON 文件读取参数

**--generate-cli-skeleton**
> 输出用于创建项目的 JSON 模板

# DESCRIPTION

**aws codebuild** 管理 AWS CodeBuild。这是一项全托管的持续集成服务，可编译源代码、运行测试并生成可部署的制品。

**项目（Project）** 定义构建环境、源码位置（CodeCommit、S3、GitHub、Bitbucket）、构建命令（buildspec.yml）以及输出制品。可使用 **create-project** 配合 JSON 配置文件定义全部设置。

**构建（Build）** 通过 **start-build** 触发，可覆盖源版本、环境变量和 buildspec 的项目默认值。构建在相互隔离的 Docker 容器中运行，计算资源可配置。

构建输出包括日志（存储在 CloudWatch Logs 和/或 S3）和制品（存储在 S3）。可使用 **batch-get-builds** 获取构建状态、日志位置和计时信息。

# CAVEATS

构建超时默认为 60 分钟；长时间构建请合理设置。IAM 服务角色必须拥有访问源码和存储制品的权限。构建缓存有助于加快后续构建速度，但需要进行配置。并发构建数量受账户级上限约束。

# HISTORY

**AWS CodeBuild** 于 **2016 年 12 月** 在 AWS re:Invent 上作为 AWS 开发者工具套件的一部分推出，旨在免除管理 Jenkins 或其他 CI 服务器的负担。支持并行构建的构建批处理于 **2020 年** 加入，提升了复杂构建矩阵的性能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-codepipeline](/man/aws-codepipeline)(1), [aws-codecommit](/man/aws-codecommit)(1), [aws-s3](/man/aws-s3)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/codebuild/index.html)```

<!-- verified: 2026-06-18 -->
