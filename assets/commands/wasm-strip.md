# TAGLINE

从 WebAssembly 文件中剥离自定义节区

# TLDR

**剥离所有自定义节区**

```wasm-strip [file.wasm]```

**剥离并写入另一个文件**

```wasm-strip -o [output.wasm] [input.wasm]```

# SYNOPSIS

**wasm-strip** [_options_] _file_

# PARAMETERS

**-o**, **--output** _file_
> 输出到指定文件，而不是原地修改。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**wasm-strip** 从 WebAssembly 二进制文件中移除自定义节区，以减小文件体积。它是 WABT（WebAssembly Binary Toolkit）的一部分。

自定义节区包含执行所不需要的可选元数据，例如调试信息、名称和 source map。剥离这些节区可以得到体积更小、适合生产部署的模块。

该工具默认原地修改文件。使用 -o 可以保留原文件，并将剥离后的输出写入新文件。

# CAVEATS

剥离会移除调试信息，使调试更困难。只影响自定义节区；标准节区保持不变。没有备份则不可逆。属于 WABT 软件包的一部分。

# HISTORY

**wasm-strip** 是 WABT（WebAssembly Binary Toolkit）的一部分，由 WebAssembly 社区组开发。与原生二进制的传统 strip 命令类似，它通过移除非必要的元数据来缩减二进制体积以便分发。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm-objdump](/man/wasm-objdump)(1), [wasm-validate](/man/wasm-validate)(1), [wasm2wat](/man/wasm2wat)(1), [strip](/man/strip)(1)
