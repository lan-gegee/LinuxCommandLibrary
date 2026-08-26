# TAGLINE

向 dconf 配置数据库写入值

# TLDR

**写入**某个键的值

```dconf write /[path/to/key] "[value]"```

写入**字符串**值

```dconf write /[path/to/key] "'[string]'"```

写入**整数**值

```dconf write /[path/to/key] "[5]"```

写入**布尔**值

```dconf write /[path/to/key] "[true]"```

写入**数组**值

```dconf write /[path/to/key] "['first', 'second']"```

写入**空数组**

```dconf write /[path/to/key] "@as []"```

# SYNOPSIS

**dconf write** _key_ _value_

# DESCRIPTION

**dconf write** 在 dconf 数据库中设置一个值。值必须以 GVariant 文本格式指定，这需要小心处理引号，以同时满足 shell 解析和 GVariant 语法的要求。

dconf write 的难点在于分层引号：shell 要求整个值参数用引号包裹，而 GVariant 格式又要求字符串有自己的引号。于是出现了像 "'string value'" 这样的写法——外层双引号是给 shell 的，内层单引号则是 GVariant 语法。整数、布尔及其他类型不需要内层引号。

对于正在监视 dconf 数据库的应用程序，更改会立即生效。与 gsettings 不同，dconf write 不依据 schema 校验值，因此可能写出应用程序无法接受的值。如需经过 schema 校验、错误检查更好的写入方式，请改用 gsettings。dconf write 最适合用于值格式已知且可控的脚本场景。

# PARAMETERS

_key_
> 键的完整路径

_value_
> GVariant 格式的值

# VALUE FORMATS

**Strings**
> 双引号内嵌单引号："'text'"

**Integers**
> 纯数字："42"

**Booleans**
> true 或 false

**Arrays**
> ['item1', 'item2']

**Empty typed arrays**
> @as []（字符串数组）、@ai []（整数数组）

# CAVEATS

引号规则很棘手：shell 引号包裹 GVariant 格式。字符串同时需要 shell 引号和 GVariant 引号。无效值会被静默忽略。需要校验的写入请使用 gsettings。

# INSTALL

```apt: sudo apt install dconf-cli```

```dnf: sudo dnf install dconf```

```pacman: sudo pacman -S dconf```

```apk: sudo apk add dconf```

```zypper: sudo zypper install dconf```

```nix: nix profile install nixpkgs#dconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dconf](/man/dconf)(1), [dconf-read](/man/dconf-read)(1), [gsettings](/man/gsettings)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/dconf)```

<!-- verified: 2026-07-11 -->
