# TAGLINE

管理多个 Java JDK 安装并自动设置 JAVA_HOME

# TLDR

**添加 JDK**

```jenv add [/path/to/java/home]```

**列出已安装版本**

```jenv versions```

**显示当前版本**

```jenv version```

**设置全局 Java 版本**

```jenv global [11.0.20]```

**为目录设置本地版本**

```jenv local [17.0.1]```

**为当前 shell 设置版本**

```jenv shell [11.0.20]```

**启用插件**

```jenv enable-plugin [export]```

**检查配置**

```jenv doctor```

# SYNOPSIS

**jenv** _command_ [_arguments_]

# SUBCOMMANDS

**add** _path_
> 添加 JDK 安装。

**versions**
> 列出可用版本。

**version**
> 显示当前激活的版本。

**global** _version_
> 设置全局默认版本。

**local** _version_
> 设置目录级版本。

**shell** _version_
> 为当前 shell 设置版本。

**enable-plugin** _name_
> 启用插件。

**disable-plugin** _name_
> 禁用插件。

**doctor**
> 校验配置。

# DESCRIPTION

**jenv** 管理多个 Java JDK 安装并自动设置 JAVA_HOME。它本身不安装 JDK。版本优先级：shell > local > global。JAVA_HOME 支持需启用 **export** 插件。本地版本会创建 **.java-version** 文件。

# INSTALL

```pacman: sudo pacman -S jenv```

```brew: brew install jenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1)
