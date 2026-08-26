# TAGLINE

Gradle 子项目层次结构查看工具

# TLDR

**列出所有子项目**

```gradle projects```

**通过 wrapper 列出**

```./gradlew projects```

**列出特定项目的子项目**

```gradle :[subproject]:projects```

# SYNOPSIS

**gradle** **projects**

# DESCRIPTION

**gradle projects** 显示多项目 Gradle 构建中所有子项目的分层列表。输出展示根项目及其所有子项目的路径，帮助在包含多个模块的复杂构建中导航。

# INSTALL

```pacman: sudo pacman -S gradle```

```apk: sudo apk add gradle```

```brew: brew install gradle```

```nix: nix profile install nixpkgs#gradle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradle](/man/gradle)(1), [gradle-tasks](/man/gradle-tasks)(1)

# RESOURCES

```[Documentation](https://docs.gradle.org/current/userguide/command_line_interface.html)```

<!-- verified: 2026-07-17 -->
