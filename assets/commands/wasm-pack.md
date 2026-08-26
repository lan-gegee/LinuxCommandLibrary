# TAGLINE

为 WebAssembly 构建 Rust 项目

# TLDR

**将 Rust 项目构建为 WebAssembly**

```wasm-pack build```

**为 npm 发布而构建**

```wasm-pack build --target bundler```

**为网页浏览器构建**

```wasm-pack build --target web```

**为 Node.js 构建**

```wasm-pack build --target nodejs```

**使用自定义输出目录构建**

```wasm-pack build --out-dir [dist]```

**以开发模式构建**

```wasm-pack build --dev```

**发布到 npm**

```wasm-pack publish```

**从模板创建新项目**

```wasm-pack new [project-name]```

# SYNOPSIS

**wasm-pack** [_options_] _command_ [_args_]

# COMMANDS

**build**: 编译为 WebAssembly 并生成绑定。

**new**: 从模板创建新项目。

**pack**: 创建用于 npm 发布的 tarball。

**publish**: 将软件包发布到 npm 仓库。

**login**: 登录 npm 仓库。

**test**: 运行 wasm-pack 测试。

# PARAMETERS

**--target** _target_
> 输出目标：bundler（默认）、web、nodejs、deno、no-modules。

**--out-dir** _dir_
> 输出目录（默认：pkg）。

**--out-name** _name_
> 输出文件的基本名。

**--dev**
> 带调试信息的开发构建。

**--profiling**
> 带调试信息的发布构建。

**--release**
> 经过优化的发布构建（默认）。

**--scope** _scope_
> 发布时使用的 npm scope。

**--mode** _mode_
> 构建模式：normal、no-install、force。

**--verbose**
> 启用详细输出。

**--quiet**
> 抑制输出。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**wasm-pack** 是面向 Rust 生成的 WebAssembly 的构建工具。它把 Rust 代码编译成 WebAssembly，用 wasm-bindgen 生成 JavaScript 绑定，并产出可直接用于 npm 的软件包。

构建过程先将 Rust 编译到 wasm32-unknown-unknown 目标，然后运行 wasm-bindgen 生成 JavaScript 胶水代码，并可选择运行 wasm-opt 进行优化。输出包括 .wasm 文件、TypeScript 定义以及供 npm 使用的 package.json。

不同目标会生成不同的 JavaScript 模块格式：bundler 对应 webpack/rollup，web 对应浏览器中的 ES 模块，nodejs 对应 CommonJS，no-modules 对应 script 标签。

通过 cargo 安装：`cargo install wasm-pack`

# CAVEATS

需要带 wasm32-unknown-unknown 目标的 Rust 工具链。首次构建可能会下载 wasm-bindgen 和 wasm-opt。某些 Rust crate 可能无法编译为 WebAssembly。WASI 支持需要不同的工具链。

# HISTORY

**wasm-pack** 由 Rust 与 WebAssembly 工作组创建，旨在简化将 Rust 生成的 WebAssembly 发布到 npm 的流程。它将编译、绑定生成和软件包发布的整个工作流整合到一个工具中。

# INSTALL

```pacman: sudo pacman -S wasm-pack```

```apk: sudo apk add wasm-pack```

```zypper: sudo zypper install wasm-pack```

```brew: brew install wasm-pack```

```nix: nix profile install nixpkgs#wasm-pack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [wasmtime](/man/wasmtime)(1), [npm](/man/npm)(1)
