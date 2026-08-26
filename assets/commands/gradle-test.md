# TAGLINE

Gradle 单元测试运行器

# TLDR

**运行所有测试**

```gradle test```

**通过 wrapper 运行**

```./gradlew test```

**运行特定的测试类**

```gradle test --tests [SomeTestClass]```

**运行特定的测试方法**

```gradle test --tests [SomeTestClass.testMethod]```

**运行匹配模式的测试**

```gradle test --tests '*Test'```

**强制重新运行所有测试**

```gradle cleanTest test```

**运行测试并在失败后继续**

```gradle test --continue```

**不执行的试运行**

```gradle test --test-dry-run```

# SYNOPSIS

**gradle** **test** [**--tests** _pattern_] [_options_]

# PARAMETERS

**--tests** _pattern_
> 运行匹配模式的测试（类、方法或通配符）。

**--continue**
> 在测试失败后继续。

**--test-dry-run**
> 模拟执行而不实际运行测试。

**--info**
> 显示更多测试输出。

**--rerun-tasks**
> 即使是最新的也强制重新运行。

**-x** _task_
> 排除某个任务。

# DESCRIPTION

**gradle test** 运行 Gradle 项目的单元测试套件。它会编译测试源码、运行测试并生成报告。使用 **--tests** 可以按类名、方法名或通配符模式运行特定测试。多个 **--tests** 选项可以组合使用。默认情况下，Gradle 会跳过之前已通过的测试，除非源码发生了变化。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-build](/man/gradle-build)(1)

# RESOURCES

```[Documentation](https://docs.gradle.org/current/userguide/java_testing.html)```

<!-- verified: 2026-07-17 -->
