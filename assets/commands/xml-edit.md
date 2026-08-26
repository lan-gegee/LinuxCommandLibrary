# TAGLINE

从命令行编辑 XML 文档

# TLDR

**更新元素值**

```xml edit -u "[//element]" -v "[new value]" [file.xml]```

**插入元素**

```xml edit -s "[//parent]" -t elem -n "[child]" -v "[value]" [file.xml]```

**删除元素**

```xml edit -d "[//element]" [file.xml]```

**重命名元素**

```xml edit -r "[//old]" -v "[new]" [file.xml]```

# SYNOPSIS

**xml edit** [_options_] _file_

# PARAMETERS

**-u**, **--update** _xpath_
> 更新匹配的节点。

**-d**, **--delete** _xpath_
> 删除匹配的节点。

**-s**, **--subnode** _xpath_
> 添加子节点。

**-i**, **--insert** _xpath_
> 在其前插入。

**-a**, **--append** _xpath_
> 在其后追加。

**-r**, **--rename** _xpath_
> 重命名节点。

**-v**, **--value** _value_
> 操作所用的值。

**-t**, **--type** _type_
> 节点类型（elem、attr、text）。

**-n**, **--name** _name_
> 节点名称。

**-L**, **--inplace**
> 就地编辑文件。

# DESCRIPTION

**xml edit** 从命令行修改 XML 文档。属于 xmlstarlet 工具集。支持插入、更新、删除和重命名元素及属性。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-select](/man/xml-select)(1), [xml-format](/man/xml-format)(1)
