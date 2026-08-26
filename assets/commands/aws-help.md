# TAGLINE

显示 AWS CLI 命令文档

# TLDR

**查看**常规帮助

```aws help```

**服务**帮助

```aws s3 help```

**命令**帮助

```aws s3 cp help```

**子命令**帮助

```aws ec2 describe-instances help```

**列出**可用帮助主题

```aws help topics```

# SYNOPSIS

**aws** [_service_] [_command_] **help**

# DESCRIPTION

**aws help** 显示 AWS CLI 命令的完整文档，通过分页器界面展示语法、参数、示例和相关命令。

帮助覆盖每个层级：CLI 总体帮助、特定服务的帮助以及单个命令的帮助。

# FEATURES

文档内容包括：
- 命令语法和结构
- 参数说明与类型
- 用法示例
- 可用子命令
- 输出格式细节
- 相关命令

# NAVIGATION

在帮助分页器中：
- **Space** - 向下翻页
- **b** - 向上翻页
- **/** - 搜索
- **q** - 退出

# WORKFLOW

```bash
# General help
aws help

# S3 service help
aws s3 help

# Specific command help
aws s3 cp help

# EC2 describe-instances help
aws ec2 describe-instances help
```

# CAVEATS

默认在分页器中打开（可用 --no-cli-pager 禁用）。某些情况下需要联网才能获取完整文档。复杂命令的帮助文本可能非常长。

# HISTORY

**help** 命令自 **2013 年** AWS CLI 首次发布以来就是其中的一部分，为所有服务和命令提供内联文档。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [man](/man/man)(1), [less](/man/less)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/)```

<!-- verified: 2026-06-18 -->
