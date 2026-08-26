# TAGLINE

管理 conda 配置设置

# TLDR

**显示全部配置**

```conda config --show```

**显示特定配置项**

```conda config --show [channels]```

**添加频道**

```conda config --add channels [conda-forge]```

**移除频道**

```conda config --remove channels [channel_name]```

**设置某个配置值**

```conda config --set [auto_activate_base] [false]```

**显示配置来源**

```conda config --show-sources```

# SYNOPSIS

**conda** **config** [_options_]

# PARAMETERS

**--show** [_key_]
> 显示配置值。

**--add** _key_ _value_
> 向列表型配置项添加一个值。

**--remove** _key_ _value_
> 从列表型配置项移除一个值。

**--set** _key_ _value_
> 设置布尔型或字符串型配置项。

**--show-sources**
> 显示所有配置文件的来源。

**--env**
> 应用于环境级配置。

# CONFIGURATION

**~/.condarc**
> 用户级配置文件。

**.condarc**
> 项目或环境特定的配置。

# DESCRIPTION

**conda config** 提供了访问 conda 配置系统的命令行入口。该系统控制软件包频道、代理设置、SSL 验证、默认行为以及众多影响 conda 运行方式的选项。配置存储在 .condarc 文件（YAML 格式）中，可存在于系统、用户或项目级别，用户级通常位于 ~/.condarc。

配置系统采用分层覆盖机制，越具体的配置优先级越高。常见的配置任务包括管理频道优先级列表（决定搜索软件包时使用哪些仓库及其顺序）、为公司环境配置代理服务器、对内部仓库禁用 SSL 验证，以及控制环境的自动激活。

频道在 conda 配置中尤为重要，因为它们决定了软件包的来源。defaults 频道指向 Anaconda 的官方仓库，而 conda-forge 是由社区驱动、软件包选择更丰富的频道。当同一软件包存在于多个频道时，频道优先级会影响选用哪个版本。--show-sources 选项可揭示当前哪些 .condarc 文件正在生效，以及各配置值是如何被继承或覆盖的。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-info](/man/conda-info)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/config.html)```

<!-- verified: 2026-06-22 -->
