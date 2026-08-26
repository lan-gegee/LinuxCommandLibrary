# TAGLINE

对 PlatformIO 项目运行静态代码分析

# TLDR

**检查所有已配置的环境**

```pio check```

**只检查特定环境**

```pio check -e [native]```

**选择分析工具**

```pio check --tool [cppcheck]```

**只在达到给定严重级别的缺陷时失败**

```pio check --fail-on-defect [high]```

**向工具传递额外标志**

```pio check --flags "cppcheck: --std=c++17 --platform=unix64"```

**将分析限制在特定路径**

```pio check --src-filters "+<src/app/>"```

**跳过第三方软件包**（框架/工具链）

```pio check --skip-packages```

**输出 JSON 供 CI 使用**

```pio check --json-output```

# SYNOPSIS

**pio check** [_options_]

# PARAMETERS

**-e**, **--environment** _NAME_
> 只对指定的构建环境（在 `platformio.ini` 中定义）运行检查。

**-d**, **--project-dir** _PATH_
> 项目目录。默认为当前目录。

**-c**, **--project-conf** _FILE_
> 替代的 `platformio.ini` 路径。

**--tool** _NAME_
> 分析工具：`cppcheck`、`clangtidy`、`pvs-studio`。可重复指定多个工具。

**--severity** _LEVEL_
> 要报告的最低缺陷严重级别：`low`、`medium`、`high`。

**--fail-on-defect** _LEVEL_
> 如果报告了 _LEVEL_ 及以上级别的缺陷，则返回非零退出码。

**--pattern** _PATTERN_
> 要分析的文件的 glob 模式（`--src-filters` 的替代方案）。

**--src-filters** _FILTER_
> 包含/排除过滤器（如 `+<src/app/>`、`-<src/vendor/>`）。可重复指定。

**--flags** _FLAGS_
> 传给工具的额外标志。加 `<tool>:` 前缀可只针对某个工具（如 `cppcheck: --std=c++17`）。

**--skip-packages**
> 跳过第三方框架和工具链源代码。

**--json-output**
> 以 JSON 格式而不是人类可读文本输出结果。

**-s**, **--silent**
> 除错误外抑制输出。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**pio check** 对 PlatformIO 项目的源代码运行静态分析器，并按严重级别（low、medium、high）分组报告缺陷。未指定 `--tool` 时，它使用 `platformio.ini` 中 `check_tool` 选项配置的工具；未指定 `--environment` 时，它会遍历项目中的每个环境。

该检查会整合项目的构建标志、包含路径和目标平台定义，使分析器看到的宏和头文件与编译器一致——这对嵌入式代码尤为重要，因为不同 MCU 的 `#ifdef` 分支各不相同。

# CONFIGURATION

`pio check` 会读取的 `platformio.ini` 选项：

- `check_tool` — 一个或多个工具（`cppcheck`、`clangtidy`、`pvs-studio`）。
- `check_flags` — 每个工具的额外标志（`cppcheck: --std=c++17`）。
- `check_severity` — 要报告的最低严重级别。
- `check_src_filters` — 要包含/排除的文件/文件夹。
- `check_skip_packages` — 跳过框架/工具链源代码。

# CAVEATS

需要 PlatformIO Core 4.0 以上版本。所选分析器（如 `cppcheck`）必须能通过 PlatformIO 的软件包管理器安装，或已在 PATH 中。PVS-Studio 需要许可证密钥。分析器只能看到预处理器的视野——由未定义的 `#ifdef` 保护的代码会被跳过。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-test](/man/pio-test)(1), [pio-debug](/man/pio-debug)(1), [cppcheck](/man/cppcheck)(1), [clang-tidy](/man/clang-tidy)(1)
