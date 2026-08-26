# TAGLINE

Node.js 提交信息校验器

# TLDR

**校验指定的提交**

```core-validate-commit [commit_sha]```

**校验最近的提交（HEAD）**

```core-validate-commit```

**校验一段提交范围**

```core-validate-commit [main..HEAD]```

**列出所应用的校验规则**

```core-validate-commit --list```

# SYNOPSIS

**core-validate-commit** [_options_] [_commit_]

# DESCRIPTION

**core-validate-commit** 是为 Node.js 项目开发的专用工具，用于强制执行提交信息规范。它校验提交信息是否符合项目特定的格式要求，包括正确的子系统前缀、语法规则和元数据格式。

Node.js 项目采用结构化的提交信息格式：每条提交必须以子系统标识符（如 "doc:"、"test:"、"src:"）开头，后接简明描述。该工具解析提交信息并按这些规则进行校验，检查诸如缺少子系统、大小写不规范、句尾多出句号、行长度不正确等问题。

该工具主要用于自动化 CI/CD 流水线，确保所有进入 Node.js 仓库的提交都遵循项目规范。这种一致性让生成更新日志、按子系统追踪变更以及维护项目历史变得更加容易。虽然它专为 Node.js 核心开发而设计，但也展示了对大型项目而言自动校验提交信息的价值。

# SEE ALSO

[git](/man/git)(1)
