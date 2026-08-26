# TAGLINE

无需构建工具即可将 Java 程序作为脚本运行

# TLDR

**运行 Java 脚本**

```jbang [script.java]```

**创建新脚本**

```jbang init [script.java]```

**带依赖运行**

```jbang [script.java]```

**在 IDE 中编辑**

```jbang edit [script.java]```

**安装为命令**

```jbang app install [script.java]```

**从 URL 运行**

```jbang [https://example.com/script.java]```

# SYNOPSIS

**jbang** [_options_] _command_ [_args_]

# PARAMETERS

**init** _FILE_
> 创建新脚本。

**run** _FILE_
> 运行脚本（默认）。

**edit** _FILE_
> 在 IDE 中打开。

**app install** _FILE_
> 将脚本安装为应用。

**--deps** _GAV_
> 添加 Maven 依赖。

**--java** _VERSION_
> 使用指定的 Java 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jbang** 无需构建工具即可将 Java 程序作为脚本运行。它会自动处理依赖、编译和执行。

该工具支持通过注释内联声明依赖。它让 Java 编程可以像 shell 脚本一样进行。

# CAVEATS

需要 Java。首次运行时会下载依赖。脚本通过注释指令进行配置。

# HISTORY

jbang 由 **Max Rydahl Andersen** 创建，目的是让 Java 脚本编写像 Python 或 Bash 脚本一样简单。

# INSTALL

```brew: brew install jbang```

```nix: nix profile install nixpkgs#jbang```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [kotlin](/man/kotlin)(1)
