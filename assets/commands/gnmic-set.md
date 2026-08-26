# TAGLINE

修改 gNMI 设备上的配置

# TLDR

**设置配置值**

```gnmic set -a [router:57400] --update-path [/system/name] --update-value "[router1]"```

**删除配置**

```gnmic set -a [router:57400] --delete [/interfaces/interface[name=eth1]]```

**从文件设置**

```gnmic set -a [router:57400] --update-path [/] --update-file [config.json]```

**替换配置**

```gnmic set -a [router:57400] --replace-path [/interfaces] --replace-file [interfaces.json]```

**在一个标志中组合路径、类型和值**

```gnmic set -a [router:57400] --update [/system/name:::string:::router1]```

**预览 set 操作而不发送**

```gnmic set -a [router:57400] --update-path [/system/name] --update-value "[router1]" --dry-run```

# SYNOPSIS

**gnmic set** [_options_]

# PARAMETERS

**-a**, **--address** _ADDRESS_
> 目标地址，属于 gnmic 的全局标志。

**--prefix** _PATH_
> 应用到请求中所有路径的公共前缀。

**--update-path** _PATH_
> 要更新的路径；与 **--update-value** 或 **--update-file** 配对使用。

**--update-value** _VALUE_
> 要写入 **--update-path** 的值。

**--update-file** _FILE_
> 从 JSON 或 YAML 文件读取更新值。

**--update** _PATH:::TYPE:::VALUE_
> 用一个标志定义完整的更新，以 `:::` 为分隔符（可通过 **--delimiter** 自定义）。

**--replace-path** _PATH_
> 要替换的路径；与 **--replace-value** 或 **--replace-file** 配对使用。

**--replace-value** _VALUE_
> 要写入 **--replace-path** 的值。

**--replace-file** _FILE_
> 从 JSON 或 YAML 文件读取替换值。

**--replace** _PATH:::TYPE:::VALUE_
> 用一个标志定义完整的替换，以 `:::` 为分隔符。

**--delete** _PATH_
> 要删除的路径。

**--dry-run**
> 构建并打印 SetRequest 而不发送到目标设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnmic set** 修改支持 gNMI 的设备上的配置。它支持对配置数据执行 update（合并）、replace（替换）和 delete（删除）操作。

该命令既可以设置单个值，也可以应用整个配置文件。用于通过 gNMI 协议进行网络自动化和配置管理。

# CAVEATS

在某些设备上变更可能需要提交（commit）。无效配置可能被拒绝。请先在实验环境中测试。

# HISTORY

gnmic set 是 **gnmic** 的子命令，后者是由 Nokia 创建的 gNMI 客户端。

# INSTALL

```brew: brew install gnmic```

```nix: nix profile install nixpkgs#gnmic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnmic](/man/gnmic)(1), [gnmic-get](/man/gnmic-get)(1), [gnmic-subscribe](/man/gnmic-subscribe)(1)

# RESOURCES

```[Documentation](https://gnmic.openconfig.net/cmd/set/)```

```[Source code](https://github.com/openconfig/gnmic)```

<!-- verified: 2026-07-17 -->
