# TAGLINE

小巧快速的构建系统

# TLDR

**构建项目**

```ninja```

**构建指定目标**

```ninja [target]```

**以多个并行任务构建**

```ninja -j [8]```

**在其他目录中构建**

```ninja -C [build_dir]```

**清理构建产物**

```ninja -t clean```

**试运行**

```ninja -n```

**详细输出**

```ninja -v```

**出错后继续构建**

```ninja -k [0]```

**使用指定的构建文件**

```ninja -f [build.ninja]```

**显示构建图**

```ninja -t graph [target]```

# SYNOPSIS

**ninja** [_options_] [_targets_]

# PARAMETERS

_TARGETS_
> 构建目标。

**-j** _N_
> 并行运行 N 个任务（0 表示无限制）[默认=CPU 数量]。

**-f** _FILE_
> 指定输入的构建文件 [默认=build.ninja]。

**-C** _DIR_
> 在做其他任何事情之前先切换到 DIR 目录。

**-v**
> 构建过程中显示所有命令行。

**-n**
> 试运行（不真正执行命令，但表现得像它们已成功）。

**-k** _N_
> 持续构建直到 N 个任务失败为止（0 表示无限制）[默认=1]。

**-l** _N_
> 当系统负载均值大于 N 时不再启动新任务。

**-t** _TOOL_
> 运行子工具（用 -t list 可列出子工具）。

**-d** _MODE_
> 启用调试模式（用 -d list 可列出调试模式）。

**-w** _FLAG_
> 调整警告设置（用 -w list 可列出警告项）。

**--version**
> 打印 ninja 版本号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ninja** 是一个小巧快速的构建系统，设计理念与 Make 最为接近。它专注速度和正确性，采用了不同的思路：输入文件由更高层次的构建系统生成，而非手工编写。

构建文件（build.ninja）通常由 CMake、Meson 或 GN 生成。Ninja 的设计目标是取代 Make，成为 Chromium 这类大型项目的构建执行器。

# CAVEATS

构建文件通常不由人手写，而是由元构建系统生成。与 Make 相比，Ninja 特性刻意保持精简。默认并行度取决于可用 CPU 的数量。

# HISTORY

Ninja 由 Google 的 **Evan Martin** 为构建 Chrome 而创造，于 2012 年发布。

# INSTALL

```apt: sudo apt install ninja-build```

```dnf: sudo dnf install ninja-build```

```pacman: sudo pacman -S samurai```

```apk: sudo apk add samurai```

```zypper: sudo zypper install samurai```

```brew: brew install samurai```

```nix: nix profile install nixpkgs#samurai```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [meson](/man/meson)(1), [make](/man/make)(1)
