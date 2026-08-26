# TAGLINE

从 dconf 配置数据库读取值

# TLDR

**读取**某个键的值

```dconf read /[path/to/key]```

读取键的**默认值**

```dconf read -d /[path/to/key]```

# SYNOPSIS

**dconf read** [_options_] _key_

# DESCRIPTION

**dconf read** 从 dconf 数据库读取一个值，并以 GVariant 文本格式输出。此子命令等同于直接将 "dconf read" 作为主命令使用。

该工具返回某个键当前存储的值；如果键不存在则无输出。使用 -d 标志会显示应用程序 GSettings schema 中定义的默认值，而不是用户自定义的值。这有助于判断重置用户偏好后应用程序会采用什么值。

值以 GVariant 格式输出：字符串带引号，数组使用方括号，空集合的类型化数据还带有类型标注。

# PARAMETERS

**-d**
> 显示默认值而非当前值

_key_
> 键的完整路径（例如 /org/gnome/desktop/interface/font-name）

# CAVEATS

键不存在时无输出。值为 GVariant 格式。如需 schema 信息，请改用 gsettings。

# INSTALL

```apt: sudo apt install dconf-cli```

```dnf: sudo dnf install dconf```

```pacman: sudo pacman -S dconf```

```apk: sudo apk add dconf```

```zypper: sudo zypper install dconf```

```nix: nix profile install nixpkgs#dconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dconf](/man/dconf)(1), [dconf-write](/man/dconf-write)(1), [gsettings](/man/gsettings)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/dconf)```

<!-- verified: 2026-07-11 -->
