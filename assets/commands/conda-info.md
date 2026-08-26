# TAGLINE

显示当前 conda 安装的信息

# TLDR

**显示 conda 信息**

```conda info```

**显示全部信息**（详细模式，包含频道、配置文件、插件）

```conda info --all```

**列出所有环境**

```conda info --envs```

**显示 base 环境路径**

```conda info --base```

**显示影响 conda 的环境变量**

```conda info --system```

**显示 conda 所管理目录的磁盘占用**

```conda info --size```

**以 JSON 格式显示信息**（机器可读）

```conda info --json```

**显示某个软件包的信息**（取代已移除的 `conda info <pkg>`）

```conda search [package_name] --info```

# SYNOPSIS

**conda** **info** [_options_]

# PARAMETERS

**-a**, **--all**
> 显示全部信息（频道、配置文件、插件、环境列表等）。

**--base**
> 显示 base 环境路径。

**-e**, **--envs**
> 列出所有已知的 conda 环境。配合 **--json** 可获得更多细节。

**-s**, **--system**
> 列出影响 conda 的环境变量。

**--size**
> 按环境显示 conda 所管理目录的磁盘占用。

**--unsafe-channels**
> 显示暴露了认证令牌的频道列表（请谨慎使用）。

**--json**
> 以 JSON 格式输出。适合程序化消费。

**-v**, **--verbose**
> 提高日志详细程度。最多重复四次可达 TRACE 级别。

**-q**, **--quiet**
> 隐藏进度条。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda info** 显示当前 conda 安装的信息，包括版本、配置文件、已配置的频道以及环境位置。

用于查看软件包的旧形式 **conda info** _package_ 已被弃用，并在 **conda 24.3（2024 年 3 月）** 中移除。请改用 **conda search** _package_ **--info**。

# CAVEATS

**conda info** _package_ 不再打印软件包元数据；请使用 **conda search** _package_ **--info**。**--unsafe-channels** 选项会以明文暴露频道的认证令牌，因此应避免在共享日志中使用。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-config](/man/conda-config)(1), [conda-list](/man/conda-list)(1)
