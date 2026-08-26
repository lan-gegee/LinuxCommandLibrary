# TAGLINE

将代码仓库序列化以供 LLM 使用

# TLDR

**序列化当前目录**以供 LLM 使用

```yek```

**序列化特定目录**

```yek [src/] [tests/]```

**按 token 数上限序列化**

```yek --tokens [128k]```

**按字节大小上限序列化**

```yek --max-size [10MB]```

将输出**管道传输**到剪贴板

```yek | pbcopy```

在输出中**包含行号**

```yek --line-numbers```

**包含目录树**头信息

```yek --tree-header```

**以 JSON 格式输出**

```yek --json```

**使用 glob 模式**

```yek "[src/**/*.ts]"```

# SYNOPSIS

**yek** [_options_] [_input-paths_...]

# PARAMETERS

**--tokens** _count_
> 使用 token 计数模式代替字节模式（例如 128k、100）

**--max-size** _size_
> 按字节大小限制输出（例如 10MB、128K）；默认：10MB

**--json**
> 以 JSON 格式输出结果

**--output-dir** _path_
> 输出文件所在目录；未指定时使用临时目录

**--output-name** _name_
> 写入当前目录的文件名

**--output-template** _template_
> 使用 FILE_PATH 和 FILE_CONTENT 占位符的自定义格式

**--ignore-patterns** _patterns_
> 额外要忽略的模式（在 .gitignore 基础上扩展）

**--unignore-patterns** _patterns_
> 覆盖内置的忽略规则

**--line-numbers**
> 在输出中包含行号

**-t**, **--tree-header**
> 在输出开头包含目录树

**--tree-only**
> 仅显示目录结构，不显示文件内容

**--no-config**
> 跳过加载配置文件

**--config-file** _path_
> 使用指定的配置文件

**--debug**
> 启用调试日志

# DESCRIPTION

**yek**（波斯语意为"一"）是一款基于 Rust 的快速 CLI 工具，可将代码仓库序列化为针对 LLM（大语言模型）优化的文本。它将多个文件合并为单一输出，并进行智能排序和自动过滤。

该工具遵循 **.gitignore** 规则，利用 Git 历史来提高重要文件的优先级，并自动跳过二进制文件和大文件。输出可以按 token 数或字节大小分块。

当输出被管道传输时，yek 会自动改为流式输出内容而不是写文件。这样可以实现 **yek | pbcopy** 之类的工作流，快速将代码库复制到剪贴板以便粘贴到 LLM 对话中。

配置可以存储在 **yek.toml** 或 **yek.yaml** 文件中以进行项目级设置。

# CAVEATS

token 计数是近似值，可能与实际的 LLM 分词有所不同。非常大的仓库可能需要用 **--tokens** 或 **--max-size** 进行分块。glob 模式必须加引号以防止 shell 展开。

# HISTORY

**yek** 由 **Mohsen Azimi** 创建，是一款为 LLM 分析准备代码的高性能工具。它用 **Rust** 编写，相比同类工具有显著的性能提升——基准测试显示其运行速度比 Repomix 等替代品快 230 倍。名字在波斯语（یک）中意为"一"，反映了它将多个文件合并为一个输出的用途。

# INSTALL

```brew: brew install yek```

```nix: nix profile install nixpkgs#yek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [find](/man/find)(1), [cat](/man/cat)(1), [rg](/man/rg)(1)
