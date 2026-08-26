# TAGLINE

部署包构建与发布工具

# TLDR

**发布以供部署**（.NET 8+ 默认 Release）

```dotnet publish```

**发布自包含**应用，面向目标运行时

```dotnet publish -r [linux-x64] --self-contained```

**发布单文件**可执行程序

```dotnet publish -r [linux-x64] -p:PublishSingleFile=true```

**发布到目录**

```dotnet publish -o [./publish]```

**发布裁剪版本**，获得更小的自包含输出

```dotnet publish -r [linux-x64] --self-contained -p:PublishTrimmed=true```

**交叉编译**，分别指定操作系统和体系结构

```dotnet publish --os [linux] --arch [arm64]```

**使用 Properties/PublishProfiles 中的配置文件**发布

```dotnet publish -p:PublishProfile=[FolderProfile]```

# SYNOPSIS

**dotnet publish** [_project_|_solution_|_file_] [_options_]

# PARAMETERS

_PROJECT_ | _SOLUTION_ | _FILE_
> 要发布的对象。默认为当前目录下找到的项目或解决方案。

**-c**, **--configuration** _CONFIG_
> 构建配置。使用 .NET 8 或更新 SDK 构建 `net8.0` 及以上目标时默认为 **Release**，否则为 Debug。

**-r**, **--runtime** _RID_
> 面向给定的运行时标识符（RID）发布，如 `linux-x64` 或 `osx-arm64`。需搭配 **--self-contained** 或 **--no-self-contained** 使用。

**-a**, **--arch** _ARCH_ / **--os** _OS_
> 与当前平台组合成 RID 的简写形式。不要与 **-r** 同时使用。

**--sc**, **--self-contained**
> 将 .NET 运行时随应用一起打包发布，目标机器无需安装任何东西。

**--no-self-contained**
> 发布框架依赖型应用：目标机器上必须已有兼容的 .NET 运行时。

**--ucr**, **--use-current-runtime**
> 以本机自身的运行时为目标。

**-o**, **--output** _DIR_
> 输出目录。默认为 `bin/<configuration>/<framework>/publish/`，自包含输出会附加 RID 后缀。

**-f**, **--framework** _TFM_
> 为多目标项目的某一个目标框架发布。

**-p**, **--property**:_NAME_=_VALUE_
> 设置 MSBuild 属性。`PublishSingleFile`、`PublishTrimmed`、`PublishReadyToRun` 和 `PublishAot` 都是通过这一选项启用的。

**--no-build**
> 不先构建，直接使用现有输出。隐含 **--no-restore**。

**--no-restore**
> 跳过隐式的 `dotnet restore`。

**--no-dependencies**
> 忽略项目到项目的引用，只还原根项目。

**--artifacts-path** _DIR_
> 将所有构建输出集中到一个目录下，按项目分列。

**--manifest** _FILE_
> 依据目标清单裁剪发布的包集合。

**--version-suffix** _SUFFIX_
> 替换项目版本字段中的 `*`。

**--nologo**
> 抑制启动横幅。

**--tl**:[**auto**|**on**|**off**]
> 控制构建输出的终端记录器（Terminal Logger）。

**-v**, **--verbosity** _LEVEL_
> 取值之一：`quiet`、`minimal`（默认）、`normal`、`detailed`、`diagnostic`。

# DESCRIPTION

**dotnet publish** 编译应用程序，并把运行它所需的一切整理到一个目录中。这比 `dotnet build` 的产出更多：除程序集外，它还会写出一份列出全部依赖的 `.deps.json`、一份描述应用所期望运行时的 `.runtimeconfig.json`，以及从 NuGet 缓存复制出来的依赖项本身。这是官方唯一支持的应用部署准备方式。

最核心的选择是**框架依赖**还是**自包含**。框架依赖型输出体积小、跨体系结构可移植，但要求目标机器上有匹配的 .NET 运行时。自包含输出捆绑了运行时，因此到处都能运行，代价是几十兆的体积以及被绑定到单个 RID。

除此之外，若干 MSBuild 属性可以重塑输出形态。`PublishSingleFile` 把一切捆绑进单个可执行文件（这意味着自包含）。`PublishTrimmed` 移除静态分析证明不可达的 IL。`PublishReadyToRun` 提前预编译程序集以降低启动延迟，而 `PublishAot` 则编译为完全没有 IL 和 JIT 的原生二进制。

该命令只是 MSBuild `Publish` 目标的一个薄封装，因此任何 MSBuild 属性或发布配置文件都适用，`-c` 和 `-o` 也只是映射到 `Configuration` 和 `PublishDir` 属性而已。

# CAVEATS

默认配置发生了变化：在 .NET 8 及更新的 SDK 中，`dotnet publish` 对 `net8.0`+ 目标使用 **Release**，而旧版 SDK 默认为 Debug。依赖旧行为的脚本，或者想当然地传入 `-c Debug` 以为它是默认值的脚本，都需要重新审视。

裁剪和 AOT 是最容易踩坑的地方。两者都依赖静态分析，只通过反射或动态加载触达的代码可能被移除或编译失败，而且问题往往在运行时才显现，发布时毫无征兆。请测试裁剪后的产物，重视裁剪警告而不是一味压制。

对*解决方案*使用 `-o` 在较新的 SDK 中属于错误用法，因为所有项目的输出会在同一目录里相互冲突；应改用 `PublishDir` 属性。发布到项目目录之下的文件夹会让后续多次运行的输出层层嵌套在自己内部。另外 `--no-build` 会静默隐含 `--no-restore`，所以过期的 `bin` 目录会被不加提醒地直接发布出去。

# HISTORY

**dotnet publish** 随首个 .NET Core SDK 于 **2016 年**问世，取代了 .NET Framework 应用曾经需要的各平台专属打包方式。它的能力随每次发布不断扩展：先是自包含部署，随后 .NET Core 3 引入单文件捆绑和 ReadyToRun，.NET 6 让裁剪真正可用，.NET 7 起又加入 Native AOT——这一切让一个曾被视作笨重的运行时，也能产出小巧、无依赖的原生可执行文件。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet-run](/man/dotnet-run)(1), [dotnet-restore](/man/dotnet-restore)(1), [msbuild](/man/msbuild)(1)

# RESOURCES

```[Source code](https://github.com/dotnet/sdk)```

```[Documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish)```

<!-- verified: 2026-07-14 -->
