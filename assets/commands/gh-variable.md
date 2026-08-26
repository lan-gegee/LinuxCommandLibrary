# TAGLINE

管理 GitHub Actions 配置变量

# TLDR

**列出变量**

```gh variable list```

**设置变量**

```gh variable set [name] -b "[value]"```

**从文件设置**

```gh variable set [name] < [file]```

**删除变量**

```gh variable delete [name]```

**获取变量值**

```gh variable get [name]```

**设置组织级变量**

```gh variable set [name] -o [org] -b "[value]"```

**设置环境级变量**

```gh variable set [name] -e [environment] -b "[value]"```

**以 JSON 列出变量**

```gh variable list --json name,value```

# SYNOPSIS

**gh** **variable** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出变量。

**set**
> 设置变量。

**delete**
> 删除变量。

**get**
> 获取单个变量。

# PARAMETERS

**-b**, **--body** _value_
> 变量值。

**-R**, **--repo** _owner/repo_
> 选择仓库。

**-o**, **--org** _name_
> 为组织设置或列出变量。

**-e**, **--env** _name_
> 为部署环境设置或列出变量。

**-v**, **--visibility** _scope_
> 设置组织级变量的可见性：all、private 或 selected。

**--json** _fields_
> 输出包含指定字段的 JSON。

**-q**, **--jq** _expression_
> 使用 jq 表达式过滤 JSON 输出。

# DESCRIPTION

**gh variable** 管理 GitHub Actions 配置变量，用于存储非敏感的工作流数据。与 secret 不同，变量不经加密且其值可以被读取，因此适合存放配置项、功能开关和环境名称等。

变量的作用范围可以是仓库、组织或特定的部署环境。在工作流中可以通过 **vars** 上下文访问它们（例如 `vars.VARIABLE_NAME`）。变量非常适合用于 API 端点、构建配置以及其他非机密参数。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-secret](/man/gh-secret)(1)
