# TAGLINE

纯 Rust 实现的 Git CLI

# TLDR

**克隆仓库**

```gix clone [https://github.com/user/repo]```

从远程**获取更新**

```gix fetch```

显示仓库状态

```gix status```

列出远程仓库

```gix remote list```

显示提交日志

```gix log```

对文件执行 blame

```gix blame [path/to/file]```

校验仓库完整性

```gix verify```

列出可用子命令

```gix --help```

# SYNOPSIS

**gix** [_options_] _command_ [_args_...]

**ein** [_options_] _command_ [_args_...]

# COMMANDS

**clone** _url_ [_path_]
> 将仓库克隆到新目录。

**fetch** [_remote_]
> 从远程获取数据并存入仓库。

**status**
> 计算并显示仓库状态。

**commit** _subcommand_
> 与提交对象交互。

**branch** _subcommand_
> 与分支交互。

**tag** _subcommand_
> 与标签对象交互。

**remote** _subcommand_
> 与远程主机交互。

**log** [_path_]
> 列出仓库中的提交，可限定为更改某路径的提交。

**diff**
> 打印两个对象之间的所有差异。

**blame** _path_
> 对文件中的行执行 blame。

**worktree** _subcommand_
> 处理工作树。

**submodule** _subcommand_
> 与子模块交互。

**index** _subcommand_
> 与 `.git/index` 等工作树索引交互。

**mailmap**
> 与 mailmap 交互。

**commit-graph** _subcommand_
> 与 commit-graph 文件交互。

**verify**
> 校验整个仓库的完整性。

**credential**
> 一个与 `git credential` 类似的程序。

**free** _subcommand_
> 无需 Git 仓库即可运行的子命令（例如 pack 和 index 操作）。

**completions**
> 将 shell 补全脚本生成到 stdout 或目录中。

以上仅为子集；运行 **gix --help** 查看完整且自带说明的子命令列表（现已涵盖 archive、clean、fsck、odb、attributes、exclude、dirwalk、merge 等）。

# PARAMETERS

**-r**, **--repository** _path_
> 使用指定路径的仓库。

**-t**, **--threads** _num_
> 要使用的线程数。

**--progress**
> 显示进度信息。

**--verbose**
> 启用详细输出。

**-h**, **--help**
> 显示命令或子命令的帮助。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**gix**（gitoxide）提供两个 CLI 可执行文件：**gix** 面向底层 plumbing 操作，**ein** 面向高层 porcelain 命令。它完全用 Rust 编写，目标是成为正确、高性能且安全的 Git 实现。

**gix** 可执行文件暴露底层、自带文档的 plumbing 命令，并作为 gitoxide API 的测试与验证工具。**ein** 是面向 porcelain 的较小对应物，提供少量便利命令（如 **init**、**clone** 以及 **tools** 下的仓库发现工具），面向日常使用而非 API 验证。

两个可执行文件都访问同一个底层 **gix** 库生态，该生态以纯 Rust 实现了 Git 协议、对象存储、引用处理等功能。

# CAVEATS

这些 CLI 可执行文件尚不稳定，不应在脚本中依赖它们。与 Git 相比功能覆盖不完整；某些操作可能未实现。项目正在积极开发中，API 可能变动。

# HISTORY

Gitoxide 由 **Sebastian Thiel** 发起，是一项用 Rust 重写 Git 的工程。开发初期优先关注正确性，其次才是性能。项目已发展为包含全面 Git 功能的体系，由多个 crate（gix-*）提供模块化组件。

# SEE ALSO

[git](/man/git)(1), [lazygit](/man/lazygit)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/GitoxideLabs/gitoxide)```

```[Crate status](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md)```

<!-- verified: 2026-07-17 -->
