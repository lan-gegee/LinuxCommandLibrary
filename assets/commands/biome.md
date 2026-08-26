# TAGLINE

面向 JavaScript、TypeScript 和 CSS 的快速代码格式化与 lint 工具

# TLDR

**在项目中初始化 Biome**

```biome init```

**检查代码错误**（lint 与格式化）

```biome check [path/to/directory]```

**格式化代码**

```biome format --write [path/to/directory]```

**Lint 代码并显示问题**

```biome lint [path/to/directory]```

**修复可自动修复的 lint 问题**

```biome lint --write [path/to/directory]```

**检查单个文件**

```biome check [path/to/file.js]```

**以 JSON 格式输出**

```biome check --reporter=json [path/to/directory]```

**CI 模式**（存在任何问题即失败）

```biome ci [path/to/directory]```

# SYNOPSIS

**biome** _command_ [_options_] [_paths_]

# PARAMETERS

**init**
> 创建 biome.json 配置文件。

**check**
> 运行 linter 和 formatter 检查。

**format**
> 格式化源文件。

**lint**
> 对源文件进行 lint。

**ci**
> 面向 CI 环境的检查（更严格的模式）。

**migrate eslint** | **migrate prettier**
> 读取现有的 ESLint 或 Prettier 配置，并将其设置移植到 biome.json。加 **--write** 以应用。

**--write**
> 对文件应用安全修复和格式化（旧称 **--apply**）。

**--fix**
> **--write** 的别名；应用安全修复。

**--unsafe**
> 同时应用被标记为 unsafe 的修复（配合 **--write** 使用）。

**--only** _rule_
> 只运行给定的 lint 规则或规则组。

**--skip** _rule_
> 跳过给定的 lint 规则或规则组。

**--error-on-warnings**
> 出现警告时以错误码退出。

**--reporter** _format_
> 输出格式：summary、json、github、gitlab。

**--config-path** _path_
> 配置文件的路径。

**--vcs-enabled** _bool_
> 使用版本控制忽略文件（.gitignore）。

**--no-errors-on-unmatched**
> 没有文件匹配时不报错。

**--diagnostic-level** _level_
> 最低严重级别：info、warn、error。

# DESCRIPTION

**Biome** 是一款面向 JavaScript、TypeScript、JSX、JSON、CSS、GraphQL 以及（较新版本中的）HTML 的快速代码格式化器、linter 等多功能工具。它被设计为统一的工具链，用单一、更快的替代品取代 ESLint、Prettier 等工具。

Biome 以 Rust 编写，性能出众——通常比基于 JavaScript 的同类工具快 10 到 100 倍。它只需极少配置，开箱即用地提供合理默认值，同时可通过 **biome.json** 高度定制。

该工具将格式化和 lint 整合到单次处理中，降低开销。编辑器集成可提供实时反馈，CLI 则为 CI 系统支持多种输出格式。

# CONFIGURATION

**biome.json**
> 项目级配置文件，控制 formatter 设置、linter 规则、文件包含/排除模式以及各语言专属选项。由 `biome init` 创建。

# CAVEATS

Biome 可能不支持所有 ESLint 规则或 Prettier 选项，一些配置特殊的项目在迁移期间需要调整。Biome 2.0（2025 年）加入了插件系统和类型感知 lint，但插件生态仍远小于 ESLint。CSS、GraphQL 和 HTML 支持晚于成熟的 JS/TS 支持。

# HISTORY

Biome 源自 **Rome Tools**，该项目由 **Sebastian McKenzie**（Babel 的创造者）于 **2020 年**发起。当 Rome Tools Inc. 于 **2023 年**停止运营后，社区将该分支项目延续为 Biome，并采用新的治理模式。这个分叉迅速获得关注，既保持了注重性能的 Rust 实现，又在社区管理下加速了开发。2025 年发布的 Biome 2.0 引入了插件系统和类型感知 lint。

# INSTALL

```pacman: sudo pacman -S biome```

```zypper: sudo zypper install biome```

```brew: brew install biome```

```nix: nix profile install nixpkgs#biome```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [prettier](/man/prettier)(1), [deno](/man/deno)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/biomejs/biome)```

```[Homepage](https://biomejs.dev/)```

```[Documentation](https://biomejs.dev/guides/getting-started/)```

<!-- verified: 2026-06-19 -->
