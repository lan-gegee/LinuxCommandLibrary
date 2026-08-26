# TAGLINE

读取和设置 INI 风格配置文件中的值

# TLDR

**获取**参数

```crudini --get [file.ini] [section] [param]```

**设置**参数

```crudini --set [file.ini] [section] [param] [value]```

**删除**参数

```crudini --del [file.ini] [section] [param]```

**合并**来自 stdin 的 INI 内容到文件

```crudini --merge [file.ini] < [snippet.ini]```

**设置**全局（无 section）参数

```crudini --set [file.ini] "" [param] [value]```

# SYNOPSIS

**crudini** **--set**|**--get**|**--del**|**--merge** [*options*] *config_file* ...

# DESCRIPTION

**crudini** 在 shell 中操作 INI 配置文件：获取/设置/删除参数、操作 section、合并片段。适用于必须编辑 **.ini** 文件而又不想依赖脆弱的 **sed** 的配置脚本。需要 Python **iniparse** 库。

# PARAMETERS

**--get** *file* [*section*] [*param*]

> 读取某个值，或列出 section/键。

**--set** *file* *section* [*param*] [*value*]

> 创建/更新值。空 section **""** 表示全局键。

**--del** *file* *section* [*param*]

> 删除参数或 section。

**--merge** *file* [*section*]

> 合并来自 stdin 的 INI 数据。

**--existing**

> 若目标项不存在则失败。

一次调用可以组合多个操作；参见 **crudini --help**。

# CAVEATS

INI 方言各有差异（重复键、多行值、嵌套 section）。务必先在生产配置的副本上测试。它不是通用的 TOML/YAML 编辑器。

# INSTALL

```apt: sudo apt install crudini```

```dnf: sudo dnf install crudini```

```zypper: sudo zypper install crudini```

```nix: nix profile install nixpkgs#crudini```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[augtool](/man/augtool)(1), [sed](/man/sed)(1), [git-config](/man/git-config)(1)

# RESOURCES

```[Source code](https://github.com/pixelb/crudini)```

<!-- verified: 2026-07-19 -->
