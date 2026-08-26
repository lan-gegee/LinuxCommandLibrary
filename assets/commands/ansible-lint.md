# TAGLINE

检查 playbook 是否符合最佳实践

# TLDR

对 playbook 进行 **lint 检查**

```ansible-lint [playbook.yml]```

对目录中的**所有文件**进行 lint 检查

```ansible-lint```

使用**指定 profile** 进行 lint 检查

```ansible-lint --profile [production] [playbook.yml]```

**列出**所有规则

```ansible-lint -L```

**跳过**指定规则

```ansible-lint --skip-list [yaml,risky-shell-pipe] [playbook.yml]```

以 **JSON** 格式输出

```ansible-lint -f json [playbook.yml]```

# SYNOPSIS

**ansible-lint** [_--profile profile_] [_-x skip_] [_-f format_] [_files_]

# DESCRIPTION

**ansible-lint** 检查 Ansible playbook、role 和 collection 中可能需要改进的实践和行为。它会识别已弃用的语法、安全隐患、风格问题以及违反最佳实践之处。

该工具有助于保持 Ansible 代码的一致性和高质量，并在部署前发现常见错误。

# PARAMETERS

**-L**, **--list-rules**
> 列出所有可用规则

**-T**, **--list-tags**
> 列出所有标签及其涵盖的规则

**-x** _rules_, **--skip-list** _rules_
> 跳过指定的规则或标签

**-w** _rules_, **--warn-list** _rules_
> 将列出的规则或标签仅视为警告

**--profile** _profile_
> 选择规则 profile：min、basic、moderate、safety、shared 或 production

**-f** _format_, **--format** _format_
> 输出格式：brief、full、md、json（codeclimate 的别名）、codeclimate、quiet、pep8、sarif

**--fix** [_rules_]
> 自动修复违规项，可选地限定于特定规则或标签

**-q**, **--quiet**
> 更安静的输出（可重复使用两次）

**--strict**
> 出现警告时返回非零退出码

**--offline**
> 禁用安装 requirements 和依赖项

**-c** _file_, **--config-file** _file_
> 使用指定的配置文件

# CONFIGURATION

**.ansible-lint**
> 项目级配置文件，用于规则选择、跳过列表和 profile。

**~/.config/ansible-lint/config.yml**
> 用户级默认配置。

# CAVEATS

并非所有规则都适用于所有场景；请合理配置 skip-list。--fix 选项未必能处理所有问题。复杂的变量用法可能导致误报。

# HISTORY

**ansible-lint** 的创建目的是在 Ansible 项目中推行最佳实践。它已成为官方的 Ansible 项目，并随规则集的不断演进而持续维护。

# INSTALL

```pacman: sudo pacman -S ansible-lint```

```apk: sudo apk add ansible-lint```

```zypper: sudo zypper install ansible-lint```

```brew: brew install ansible-lint```

```nix: nix profile install nixpkgs#ansible-lint```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible](/man/ansible)(1), [ansible-playbook](/man/ansible-playbook)(1), [yamllint](/man/yamllint)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible-lint)```

```[Documentation](https://docs.ansible.com/projects/lint/)```

<!-- verified: 2026-06-11 -->
