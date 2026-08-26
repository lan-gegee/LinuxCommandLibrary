# TAGLINE

构建项目并将构件安装到本地 Maven 仓库

# TLDR

**安装到本地仓库**

```mvn install```

**跳过测试安装**

```mvn install -DskipTests```

**清理并安装**（先移除 target/）

```mvn clean install```

**以指定 profile 安装**

```mvn install -P [profile]```

以**离线模式安装**（不访问网络）

```mvn install -o```

**带调试输出安装**

```mvn install -X```

使用多线程**并行构建安装**

```mvn install -T [4]```

# SYNOPSIS

**mvn install** [_options_]

# PARAMETERS

**-DskipTests**
> 跳过测试执行，但仍编译测试代码。

**-Dmaven.test.skip=true**
> 完全跳过测试的编译和执行。

**-P** _profile_
> 激活 pom.xml 中定义的构建 profile。

**-pl** _modules_
> 只构建指定模块（逗号分隔）。

**-am**
> 同时构建所需的上游模块（与 -pl 一起使用）。

**-o**
> 离线工作，只使用本地缓存的依赖。

**-U**
> 强制从远程仓库更新 SNAPSHOT 依赖。

**-T** _threads_
> 并行构建模块的线程数（例如 4 或表示每个 CPU 核心一个线程的 1C）。

**-X**
> 启用调试输出以便排查问题。

**-e**
> 出错时显示完整堆栈跟踪。

**-q**
> 安静输出，只显示错误。

**-f** _file_
> 使用替代的 POM 文件。

# DESCRIPTION

**mvn install** 是 Maven 构建生命周期的一个阶段，它构建项目并将生成的构件（JAR、WAR 等）安装到 ~/.m2/repository 的本地 Maven 仓库。这使该构件可以作为其他本地项目的依赖使用。

运行 `mvn install` 会按顺序执行所有前置生命周期阶段：validate、compile、test、package、verify，最后是 install。每个阶段运行其绑定的插件 goals。

本地仓库既是本地构建产物的缓存，也是从远程仓库下载的依赖的缓存。在开发期间，其他本地项目要依赖某个构件，前提是先将该构件安装到本地。

# CAVEATS

install 阶段默认运行所有测试；可使用 -DskipTests 跳过。本地仓库（~/.m2/repository）会随时间不断变大。除非使用 -U，否则 SNAPSHOT 版本不会自动更新。多模块项目默认会安装所有模块。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-package](/man/mvn-package)(1), [mvn-deploy](/man/mvn-deploy)(1), [gradle](/man/gradle)(1)
