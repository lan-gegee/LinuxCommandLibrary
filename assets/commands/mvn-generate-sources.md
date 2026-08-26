# TAGLINE

运行源代码生成插件

# TLDR

**生成源码**

```mvn generate-sources```

**以指定 profile 生成**

```mvn generate-sources -P [profile]```

**离线生成**

```mvn generate-sources -o```

# SYNOPSIS

**mvn generate-sources** [_options_]

# PARAMETERS

**-P** _profile_[,_profile_...]
> 激活 **pom.xml** 或 **settings.xml** 中定义的一个或多个构建 profile。

**-o**, **--offline**
> 离线工作（不访问远程仓库）。

**-U**, **--update-snapshots**
> 强制检查 SNAPSHOT 依赖和插件版本是否有更新。

**-X**, **--debug**
> 启用调试级别的 Maven 输出。

**-pl** _modules_, **--projects** _modules_
> 将构建限制为列出的 reactor 模块（逗号分隔）。

**-am**, **--also-make**
> 同时构建 **-pl** 所选模块依赖的项目。

**-T** _N_[**C**], **--threads** _N_[**C**]
> 使用 _N_ 个线程，可选按 CPU 核心数指定（如 **-T 1C**）。

**-D**_property_=_value_
> 向构建传递一个系统属性。

# DESCRIPTION

**mvn generate-sources** 调用 Maven 的 **generate-sources** 生命周期阶段，它会（连同之前所有阶段——**validate**、**initialize**）运行绑定到该阶段的全部插件执行。代码生成器就属于这里：JAXB / XJC、gRPC / Protocol Buffers、Avro、Antlr、OpenAPI、Modello、JOOQ 等。生成的源码通常位于 **target/generated-sources/**_plugin_/ 下，并在下一阶段 **process-sources** → **compile** 运行时自动加入编译源码根目录。

由于 Maven 会先执行所有前置阶段，单独使用 **mvn generate-sources** 往往意义不大——大多数用户会直接运行 **mvn compile** 或 **mvn package**，让代码生成作为副作用发生。当你想让生成的代码可供 IDE 刷新使用而又不想编译整个项目时，可以显式使用该阶段。

# CAVEATS

**mvn clean** 会清除已生成的源码。插件必须在 **pom.xml** 中绑定到 **generate-sources** 或由某个 profile 激活，否则不会发生任何事。多个插件生成到同一目录时可能冲突。

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-compile](/man/mvn-compile)(1), [mvn-package](/man/mvn-package)(1), [mvn-dependency](/man/mvn-dependency)(1)
