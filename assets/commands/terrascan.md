# TAGLINE

面向 IaC 的静态安全扫描器

# TLDR

**初始化 Terrascan**（下载策略）

```terrascan init```

**扫描当前目录**

```terrascan scan```

**扫描指定目录**

```terrascan scan -d [/path/to/terraform]```

**以指定 IaC 类型扫描**

```terrascan scan -i [terraform]```

**扫描 Kubernetes 清单**

```terrascan scan -i k8s -d [/path/to/manifests]```

**以 JSON 输出结果**

```terrascan scan -o json```

**跳过特定规则**

```terrascan scan --skip-rules "[AC_AWS_001,AC_AWS_002]"```

**扫描远程仓库**

```terrascan scan -r git -u [https://github.com/user/repo]```

# SYNOPSIS

**terrascan** [_command_] [_options_]

# COMMANDS

**init**: 初始化 Terrascan 并下载策略。

**scan**: 扫描 IaC 中的安全违规。

**server**: 以 API 服务器运行。

**version**: 显示版本信息。

**help**: 显示命令帮助。

# PARAMETERS

**-c**, **--config-path** _file_
> 配置文件路径。

**-d**, **--iac-dir** _path_
> 要扫描的目录。

**-f**, **--iac-file** _file_
> 要扫描的特定文件。

**-i**, **--iac-type** _type_
> IaC 类型：terraform、k8s、helm、kustomize。

**-t**, **--policy-type** _type_
> 策略类型：all、aws、azure、gcp、k8s。

**-o**, **--output** _format_
> 输出格式：human、json、yaml、xml、junit-xml、sarif。

**-r**, **--remote-type** _type_
> 远程类型：git。

**-u**, **--remote-url** _url_
> 远程仓库 URL。

**--skip-rules** _rules_
> 以逗号分隔的要跳过的规则。

**--severity** _level_
> 最低严重级别：low、medium、high。

**--find-vuln**
> 检查容器漏洞。

**-l**, **--log-level** _level_
> 日志级别：debug、info、warn、error。

**-x**, **--log-type** _type_
> 日志类型：console、json。

# DESCRIPTION

**Terrascan** 是一款基础设施即代码（IaC）静态代码分析器。它扫描 Terraform、Kubernetes、Helm 和 Kustomize 配置中的安全错误配置与合规违规。

该工具内置 500 多条策略，覆盖 AWS、Azure、GCP 和 Kubernetes 最佳实践。它可以集成到 CI/CD 流水线中，防止不安全的配置被部署。

Terrascan 可以作为 CLI 工具、API 服务器或 Kubernetes 准入控制器运行。自定义策略可使用 Rego（Open Policy Agent 的策略语言）编写。

策略存储在 ~/.terrascan 中，并在首次运行或执行 `terrascan init` 时自动下载。

# CAVEATS

需要 Go 环境或预编译的二进制文件。更新策略需运行 init。某些策略可能产生误报，需要排除相应规则。扫描大型代码库可能消耗大量资源。

# HISTORY

**Terrascan** 最初由 Accurics 开发，现由 Tenable 维护。它为云原生基础设施提供部署前安全扫描，帮助组织践行"安全即代码"。

# INSTALL

```brew: brew install terrascan```

```nix: nix profile install nixpkgs#terrascan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tfsec](/man/tfsec)(1), [checkov](/man/checkov)(1)
