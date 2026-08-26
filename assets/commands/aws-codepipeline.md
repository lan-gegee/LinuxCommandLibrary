# TAGLINE

管理 AWS 上的持续交付流水线。

# TLDR

**启动流水线执行**

```aws codepipeline start-pipeline-execution --name [MyPipeline]```

**带变量启动**

```aws codepipeline start-pipeline-execution --name [MyPipeline] --variables name=VERSION,value=1.0.0```

**获取流水线定义**

```aws codepipeline get-pipeline --name [MyPipeline]```

**获取流水线执行详情**

```aws codepipeline get-pipeline-execution --pipeline-name [MyPipeline] --pipeline-execution-id [execution-id]```

**获取流水线当前状态**

```aws codepipeline get-pipeline-state --name [MyPipeline]```

**列出所有流水线**

```aws codepipeline list-pipelines```

**列出流水线执行记录**

```aws codepipeline list-pipeline-executions --pipeline-name [MyPipeline]```

**从 JSON 创建流水线**

```aws codepipeline create-pipeline --cli-input-json file://[pipeline.json]```

# SYNOPSIS

**aws codepipeline** _command_ [_options_]

# PARAMETERS

**start-pipeline-execution**
> 手动触发一次流水线运行

**get-pipeline**
> 获取流水线定义和元数据

**get-pipeline-state**
> 获取所有阶段的当前状态

**get-pipeline-execution**
> 获取特定执行的详细信息

**list-pipelines**
> 列出账户中的所有流水线

**list-pipeline-executions**
> 列出流水线的执行记录

**create-pipeline**
> 创建新流水线

**update-pipeline**
> 修改流水线定义

**delete-pipeline**
> 删除流水线

**enable-stage-transition**
> 允许进入某阶段的转换

**disable-stage-transition**
> 阻止进入某阶段的转换

**--name** _pipeline-name_
> 流水线名称

**--pipeline-name** _name_
> 流水线名称（替代参数）

**--pipeline-execution-id** _id_
> 执行标识符

**--variables** _vars_
> 流水线变量（name=KEY,value=VAL）

**--source-revisions** _revisions_
> 为本次执行覆盖源版本

**--stage-name** _name_
> 阶段名称

**--transition-type** _type_
> Inbound 或 Outbound 转换类型

# DESCRIPTION

**aws codepipeline** 管理 AWS CodePipeline。这是一项持续交付服务，可为应用程序更新自动执行发布流水线。

流水线由 **阶段（stage）** 组成（Source、Build、Test、Deploy），每个阶段包含执行具体工作的 **操作（action）**，例如拉取代码、运行构建或将应用部署到环境。阶段按顺序执行，阶段之间存在转换控制。

**start-pipeline-execution** 使用最新源版本或指定的覆盖值触发新一轮运行。流水线也可以由源码变更、计划任务或 webhook 自动触发。

**流水线模式** 控制执行行为：SUPERSEDED（默认）在新执行开始时取消较旧的执行；QUEUED 按顺序依次处理执行；PARALLEL 允许并发执行。

可使用 **disable-stage-transition** 设置人工审批关卡，或在维护期间暂停部署。

# CAVEATS

流水线存在并发执行数量限制。禁用转换会阻断所有后续阶段，而不仅仅是下一个阶段。流水线变量必须先在流水线中定义才能使用。执行历史保留 12 个月。

# HISTORY

**AWS CodePipeline** 于 **2015 年 7 月** 作为 AWS 的持续交付服务推出。具备流水线变量和触发器等增强功能的 V2 流水线于 **2023 年** 推出。该服务与 CodeCommit、CodeBuild、CodeDeploy 以及 GitHub、Jenkins 等第三方工具集成。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-codebuild](/man/aws-codebuild)(1), [aws-codecommit](/man/aws-codecommit)(1)
