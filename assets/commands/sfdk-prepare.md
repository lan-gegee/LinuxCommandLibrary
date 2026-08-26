# TAGLINE

为 Sailfish OS 构建准备源码

# TLDR

**为构建准备源码**

```sfdk prepare```

**以详细输出进行准备**

```sfdk prepare --verbose```

# SYNOPSIS

**sfdk prepare** [_options_]

# PARAMETERS

**--verbose**
> 在准备过程中启用详细输出。

# DESCRIPTION

**sfdk prepare** 为构建 Sailfish OS 软件包准备源文件。它会执行 RPM spec 文件的 `%prep` 阶段，通常包括解压源码归档、应用补丁以及生成自动配置文件。这是 RPM 构建过程中实际编译之前的第一步。

属于用于开发 Sailfish OS 应用和软件包的 **Sailfish SDK**（`sfdk`）工具链的一部分。

# CAVEATS

需要配置正确的 Sailfish SDK 构建环境，且项目中存在有效的 RPM spec 文件。必须在 sfdk 管理的项目目录中运行。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-build-init](/man/sfdk-build-init)(1)
