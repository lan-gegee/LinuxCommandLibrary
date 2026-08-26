# TAGLINE

交互式 AWS CloudFormation 部署工具

# TLDR

**列出当前区域的所有 CloudFormation 堆栈**

```rain ls```

**部署 CloudFormation 模板**

```rain deploy [template.yaml] [stack-name]```

**从运行中的堆栈获取模板**

```rain cat [stack-name]```

**显示堆栈的事件日志**

```rain logs [stack-name]```

**格式化 CloudFormation 模板**

```rain fmt [template.yaml]```

**比较两个模板**

```rain diff [template1.yaml] [template2.yaml]```

**删除 CloudFormation 堆栈**

```rain rm [stack-name]```

**在部署前预测部署失败**

```rain forecast [template.yaml] [stack-name]```

# SYNOPSIS

**rain** _command_ [_options_] [_arguments_]

# PARAMETERS

**ls**
> 列出当前区域的 CloudFormation 堆栈或变更集

**deploy** _template_ _stack-name_
> 从本地模板部署 CloudFormation 堆栈

**cat** _stack-name_
> 获取并显示运行中堆栈的模板

**logs** _stack-name_
> 显示指定堆栈的事件日志

**rm** _stack-name_
> 删除 CloudFormation 堆栈

**fmt** _template_
> 将 CloudFormation 模板格式化为统一风格

**diff** _template1_ _template2_
> 比较两个 CloudFormation 模板

**build** _resource-type_
> 为指定的资源类型创建 CloudFormation 模板

**forecast** _template_ _stack-name_
> 预测潜在的部署失败

**pkg** _template_
> 打包本地构件以供部署（替代 aws cloudformation package）

**bootstrap**
> 创建用于部署的 S3 构件存储桶

**--region**, **-r** _region_
> 指定 AWS 区域

**--profile**, **-p** _profile_
> 使用指定的 AWS 配置文件

**--experimental**, **-x**
> 启用实验性命令

**--help**, **-h**
> 显示帮助信息

# DESCRIPTION

**rain** 是一个面向 AWS CloudFormation 的开发工作流工具，简化了模板编写、验证和堆栈管理。相比标准 AWS CLI，它为 CloudFormation 操作提供了更友好的界面。

相对于 AWS CLI 的主要改进包括：带彩色输出的实时部署进度、自动模板格式化、模板比较以及部署失败预测。Rain 能在部署前检测潜在问题，节省时间并减少堆栈操作失败。

该工具支持 CloudFormation 模块，可以打包 Lambda 代码等本地构件用于部署。它会自动处理 S3 存储桶管理的复杂细节。

# CAVEATS

需要通过环境变量、AWS CLI 配置文件或 IAM 角色配置 AWS 凭据。请确保 AWS 账号具有相应的 CloudFormation 及相关服务权限。

**forecast** 等部分命令是实验性的，需要 **-x** 标志。实验性功能可能在版本间发生变化。

Rain 一次只操作一个区域。使用 **--region** 可指定与默认不同的区域。

# HISTORY

Rain 由 **AWS CloudFormation 团队**开发，作为开源工具发布，旨在改善 CloudFormation 的开发体验。其名字取自"当你有很多 CloudFormation 时会发生什么（rain，雨）"的双关。它用 Go 编写，并在 GitHub 上持续维护。

# INSTALL

```brew: brew install rain```

```nix: nix profile install nixpkgs#rain```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [terraform](/man/terraform)(1), [sam](/man/sam)(1), [cdk](/man/cdk)(1)
