# TAGLINE

以 JSON 格式输出已安装软件包的元数据

# TLDR

**检查已安装的软件包**

```pip inspect```

**以 JSON 输出**

```pip inspect --local```

# SYNOPSIS

**pip** **inspect** [_options_]

# PARAMETERS

**--local**
> 仅检查虚拟环境中的软件包。

**--user**
> 仅检查用户级安装的软件包。

**--path** _path_
> 检查位于该路径下的软件包。

# DESCRIPTION

**pip inspect** 输出描述已安装软件包及其元数据的 JSON。提供关于已安装发行版的详细信息，包括版本、requires 和 provides 元数据。适用于程序化的环境分析。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-list](/man/pip-list)(1), [pip-show](/man/pip-show)(1)
