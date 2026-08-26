# TAGLINE

Ruby 静态代码分析器和格式化工具

# TLDR

**检查当前目录**

```rubocop```

**检查特定文件**

```rubocop [file.rb] [other.rb]```

**自动安全地修复问题**

```rubocop -a```

**自动修复所有问题**

```rubocop -A```

**检查特定 cops**

```rubocop --only [Layout/LineLength,Style/StringLiterals]```

**生成配置文件**

```rubocop --init```

**生成待办列表**

```rubocop --auto-gen-config```

**显示违规详情**

```rubocop --extra-details```

# SYNOPSIS

**rubocop** [_-a_] [_-A_] [_--only cops_] [_-c config_] [_options_] [_files_]

# PARAMETERS

**-a**, **--auto-correct**
> 自动安全地修复问题。

**-A**, **--auto-correct-all**
> 自动修复所有问题。

**--only** _COPS_
> 仅运行指定的 cops。

**--except** _COPS_
> 排除指定的 cops。

**-c** _FILE_
> 配置文件。

**--auto-gen-config**
> 生成待办配置。

**--init**
> 创建 .rubocop.yml。

**-f** _FORMAT_
> 输出格式。

**--display-cop-names**
> 显示 cop 名称。

**--extra-details**
> 显示额外详情。

**-L**, **--list-target-files**
> 列出要检查的文件。

**--parallel**
> 并行运行。

**--safe-auto-correct**
> 仅进行安全的修正。

# DESCRIPTION

**rubocop** 是一个 Ruby 静态代码分析器和格式化工具。它强制执行《Ruby 风格指南》（Ruby Style Guide）中的风格规范。

cop 是检查特定风格违规的单条规则。类别包括 Layout、Style、Lint、Metrics 和 Naming。

自动修正会修改文件以修复违规。安全模式（-a）只应用不改变行为的修正；完整模式（-A）包含所有修正。

通过 .rubocop.yml 可以自定义规则。cop 可以被启用、禁用或以不同参数进行配置。

auto-gen-config 命令会创建一个待办文件，忽略当前存在的违规。这使得现有项目可以渐进式地采用该工具。

与编辑器集成可以实时显示问题；与 CI 集成可以在拉取请求上强制执行风格规范。

# CONFIGURATION

**.rubocop.yml**
> 项目级配置文件，定义启用的 cops、自定义参数、排除的文件以及风格偏好。

**~/.rubocop.yml**
> 用户级默认配置，在找不到项目配置时应用。

**.rubocop_todo.yml**
> 自动生成的文件，列出当前需要忽略的违规，由 --auto-gen-config 创建，用于渐进式采用。

# CAVEATS

风格是主观的——许多团队会进行大量自定义。自动修正可能出错。检查大型代码库需要一定时间。

# HISTORY

**RuboCop** 由 **Bozhidar Batsov** 于 **2012 年**前后创建。它已成为事实上的标准 Ruby linter，紧密遵循同样由 Batsov 撰写的社区版 Ruby 风格指南。

# INSTALL

```pacman: sudo pacman -S rubocop```

```nix: nix profile install nixpkgs#rubocop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [bundle](/man/bundle)(1), [standardrb](/man/standardrb)(1), [reek](/man/reek)(1)
