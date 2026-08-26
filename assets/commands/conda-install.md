# TAGLINE

软件包安装管理器

# TLDR

**安装一个软件包**

```conda install [package_name]```

**安装指定版本**

```conda install [package_name]=[version]```

**从指定频道安装**

```conda install -c [conda-forge] [package_name]```

**安装到指定环境**

```conda install -n [env_name] [package_name]```

**安装多个软件包**

```conda install [package1] [package2] [package3]```

**免确认安装**

```conda install -y [package_name]```

# SYNOPSIS

**conda** **install** [_options_] [_packages..._]

# PARAMETERS

**-n**, **--name** _name_
> 安装到指定的具名环境。

**-c**, **--channel** _channel_
> 搜索时使用的附加频道。

**-y**, **--yes**
> 不请求确认。

**--freeze-installed**
> 不更新已安装的软件包。

**--update-deps**
> 更新依赖。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda install** 将软件包安装到 conda 环境中。它会解析依赖并确保软件包之间的兼容性。

软件包会在已配置的频道中搜索；除非指定了具体频道，否则 defaults 频道会被优先搜索。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-remove](/man/conda-remove)(1), [conda-update](/man/conda-update)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/install.html)```

<!-- verified: 2026-06-22 -->
