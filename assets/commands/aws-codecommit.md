# TAGLINE

管理 AWS CodeCommit 上托管的 Git 仓库。

# TLDR

**创建新仓库**

```aws codecommit create-repository --repository-name [my-repo] --repository-description "[Description]"```

**列出账户中的所有仓库**

```aws codecommit list-repositories```

**获取仓库详情**

```aws codecommit get-repository --repository-name [my-repo]```

**使用 git-remote-codecommit 克隆仓库**（通过 pip install git-remote-codecommit 安装）

```git clone codecommit::[region]://[my-repo]```

**从现有提交创建分支**

```aws codecommit create-branch --repository-name [my-repo] --branch-name [feature-branch] --commit-id [abc123]```

**创建拉取请求**

```aws codecommit create-pull-request --title "[PR Title]" --targets repositoryName=[my-repo],sourceReference=[feature-branch],destinationReference=main```

**直接向仓库写入文件**

```aws codecommit put-file --repository-name [my-repo] --branch-name main --file-content file://[local-file.txt] --file-path [path/in/repo.txt] --commit-message "[message]"```

# SYNOPSIS

**aws codecommit** _command_ [_options_]

# DESCRIPTION

**aws codecommit** 是 AWS CodeCommit 的 AWS CLI 接口。CodeCommit 是一项全托管的源代码控制服务，托管安全的 Git 仓库。它免去了自行运维源代码控制系统的负担，并能自动扩展以满足项目需求。

CodeCommit 支持分支、提交、合并等标准 Git 功能，还提供 AWS 特有的能力，例如拉取请求审批规则、用于事件通知的仓库触发器，以及与 AWS IAM 集成实现访问控制。

# COMMANDS

**create-repository**
> 创建新的 CodeCommit 仓库

**delete-repository**
> 删除仓库

**list-repositories**
> 列出账户中的所有仓库

**get-repository**
> 获取仓库元数据，包括其克隆 URL

**create-branch**
> 创建新分支

**create-pull-request**
> 在分支之间创建拉取请求

**merge-pull-request-by-fast-forward**
> 以 fast-forward 方式合并拉取请求

**put-file**
> 在仓库中添加或更新文件

**get-file**
> 以 base64 形式获取文件内容

**create-commit**
> 创建包含多个文件更改的提交

**create-approval-rule-template**
> 定义拉取请求的审批要求

# CAVEATS

自 **2024 年** 年中起，AWS CodeCommit 不再向新客户开放；现有客户可继续使用。CodeCommit 默认使用 AWS IAM 进行身份验证，而非 SSH 密钥或密码。如需 HTTPS 访问，需配置 Git 凭据助手或 git-remote-codecommit。单个文件上限为 2 GB，且每秒 API 请求数有配额限制。

# HISTORY

AWS CodeCommit 于 **2015 年 7 月** 作为 AWS 开发者工具套件的一部分推出，提供兼容 Git 的托管仓库，可作为 GitHub Enterprise 或自托管 GitLab 的替代方案。拉取请求支持于 **2017 年** 加入，面向合规工作流的审批模板于 **2019 年** 加入。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [git](/man/git)(1), [aws-codebuild](/man/aws-codebuild)(1), [aws-codepipeline](/man/aws-codepipeline)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/codecommit/index.html)```

<!-- verified: 2026-06-18 -->
