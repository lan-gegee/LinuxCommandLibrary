# TAGLINE

面向 AI 编程代理的 ContextCodeCache 生成器

# TLDR

**扫描项目**并生成 `.ccc/` 缓存

```ccc scan```

**扫描并生成 token 流**

```ccc scan . --tokens```

**检查已提交的缓存是否最新**（CI）

```ccc check .```

**将二进制安装到 PATH**（Linux）

```ccc install```

# SYNOPSIS

**ccc** scan [_PATH_] [--tokens]

**ccc** check [_PATH_] [--format json]

**ccc** tokenize [_PATH_]

**ccc** install [--dir DIR] [--force]

# DESCRIPTION

ccc 扫描源代码树，生成一个紧凑的、机器可读的 `.ccc/` 目录，其中包含每个文件的摘要：常量、函数（带类型和文档摘要）、文件内的调用图边，以及标记注释（TODO、FIXME 等）。

该缓存设计为提交到仓库并由 AI 代理消费，让它们拥有一个廉价且始终最新的结构化索引，而不必反复 grep 或重新读取源码。

支持的语言：Rust、Python、JavaScript、TypeScript（+ TSX）和 Go（通过 tree-sitter）。不支持的文件会被跳过；隐藏目录、常见的构建/第三方目录以及 `.gitignore` 规则均被遵守。

# INSTALL

需要 Rust ≥ 1.77 和较新的 cargo：

```bash
cargo build --release
./target/release/ccc install
```

`ccc install` 子命令将二进制复制到 `~/.local/bin`（或用 `--dir` 指定的目录）。使用 `--force` 可覆盖已有安装。

# PARAMETERS

**scan** [_PATH_]
> 为给定路径重新生成 `.ccc` 目录（默认为当前目录）。

**--tokens**
> 同时输出预编码的 token 流（`tokens.bin` + `tokens.json`），供能直接消费原始 token ID 的模型使用。

**check** [_PATH_]
> 如果磁盘上的缓存相对当前源码已过期，则以非零值退出。适用于 CI。

**--format json**
> 输出机器可读的变更文件列表（`{ root, up_to_date, files[], changes[] }`）。

**tokenize** [_PATH_]
> 将已有的 `.ccc` 预编码为 `tokens.bin` + `tokens.json`，无需完整重新扫描。

**install** [--dir DIR] [--force]
> 将正在运行的二进制复制到你的 PATH 上（Linux）。默认目录：`~/.local/bin`。

# CAVEATS

token 流使用近似的 tiktoken ID（OpenAI 词表，例如 `o200k_base`），**与 Anthropic 模型不兼容**。配合 Claude 请使用缓存的 Markdown 形式。

每当影响索引的源码文件发生变化时，请重新生成缓存。CI 中执行 `ccc check .` 会在缓存过期时使构建失败。

# RESOURCES

```[Source code](https://github.com/colwill/ccc)```

<!-- verified: 2026-07-11 -->
