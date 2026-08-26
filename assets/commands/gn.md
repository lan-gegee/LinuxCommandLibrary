# TAGLINE

生成 Ninja 文件的元构建系统

# TLDR

**生成** Ninja 构建文件到输出目录

```gn gen [out/Default]```

**内联指定构建参数**来**生成**

```gn gen [out/Default] --args='is_debug=true target_cpu="x64"'```

为输出目录**打开**参数编辑器

```gn args [out/Default]```

**列出**所有可用的构建参数及其默认值

```gn args [out/Default] --list```

**描述**构建目标（deps、sources、configs）

```gn desc [out/Default] [//base:base]```

**列出**构建中已知的全部目标

```gn ls [out/Default]```

不写构建文件而**检查** include 规则

```gn check [out/Default]```

就地**格式化** BUILD.gn 文件

```gn format [path/to/BUILD.gn]```

# SYNOPSIS

**gn** _command_ [_options_]... [_args_]...

# PARAMETERS

**gen** _out_dir_ [**--args=**_string_]
> 为 _out_dir_ 生成 Ninja 构建文件。**--args** 内联设置构建参数；参数会保存到 _out_dir_/args.gn 中。

**args** _out_dir_ [**--list**[=_arg_]] [**--short**] [**--overrides-only**]
> 在 **$EDITOR** 中打开 _out_dir_/args.gn，或列出参数。**--list** 显示默认值和帮助文本；传入参数名可查看单个条目。

**desc** _out_dir_ _target_ [_what_]
> 打印关于 _target_ 的信息。_what_ 可以是 **sources**、**deps**、**configs**、**public**、**defines**、**include_dirs**、**runtime_deps** 等。

**ls** _out_dir_ [_label_pattern_]
> 列出匹配的目标。模式支持通配符，如 **//base/\***。

**refs** _out_dir_ _target_ [**--all**]
> 显示依赖于 _target_ 的目标。

**path** _out_dir_ _target1_ _target2_
> 显示两个目标之间的依赖路径。

**check** _out_dir_ [_label_pattern_]
> 运行 include 规则检查。等同于 **gn gen --check** 但不写构建文件。

**format** [**--dry-run**] [**--stdin**] _file.gn_
> 按规范风格重新格式化 GN 文件。

**clean** _out_dir_
> 删除 _out_dir_ 中除 **args.gn** 外的内容，然后重新运行 **ninja** 来重建。

**help** [_command_]
> 打印一般帮助，或某条命令、某个目标类型或某个内置函数的详细帮助。

**-q**
> 抑制提示性输出。

**--root=**_path_
> 覆盖源码根目录（**.gn** 文件所在处）。

**--dotfile=**_path_
> 使用非默认的 **.gn** dotfile。

**--script-executable=**_path_
> 覆盖 **exec_script** 所使用的 Python 解释器。

**--time**
> 打印构建步骤的耗时信息。

**--tracelog=**_file_
> 将 GN 的执行过程写成 Chrome trace 格式的日志。

# DESCRIPTION

**gn** 是一个元构建系统，被 **Chromium**、**Fuchsia**、**V8**、**Skia**、**ANGLE**、**Dart** 等大型原生项目使用。它读取用一种小型声明式语言编写的 **.gn** dotfile 和 **BUILD.gn** 文件，然后生成用于快速增量构建的 **Ninja** 构建文件。

目标在 **BUILD.gn** 文件中通过 **executable**、**static_library**、**shared_library**、**source_set**、**group** 和 **action** 等规则声明。目标通过 **deps**（私有）和 **public_deps** 引用其他目标，并通过 **configs**、**public_configs**、**defines**、**include_dirs** 和 **sources** 引入编译标志。属性可以用 **+=** 和 **-=** 按目标追加或移除。

构建配置保存在每个输出目录内的 **args.gn** 中，因此可以并行维护多种构建配置（debug、release、交叉编译、插桩），而无需重新检出源码树。交叉编译通过 **target_os** 和 **target_cpu** 参数配置。

# COMMON ARGS

```
is_debug          Debug vs. release build
is_component_build  Build with shared libraries
target_os         "linux", "mac", "win", "android", ...
target_cpu        "x64", "arm64", "x86", "arm", ...
symbol_level      0=none, 1=minimal, 2=full
treat_warnings_as_errors
```

使用 **gn args [out/Default] --list** 可查看项目暴露的所有参数。

# CONFIGURATION

每个项目都在源码根目录有一个 **.gn** dotfile，指向 **BUILDCONFIG.gn** 文件和其他默认值。各构建目录的配置保存在 **<out_dir>/args.gn** 中，可用 **gn args** 编辑。**gn format** 命令为 **BUILD.gn** 文件强制统一规范风格；许多项目将其作为提交前检查运行。

# CAVEATS

**gn** 本身不执行构建——它只生成 Ninja 文件。之后需运行 **ninja -C [out/Default]**。**BUILD.gn** 语言**不是** Python：虽然看起来相似，但它是有意受限的（没有类、不允许递归、执行是确定性的）。支持手动编辑 **args.gn**，但之后必须运行 **gn gen** 重新生成 Ninja 文件。

对于 Chromium 及其衍生项目，**gn** 通过 **depot_tools** 提供；系统级安装的版本可能落后于源码树所需的版本。

# HISTORY

**GN**（"Generate Ninja"）由 **Google** 的 **Brett Wilson** 创建，作为 **Chromium** 构建中 **GYP** 的更快替代品。它于 **2014** 年前后首次出现在 Chromium 代码树中，并在 **2017** 年之前逐步取代了 GYP。GN 现在是托管在 **gn.googlesource.com/gn** 的独立项目，被用作 Chromium、Fuchsia、V8 以及其他多个大型开源代码库的主要构建系统。

# INSTALL

```apt: sudo apt install generate-ninja```

```dnf: sudo dnf install gn```

```pacman: sudo pacman -S gn```

```apk: sudo apk add gn```

```zypper: sudo zypper install gn```

```nix: nix profile install nixpkgs#gn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ninja](/man/ninja)(1), [cmake](/man/cmake)(1), [bazel](/man/bazel)(1), [meson](/man/meson)(1)
