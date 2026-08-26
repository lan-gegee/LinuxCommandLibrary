# TAGLINE

校验最佳实践和常见错误的 Dockerfile linter

# TLDR

**对 Dockerfile 进行 lint**

```hadolint [path/to/Dockerfile]```

**从标准输入 lint**

```cat Dockerfile | hadolint -```

**忽略指定规则**

```hadolint --ignore [DL3008] --ignore [DL3009] [path/to/Dockerfile]```

**以 JSON 输出**

```hadolint --format json [path/to/Dockerfile]```

**只允许来自受信任仓库的镜像**

```hadolint --trusted-registry [docker.io] [path/to/Dockerfile]```

**使用自定义配置文件**

```hadolint --config [path/to/.hadolint.yaml] [path/to/Dockerfile]```

**设置失败阈值的严重级别**

```hadolint --failure-threshold [warning] [path/to/Dockerfile]```

# SYNOPSIS

**hadolint** [_options_] _dockerfile_

# PARAMETERS

_DOCKERFILE_
> 要 lint 的 Dockerfile。

**--ignore** _RULE_
> 忽略指定的规则。

**--format** _FMT_
> 输出格式：tty、json、checkstyle、codeclimate、gitlab_codeclimate、gnu、codacy、sonarqube、sarif（默认为 tty）。

**--trusted-registry** _REG_
> 受信任的容器仓库。来自不受信任仓库的镜像会产生警告。

**--config** _FILE_
> 配置文件路径（默认为 .hadolint.yaml）。

**--failure-threshold** _SEVERITY_
> 只有达到或超过该严重级别的规则才以失败码退出（error、warning、info、style、ignore、none）。

**--no-color**
> 禁用彩色输出。

**--no-fail**
> 不以失败状态码退出。

**-t**, **--strict-labels**
> 检查标签是否符合定义的格式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Hadolint** 是一款 Dockerfile linter，用于校验最佳实践和常见错误。它使用 ShellCheck 校验 RUN 指令中的 shell 命令。

该工具检查安全问题、低效的分层和弃用的语法，帮助创建优化且安全的容器镜像。

# CAVEATS

shell 检查要求 bash 语法。部分规则未必适用于所有场景。建议使用配置文件。

# HISTORY

Hadolint 的诞生旨在结合 Docker 最佳实践与 ShellCheck 的 shell 分析来提升 Dockerfile 质量。

# INSTALL

```dnf: sudo dnf install hadolint```

```brew: brew install hadolint```

```nix: nix profile install nixpkgs#hadolint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [shellcheck](/man/shellcheck)(1)
