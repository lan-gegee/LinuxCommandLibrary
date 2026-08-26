# TAGLINE

YAML 语法与风格检查工具

# TLDR

**检查一个 YAML 文件**

```yamllint [file.yaml]```

递归**检查目录中的所有 YAML 文件**

```yamllint [path/to/directory]```

**使用指定的配置文件**

```yamllint -c [.yamllint.yaml] [file.yaml]```

**使用预定义配置**（relaxed 或 default）

```yamllint -d relaxed [file.yaml]```

为编辑器**输出可解析格式**

```yamllint -f parsable [file.yaml]```

**严格模式**（出现警告时也返回非零退出码）

```yamllint -s [file.yaml]```

**列出将被检查的文件**

```yamllint --list-files [path]```

# SYNOPSIS

**yamllint** [_options_] [_file_or_dir ..._]

# PARAMETERS

**-c**, **--config-file** _file_
> 使用指定的配置文件。

**-d**, **--config-data** _data_
> 以 YAML 字符串或预设名称（default、relaxed）提供配置。

**-f**, **--format** _format_
> 输出格式：standard、parsable、github、gitlab、colored、auto。

**-s**, **--strict**
> 出现警告时也返回非零退出码（而不仅仅是错误）。

**--no-warnings**
> 抑制输出中的警告消息。

**--list-files**
> 仅列出将要处理的文件，不进行检查。

**-v**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助消息并退出。

# DESCRIPTION

**yamllint** 是一个 YAML 文件检查工具，用于检测语法有效性和风格问题。除基本语法检查外，它还能发现重复键、行长度超限、行尾空格、缩进不一致以及真值歧义等问题。

配置会依次从当前目录或父目录中的 **.yamllint**、**.yamllint.yaml**、**.yamllint.yml**，以及环境变量 **$YAMLLINT_CONFIG_FILE** 或 **$XDG_CONFIG_HOME/yamllint/config**（~/.config/yamllint/config）加载。

该工具提供多种适用于不同场景的输出格式：人类可读、编辑器集成以及 CI 系统（GitHub Actions、GitLab CI）。

# CAVEATS

yamllint 校验 YAML 的语法与风格，但不会对照 schema 进行校验。若需 schema 校验，请使用 **ajv** 等工具或各语言专用的校验器。默认情况下只有错误才导致非零退出码；使用 **-s** 可进入严格模式，此时警告也会导致失败。

# HISTORY

yamllint 由 **Adrien Vergé** 创建，首次发布于 **2016 年**。它的开发初衷是满足对一个能同时检查语法与风格问题的综合性 YAML 检查工具的需求。该项目用 Python 编写，如今已成为 CI/CD 流水线中校验配置文件、Ansible playbook、Kubernetes 清单及其他基于 YAML 的基础设施代码的标准工具。

# INSTALL

```dnf: sudo dnf install yamllint```

```pacman: sudo pacman -S yamllint```

```apk: sudo apk add yamllint```

```brew: brew install yamllint```

```nix: nix profile install nixpkgs#yamllint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yq](/man/yq)(1), [jsonlint](/man/jsonlint)(1), [ansible-lint](/man/ansible-lint)(1)
