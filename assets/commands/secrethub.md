# TAGLINE

加密机密管理服务 CLI

# TLDR

**写入机密**

```secrethub write [org/repo/secret]```

**读取机密**

```secrethub read [org/repo/secret]```

**列出机密**

```secrethub ls [org/repo]```

**带机密运行命令**

```secrethub run -- [command]```

**初始化仓库**

```secrethub repo init [org/repo]```

**将机密注入文件**

```secrethub inject -i [template.env] -o [.env]```

# SYNOPSIS

**secrethub** _command_ [_options_] [_args_]

# PARAMETERS

**write** _path_
> 在给定路径存储机密（从 stdin 或提示符读取值）。

**read** _path_
> 检索并打印机密值。

**ls** _path_
> 列出某个路径下的机密、目录或仓库。

**run** **--** _command_
> 执行命令，并将机密作为环境变量注入。

**inject** **-i** _template_ **-o** _output_
> 渲染模板，将机密引用替换为实际值。

**repo init** _path_
> 初始化新仓库。

**generate** _path_
> 在给定路径生成并存储随机机密。

**--clip**
> 将机密复制到剪贴板而不是打印（配合 **read** 使用）。

**--env-file** _file_
> 从文件加载环境变量引用（配合 **run** 使用）。

# DESCRIPTION

**secrethub** 曾是一款机密管理服务 CLI，提供端到端加密和零知识架构的安全凭据存储。机密以基于路径的层次结构（org/repo/secret）组织在仓库中，并在传输前于客户端加密。

**run** 命令将机密注入子进程的环境变量，避免凭据出现在配置文件和 shell 历史中。通过 **inject** 进行的模板注入会根据引用替换生成包含机密的配置文件，支持安全的部署工作流。

内置的访问控制允许团队以细粒度权限共享机密。该服务已被 1Password 收购并停止运营；用户应迁移到 1Password、HashiCorp Vault 等类似工具。

# CAVEATS

服务已停运。请改用其他替代方案。需要账户。

# HISTORY

**SecretHub** 是一家总部位于荷兰的机密管理服务商。它于 2021 年 4 月被 **1Password 收购**，随后**停止运营**，服务于 **2022 年 1 月 1 日**终止。其功能被整合进 1Password Secrets Automation 和 1Password CLI（**op**）。现有用户获得了针对 Python、Go、JavaScript、Terraform 和 Kubernetes operator 的迁移指南。

# SEE ALSO

[op](/man/op)(1), [vault](/man/vault)(1), [pass](/man/pass)(1)
