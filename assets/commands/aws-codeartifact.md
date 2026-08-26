# TAGLINE

管理私有软件包制品仓库。

# TLDR

**为包管理器登录 CodeArtifact 仓库**（tool：npm、pip、twine、dotnet、nuget、swift）

```aws codeartifact login --tool [npm] --domain [my-domain] --repository [my-repo]```

**获取域的授权令牌**

```aws codeartifact get-authorization-token --domain [my-domain] --query authorizationToken --output text```

**创建用于存储制品的新域**

```aws codeartifact create-domain --domain [my-domain]```

**在域内创建仓库**

```aws codeartifact create-repository --domain [my-domain] --repository [my-repo]```

**列出仓库中的所有软件包**

```aws codeartifact list-packages --domain [my-domain] --repository [my-repo]```

**获取特定格式的仓库端点**

```aws codeartifact get-repository-endpoint --domain [my-domain] --repository [my-repo] --format [npm|pypi|maven|nuget|cargo|ruby|swift|generic]```

# SYNOPSIS

**aws codeartifact** _command_ [_options_]

# DESCRIPTION

**aws codeartifact** 是 AWS CodeArtifact 的 AWS CLI 接口。CodeArtifact 是一项全托管的制品仓库服务，兼容 npm、PyPI、Maven、NuGet、Swift、Ruby、Cargo 及通用软件包格式，让团队既能从 CodeArtifact 也能从公共仓库发布、共享和获取软件包。

CodeArtifact 将软件包组织到 **域（domain）** 下的 **仓库（repository）** 中。域通过单一加密密钥提供集中式资产存储，而仓库之间可通过 **上游（upstream）** 连接串联起来，从外部源获取软件包。

# COMMANDS

**login**
> 为包管理器配置访问仓库所需的凭据

**get-authorization-token**
> 获取用于 API 访问的临时凭据

**create-domain**
> 创建用于组织仓库的新域

**create-repository**
> 在域内创建仓库

**list-repositories**
> 列出整个账户或某个域下的仓库

**list-packages**
> 列出仓库中的软件包

**publish-package-version**
> 向仓库发布通用软件包版本

**describe-package-version**
> 获取特定软件包版本的详细信息

**copy-package-versions**
> 在仓库之间复制软件包版本

**associate-external-connection**
> 将仓库连接到公共注册表（npmjs、PyPI 等）

# CAVEATS

授权令牌默认 12 小时后过期。令牌过期后必须重新运行 **login** 命令。跨账户访问需要显式的域权限策略。上游仓库按特定顺序解析，缓存的软件包可能并非最新的上游版本。

# HISTORY

AWS CodeArtifact 于 **2020 年 6 月** 作为托管制品仓库服务推出，旨在取代 Nexus 或 Artifactory 等自托管方案。后续版本在 **2022-2023 年** 间陆续加入了对 Swift、Ruby 和 Cargo 等更多软件包格式的支持。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [npm](/man/npm)(1), [pip](/man/pip)(1), [maven](/man/maven)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/codeartifact/index.html)```

<!-- verified: 2026-06-18 -->
