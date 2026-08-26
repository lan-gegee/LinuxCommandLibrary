# TAGLINE

为 systemd 单元名称转义字符串

# TLDR

**转义**给定文本

```systemd-escape [text]```

**反转义**

```systemd-escape -u [escaped_text]```

**将给定文本视为路径处理（合并斜杠和 ".."）**

```systemd-escape -p [/path/to/resource]```

**为转义后的文本追加单元后缀**

```systemd-escape --suffix [service] [text]```

**将转义后的文本插入模板单元**

```systemd-escape --template [getty@.service] [tty1]```

**从路径构建 .mount 单元名称**

```systemd-escape -p --suffix=mount [/tmp/waldi/foobar/]```

**将部分未转义的输入修正为有效的单元名称**

```systemd-escape -m [some string]```

# SYNOPSIS

**systemd-escape** [_options_] [_string_...]

# PARAMETERS

**-u**, **--unescape**
> 反转转义（解码）。不能与 **--suffix=** 或 **--mangle** 组合使用。

**-p**, **--path**
> 将参数视为文件系统路径，简化斜杠和 ".." 组件。适用于生成与 `%f` 说明符匹配的字符串。

**--suffix=**_suffix_
> 为转义后的字符串追加单元类型后缀，例如 `service` 或 `mount`。与 **--template=**、**--unescape** 和 **--mangle** 不兼容。

**--template=**_template_
> 将转义后的字符串插入到类似 `foobar@.service` 的模板单元名称的 `@` 位置。配合 **--unescape** 使用时，仅提取并反转义实例部分。

**-m**, **--mangle**
> 仅转义明显未转义的字符，并在缺少时追加合适的单元后缀。与 **--suffix=**、**--template=** 和 **--unescape** 不兼容。

**--instance**
> 与 **--unescape --template=** 配合使用：只打印模板单元名称的实例部分。

**-h**, **--help**
> 显示帮助文本。

**--version**
> 显示版本信息。

# DESCRIPTION

**systemd-escape** 将任意字符串转换为有效的 systemd 单元名称组件，或者逆转该转换。systemd 单元名称有严格的命名规则：只允许字母数字、`:`、`_` 和 `.`；其他字符会被编码为 `\xNN` 序列，`/` 则变成 `-`。

该工具在从路径构建 **.mount** 或 **.swap** 单元时特别有用，也适用于用动态实例字符串实例化 `foo@.service` 这类模板单元的场景。

# EXAMPLES

```bash
$ systemd-escape 'Hallöchen, Meister'
Hall\xc3\xb6chen\x2c\x20Meister

$ systemd-escape -u 'Hall\xc3\xb6chen\x2c\x20Meister'
Hallöchen, Meister

$ systemd-escape -p --suffix=mount "/tmp//waldi/foobar/"
tmp-waldi-foobar.mount
```

# CAVEATS

路径中的正斜杠在转义后会变成短横线，前导斜杠会被 **--path** 去除。某些选项组合互斥（见上文）。本命令是 systemd 套件的一部分，凡安装了 systemd 的系统均可使用。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1)
