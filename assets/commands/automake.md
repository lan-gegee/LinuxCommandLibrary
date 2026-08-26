# TAGLINE

从 Makefile.am 生成 Makefile.in 模板

# TLDR

**生成** Makefile.in

```automake --add-missing```

以**复制**方式而非符号链接生成

```automake --add-missing --copy```

针对**特定版本**生成

```automake-1.16```

# SYNOPSIS

**automake** [_--add-missing_] [_--copy_] [_options_] [_Makefile_...]

# DESCRIPTION

**automake** 从 Makefile.am 文件生成 Makefile.in 模板。它与 autoconf 配合构建完整的 GNU 构建系统，处理编译、安装和分发任务。

Automake 提供可在各类类 Unix 系统上工作的可移植 makefile。

# PARAMETERS

**-a**, **--add-missing**
> 补充缺失的标准辅助文件（install-sh、missing 等）。

**-c**, **--copy**
> 复制辅助文件而不是创建符号链接。

**--force-missing**
> 即使标准辅助文件已存在也进行替换。

**-W** _category_, **--warnings=**_category_
> 报告给定类别的警告（如 all、none、error、portability）。

**--gnu**
> 要求符合 GNU 编码规范（默认行为）。

**--foreign**
> 放宽检查；允许缺少 GNU 规范要求的文件。

**--gnits**
> 应用更严格的 GNU Gnits 规范。

**-i**, **--ignore-deps**
> 禁用自动依赖跟踪的生成。

# WORKFLOW

1. 编写 Makefile.am
2. 运行 **automake** 生成 Makefile.in
3. 运行 **autoconf** 生成 configure
4. 用户运行 ./configure 生成 Makefile

# CAVEATS

学习曲线陡峭。生成的 Makefile 很复杂。需要理解 autotools 的各种约定。许多项目现在改用 CMake 或 Meson。

# HISTORY

**Automake** 由 David MacKenzie 和 Tom Tromey 创建，于 **1994 年**首次发布，为 autoconf 补充了 makefile 生成能力。

# INSTALL

```dnf: sudo dnf install automake```

```pacman: sudo pacman -S automake```

```apk: sudo apk add automake```

```zypper: sudo zypper install automake```

```brew: brew install automake```

```nix: nix profile install nixpkgs#automake```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[autoconf](/man/autoconf)(1), [autoreconf](/man/autoreconf)(1), [make](/man/make)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/automake/)```

```[Documentation](https://www.gnu.org/software/automake/manual/automake.html)```

<!-- verified: 2026-06-17 -->
