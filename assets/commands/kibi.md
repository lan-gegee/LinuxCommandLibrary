# TAGLINE

用不到 1024 行 Rust 编写的文本编辑器

# TLDR

**打开文件**

```kibi [path/to/file]```

**创建新文件**

```kibi```

# SYNOPSIS

**kibi** [_file_]

# DESCRIPTION

**kibi** 是一个可配置的文本编辑器，支持 UTF-8、增量搜索、语法高亮和行号显示，用不到 1024 行的 Rust 编写，依赖极少。它支持为 **38 种以上语言**配置语法高亮。

kibi 的灵感来自 **kilo**（由 Salvatore Sanfilippo 创建），目标是成为一个体量极小但功能完备的编辑器，通过 Rust 保证内存安全，同时保持代码库极其精简。

# KEY BINDINGS

**Ctrl+S** — 保存
**Ctrl+Q** — 退出
**Ctrl+F** — 查找（增量搜索）
**Ctrl+G** — 跳转到行
**Ctrl+D** — 复制行

# CAVEATS

功能集有意保持精简 —— 没有插件系统或高级编辑功能。1024 行的限制意味着完整编辑器中的某些功能并不存在。

# HISTORY

**kibi** 由 **Ilaï Deutel**（ilai-deutel）创建，以 **Rust** 编写。它兼容 Linux、macOS、Windows 10 和 WASI。"kibi" 一词意为 1024（如 kibibyte 中所示），暗指其行数限制。

# INSTALL

```apk: sudo apk add kibi```

```brew: brew install kibi```

```nix: nix profile install nixpkgs#kibi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [micro](/man/micro)(1), [vim](/man/vim)(1)
