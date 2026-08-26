# TAGLINE

检查并强制执行提交信息规范

# TLDR

**检查最近一次提交**

```gitlint```

**检查特定提交**

```gitlint --commit [commit-hash]```

**检查一段提交范围**

```gitlint --commits [HEAD~5..HEAD]```

**检查来自 stdin 的提交信息**

```echo "Fix bug" | gitlint --stdin-msg```

**生成默认配置文件**

```gitlint generate-config```

**安装为 commit-msg git 钩子**

```gitlint install-hook```

**卸载 commit-msg 钩子**

```gitlint uninstall-hook```

使用指定配置文件进行检查

```gitlint --config [.gitlint] --commits [main..HEAD]```

# SYNOPSIS

**gitlint** [_options_] [_command_]

# PARAMETERS

**--commit** _SHA_
> 检查特定提交。

**--commits** _RANGE_
> 检查一段提交范围。

**--stdin-msg**
> 从 stdin 而非 git log 读取提交信息。

**--msg-filename** _FILE_
> 从文件读取提交信息。

**-c** _RULE.OPTION=VALUE_
> 在命令行上设置某条规则的选项。

**-C**, **--config** _FILE_
> 使用指定的配置文件。

**--ignore** _RULES_
> 要忽略规则的逗号分隔列表。

**--contrib** _RULES_
> 要启用的 contrib 规则的逗号分隔列表（如 contrib-title-conventional-commits）。

**--target** _DIRECTORY_
> 目标 git 仓库的路径（默认：当前工作目录）。

**-e**, **--extra-path** _PATH_
> 包含额外用户自定义规则的目录或 Python 模块的路径。

**--ignore-stdin**
> 忽略任何 stdin 数据。适合在 CI 服务器上运行。

**--staged**
> 智能检测暂存提交的元数据。

**--fail-without-commits**
> 当目标提交范围为空时直接失败。

**-v**, **--verbose**
> 详细程度，多次使用可输出更多信息（如 -v、-vv、-vvv）。

**-s**, **--silent**
> 静默模式（无输出）。优先于 -v。

**-d**, **--debug**
> 启用调试输出。

**--version**
> 显示版本并退出。

**--help**
> 显示帮助信息。

# COMMANDS

**lint**
> 检查 git 仓库（默认命令）。

**generate-config**
> 创建默认的 .gitlint 配置文件。

**install-hook**
> 将 gitlint 安装为 git commit-msg 钩子。

**uninstall-hook**
> 移除 gitlint commit-msg 钩子。

**run-hook**
> 运行 gitlint commit-msg 钩子。

# DESCRIPTION

**gitlint** 通过检查提交信息是否遵循关于格式、长度和内容的既定规则来强制执行提交信息规范，确保整个项目的提交历史一致且易读。

默认规则包括：标题最大长度（72 字符）、标题不以句号结尾、正文最大行长（80 字符）、标题与正文之间须有空行等。Contrib 规则还增加了对 Conventional Commits 等格式的支持。

可以编写自定义 Python 规则以强制执行项目特有的约定。通过 **--commits** 检查提交范围，该工具可以自然地集成到 CI 流水线中。

# CONFIGURATION

**.gitlint**
> 项目级配置文件，定义提交信息规则、要忽略的规则及自定义设置。采用 INI 格式，每条规则一个区块。

# CAVEATS

需要 Python 3。作为钩子使用时只检查最近一次提交信息。CI 中需要 **--commits** 标志才能检查分支上的所有提交。自定义规则需要编写 Python 类。

# INSTALL

```dnf: sudo dnf install gitlint```

```apk: sudo apk add gitlint```

```brew: brew install gitlint```

```nix: nix profile install nixpkgs#gitlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-commit](/man/git-commit)(1), [pre-commit](/man/pre-commit)(1)
