# TAGLINE

Travis CI 命令行界面

# TLDR

登录 Travis CI

```travis login```

启用仓库

```travis enable```

显示构建状态

```travis status```

查看构建日志

```travis logs```

检查 travis.yml

```travis lint```

加密机密值

```travis encrypt [SECRET_VAR=value]```

将加密结果添加到 yaml

```travis encrypt [SECRET=value] --add```

触发构建

```travis restart```

# SYNOPSIS

**travis** [_options_] _command_ [_args_]

# PARAMETERS

**login**
> 使用 GitHub token 向 Travis CI 进行身份认证。

**logout**
> 删除已存储的访问令牌。

**enable**
> 为仓库启用 Travis CI。

**disable**
> 为仓库禁用 Travis CI。

**status**
> 显示当前仓库的构建状态。

**logs**
> 显示构建日志。

**lint**
> 校验 .travis.yml 配置文件。

**encrypt** _DATA_
> 加密字符串以便在 .travis.yml 中使用。

**encrypt-file** _FILE_
> 加密文件以供构建使用。

**restart**
> 重启最近一次构建。

**cancel**
> 取消最近一次构建。

**env** [_list|set|copy_]
> 管理环境变量。

**whoami**
> 显示当前用户。

**sync**
> 触发与 GitHub 的同步。

**token**
> 显示已存储的 API 令牌。

**--add**
> 自动将加密后的值添加到 .travis.yml。

**-r**, **--repo** _SLUG_
> 指定仓库 (owner/name)。

**--com**
> 使用 travis-ci.com API 端点。

**--pro**
> travis-ci.com 的快捷方式（等同于 --com）。

**-t**, **--token** _TOKEN_
> 使用指定的访问令牌。

**--debug**
> 显示 API 请求以便调试。

# DESCRIPTION

**travis** 是 Travis CI（一个持续集成和部署服务）的官方命令行客户端。它在终端中提供对 CI 操作的程序化访问，包括仓库管理、构建监控、机密加密和配置校验等。

认证通过 GitHub OAuth 令牌完成，大多数操作都要求先登录。该 CLI 可以为仓库启用或禁用 CI、查看构建状态和日志、重启构建以及管理加密的环境变量。encrypt 命令会生成针对每个仓库的加密字符串，可以安全地提交到版本控制。

lint 子命令校验 `.travis.yml` 配置文件，在推送之前发现语法错误和配置问题。该 CLI 还支持管理缓存、查看分支状态以及直接与 Travis CI API 交互。

# CAVEATS

需要关联 GitHub 的 Travis CI 账户。travis-ci.org 端点已经关闭；所有用户必须使用 travis-ci.com（传入 **--com** 标志）。认证需要 GitHub OAuth 令牌。

# HISTORY

**Travis CI** 创建于 **2011 年**，是面向 GitHub 的托管 CI 服务。CLI 提供了对 CI 操作的命令行访问能力。

# INSTALL

```apt: sudo apt install travis```

```brew: brew install travis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [circleci](/man/circleci)(1)
