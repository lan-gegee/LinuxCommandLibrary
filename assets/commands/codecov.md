# TAGLINE

Codecov 服务的代码覆盖率报告上传器

# TLDR

使用 token **上传覆盖率报告**

```codecovcli upload-process -t [token]```

**上传特定的覆盖率文件**

```codecovcli do-upload -t [token] -f [coverage.xml]```

**带覆盖率标志上传**

```codecovcli do-upload -t [token] -F [unittests]```

**针对特定 commit SHA 上传**

```codecovcli do-upload -t [token] -C [commit_sha]```

**以详细输出模式上传**

```codecovcli -v upload-process -t [token]```

一步完成**创建 commit 并上传**

```codecovcli upload-process -t [token] -r [owner/repo] --git-service [github]```

# SYNOPSIS

**codecovcli** [_global-options_] _command_ [_options_]

# PARAMETERS

**-t** _TOKEN_
> 仓库上传 token。也可通过 CODECOV_TOKEN 环境变量设置。

**-f**, **--file** _FILE_
> 要上传的特定覆盖率报告文件。

**-F**, **--flag** _NAME_
> 用于对覆盖率分组的标志（如 unittests、integration）。可多次指定。

**-C**, **--sha** _SHA_
> 与上传关联的 commit SHA。

**-B**, **--branch** _NAME_
> 上传所属的分支名。

**-r**, **--slug** _OWNER/REPO_
> 仓库标识（owner/repo）。

**-n**, **--name** _NAME_
> 自定义上传名称。

**--git-service** _SERVICE_
> Git 托管服务（github、gitlab、bitbucket、github_enterprise、gitlab_enterprise、bitbucket_server）。

**-v**, **--verbose**
> 启用详细日志。

**-Z**, **--fail-on-error**
> 上传失败时以非零状态退出。

**-s**, **--dir** _DIR_
> 在指定目录中搜索覆盖率文件。

**--enterprise-url** _URL_
> Codecov Self-Hosted 实例的上传主机。

**--disable-search**
> 禁用覆盖率文件的自动发现。

# DESCRIPTION

**codecovcli** 是 Codecov 代码覆盖率服务的命令行接口。它上传由测试框架生成的覆盖率报告，并通过仪表板和 pull request 评论提供洞察。

该 CLI 会自动检测 CI 环境（GitHub Actions、GitLab CI、Jenkins 等）并提取 commit、分支和构建信息。它会搜索常见格式（lcov、cobertura、jacoco 等）的覆盖率文件并上传。

关键命令包括 **upload-process**（一个封装：一步完成创建 commit、创建报告并上传）、**do-upload**（仅上传）、**create-commit**、**create-report** 以及 **send-notifications**。

# CAVEATS

需要 Codecov 账户和仓库 token（公共仓库可无 token 上传）。覆盖率格式必须受支持（lcov、cobertura、clover 等）。私有仓库需要进行认证。较旧的 Bash uploader 脚本已被弃用，由本 CLI 取代。

# HISTORY

Codecov 由 **Steve Peak** 和 **Eli Hooten** 于 **2014 年**创立，旨在为开发团队提供代码覆盖率分析。**2022 年**，Codecov 被 **Sentry** 收购。出于安全性和功能方面的改进，最初的 Bash uploader 已被基于 Python 的 **codecovcli** 取代。

# SEE ALSO

[lcov](/man/lcov)(1), [gcov](/man/gcov)(1)
