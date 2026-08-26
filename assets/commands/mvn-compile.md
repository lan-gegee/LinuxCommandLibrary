# TAGLINE

编译 Maven 项目的主源代码

# TLDR

**编译**项目

```mvn compile```

编译期间**激活某个 profile**

```mvn compile -P [profile_name]```

**编译但不**在后续生命周期阶段运行测试

```mvn compile -DskipTests```

以**离线模式**编译（不联网）

```mvn compile -o```

**强制更新**依赖

```mvn compile -U```

使用指定的 JDK **工具链运行**

```mvn compile -Dmaven.compiler.release=[17]```

**安静地编译**

```mvn compile -q```

在多模块构建中**编译指定模块**

```mvn -pl [module/path] -am compile```

# SYNOPSIS

**mvn compile** [_options_]

# PARAMETERS

**-P** _profile_
> 激活一个或多个以逗号分隔的 Maven profile。

**-DskipTests**
> 跳过后续阶段中的测试编译。若不带此选项运行 **mvn test**，测试仍会被编译。

**-Dmaven.compiler.release** _N_
> 设置传递给 javac 的 **--release** 标志，控制目标 JDK API 级别。

**-o**, **--offline**
> 以离线模式运行；绝不访问远程仓库。

**-U**, **--update-snapshots**
> 强制更新 SNAPSHOT 依赖和插件。

**-pl** _MODULES_
> 将 reactor 构建限制为以逗号分隔的模块列表。

**-am**, **--also-make**
> 与 **-pl** 一起使用时，同时构建所选模块的依赖模块。

**-q**, **--quiet**
> 只输出错误和最终结果。

**-X**, **--debug**
> 启用详细调试输出（完整堆栈跟踪、有效 POM）。

**-T** _N_
> 使用 _N_ 个线程并行构建（或用 **1C** 表示每个核心一个线程）。

# DESCRIPTION

**mvn compile** 运行 Maven 默认生命周期的 **compile** 阶段，会先执行它之前的所有阶段（validate、initialize、generate-sources、process-resources 等），最后调用 **maven-compiler-plugin** 将 **src/main/java** 编译到 **target/classes**。来自 **src/main/resources** 的资源会在 **process-resources** 阶段被复制，因此在 **compile** 完成后它们已位于类路径上。

编译器版本和目标语言级别由 **pom.xml** 中 **maven-compiler-plugin** 的配置，或由 **maven.compiler.source**、**maven.compiler.target** 和 **maven.compiler.release** 属性决定。多模块并行构建可使用 **-T**，而 **-pl/-am** 可只编译大型 reactor 中的相关模块。

# CAVEATS

**src/test/java** 中的测试源码在单独的阶段（**test-compile**）编译，仅靠 **mvn compile** 不会生成它们。注解处理器生成的源码写入 **target/generated-sources/annotations**，必须位于源码路径上才能被 IDE 识别。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-package](/man/mvn-package)(1), [mvn-install](/man/mvn-install)(1), [javac](/man/javac)(1)
