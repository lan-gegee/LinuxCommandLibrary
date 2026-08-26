# TAGLINE

带模糊补全的增强版交互式 AWS CLI

# TLDR

**启动** SAWS shell

```saws```

然后在 SAWS 内**运行带补全的 AWS 命令**

```aws [ec2] [describe-instances]```

带存储桶补全地**列出 S3**

```aws s3 ls s3://```

# SYNOPSIS

**saws**

# DESCRIPTION

**saws** 是围绕官方 AWS CLI 的生产力增强层。它会启动一个交互式会话，支持与 **aws** *命令* *子命令* 相同的结构，但增加了对命令、子命令、选项以及实时 AWS 资源（S3 存储桶、EC2 实例 ID/标签等）的模糊自动补全，还提供语法高亮、fish 风格的建议、快捷键、历史记录和上下文帮助。

它要求已安装可用的 AWS CLI 并配置标准的 AWS 凭据 / profile。配置和主题位于 **~/.sawsrc** 及相关文件中。

# PARAMETERS

**saws** 以交互为主。启动后即可输入常规 AWS CLI 命令：

**aws** *service* *operation* [*options*]

> 与 **aws** 相同的使用方式，但带有增强的补全。

快捷键和工具栏选项在上游文档中说明。**F 键** / 工具栏开关用于控制模糊匹配和文档快捷方式等功能（见项目 README）。

# CAVEATS

项目活跃度可能落后于当前 AWS CLI 的功能更新速度——请确认与你安装的 AWS CLI v1/v2 兼容。资源补全需要网络权限来枚举账户资源。它并不是独立的 API 客户端：报错往往源自 **aws** 本身或 IAM 权限。

# SEE ALSO

[aws](/man/aws)(1), [aws-shell](/man/aws-shell)(1)

# RESOURCES

```[Source code](https://github.com/donnemartin/saws)```

```[Documentation](https://saws.readthedocs.org/)```

<!-- verified: 2026-07-19 -->
