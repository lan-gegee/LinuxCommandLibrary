# TAGLINE

Gradle 版本锁定 wrapper 生成器

# TLDR

**生成 wrapper**

```gradle wrapper```

**指定 Gradle 版本**

```gradle wrapper --gradle-version [9.4.0]```

**使用分发类型（bin 或 all）**

```gradle wrapper --distribution-type [all]```

**用现有 wrapper 升级 wrapper 版本**

```./gradlew wrapper --gradle-version [9.4.0]```

**指定带 SHA-256 校验的分发包**

```gradle wrapper --gradle-version [9.4.0] --gradle-distribution-sha256-sum [checksum]```

**用 wrapper 运行项目构建**

```./gradlew build```

# SYNOPSIS

**gradle wrapper** [_options_]

# PARAMETERS

**--gradle-version** _VERSION_
> 要使用的 Gradle 版本。

**--distribution-type** _TYPE_
> bin 或 all（包含源码）。

**--gradle-distribution-url** _URL_
> 自定义分发包 URL。

**--gradle-distribution-sha256-sum** _HASH_
> 用于校验分发包的 SHA-256 校验和。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gradle wrapper** 生成 Gradle Wrapper，使项目能够使用特定的 Gradle 版本而无需全局安装。用户运行 **./gradlew** 而不是 **gradle**，wrapper 会自动下载并使用指定的版本。

通过在版本控制中固定确切的 Gradle 版本，可以保证不同机器和 CI 系统上构建的一致性。

# CONFIGURATION

**gradle/wrapper/gradle-wrapper.properties**
> 为 wrapper 指定 Gradle 分发包的 URL、版本和校验和。

# CAVEATS

Wrapper 文件应提交到版本库。首次运行会下载 Gradle。请使用 https 分发 URL。

# HISTORY

Gradle Wrapper 的引入是为了解决版本一致性问题，现已成为运行 Gradle 构建的推荐方式。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1)
