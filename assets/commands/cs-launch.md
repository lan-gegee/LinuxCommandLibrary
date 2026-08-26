# TAGLINE

从 Maven 坐标运行 JVM 应用

# TLDR

按 Maven 坐标**启动应用**

```cs launch [org.scalameta::metals:latest.stable]```

**启动时传递参数**给应用

```cs launch [com.lihaoyi::ammonite:2.5.9] -- [--help]```

以指定的主类**启动**

```cs launch [org.example::app:1.0] -M [com.example.Main]```

从自定义仓库**启动**

```cs launch -r [https://repo.example.com/maven] [org.example::app:1.0]```

附加 JVM 选项**启动**

```cs launch [app:version] --java-opt [-Xmx2G]```

**启动并转入后台**

```cs launch --fork [app:version]```

# SYNOPSIS

**cs launch** [_options_] _coordinates_ [-- _app-args_]

# PARAMETERS

_COORDINATES_
> Maven 坐标（Scala 用 groupId::artifactId:version，Java 用 groupId:artifactId:version）。

**-M** _CLASS_, **--main-class** _CLASS_
> 指定要运行的主类。

**-r** _URL_, **--repository** _URL_
> 添加自定义 Maven 仓库。

**--java-opt** _OPT_
> 传递给被启动应用的 JVM 选项。

**--fork**
> 分叉进程并立即返回。

**--standalone**
> 将所有依赖包含进 classpath。

**--**
> cs 选项与应用参数之间的分隔符。

**-q**, **--quiet**
> 抑制 coursier 的输出。

# DESCRIPTION

**cs launch** 直接根据 Maven 坐标运行 JVM 应用，无需事先安装。它可以在一条命令内完成依赖解析、构件下载和应用执行。

这样就能在不安装的情况下试用应用、运行特定版本进行测试，或通过脚本执行应用。依赖会被缓存，因此再次启动同一版本时速度很快。

该命令同时支持 Scala（用 :: 表示跨版本）和 Java 构件。任何在其 manifest 中定义了主类或显式指定主类的构件都可以被启动。

# CAVEATS

首次启动需要下载依赖，耗时较长。获取新构件需要网络连接。依赖众多的应用会占用大量缓存空间。有些应用可能需要特定的 JVM 版本。

# HISTORY

cs launch 是 Coursier 的一部分，由 Alexandre Archambault 创建。launch 功能将 npx 等工具推广的"免安装即运行"工作流带到了 JVM 生态。

# INSTALL

```apt: sudo apt install csound```

```pacman: sudo pacman -S csound```

```zypper: sudo zypper install csound```

```brew: brew install csound```

```nix: nix profile install nixpkgs#csound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cs](/man/cs)(1), [cs-resolve](/man/cs-resolve)(1), [java](/man/java)(1), [scala](/man/scala)(1)

# RESOURCES

```[Source code](https://github.com/coursier/coursier)```

```[Documentation](https://get-coursier.io/docs/cli-launch)```

<!-- verified: 2026-06-26 -->
