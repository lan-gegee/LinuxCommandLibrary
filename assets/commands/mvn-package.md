# TAGLINE

构建项目并生成可分发的软件包

# TLDR

**构建软件包**

```mvn package```

**跳过测试构建**

```mvn package -DskipTests```

**以指定 profile 构建**

```mvn package -P [production]```

**清理后构建**

```mvn clean package```

# SYNOPSIS

**mvn package** [_options_]

# PARAMETERS

**-DskipTests**
> 跳过测试执行。

**-Dmaven.test.skip**
> 跳过测试的编译和执行。

**-P** _profile_
> 激活 profile。

**-o**
> 离线工作。

**-T** _threads_
> 并行构建。

# DESCRIPTION

**mvn package** 构建项目并生成可分发的软件包（JAR、WAR 等）。它会执行 compile、test 和 package 阶段。输出位于 target/ 目录。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-install](/man/mvn-install)(1), [mvn-compile](/man/mvn-compile)(1)
