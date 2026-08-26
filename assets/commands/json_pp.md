# TAGLINE

来自 Perl 的 JSON 格式化打印工具

# TLDR

**格式化输出 JSON**

```json_pp < [data.json]```

**将 JSON 文件格式化后写入输出文件**

```json_pp < [input.json] > [output.json]```

**按字母顺序排序键**

```json_pp -json_opt canonical < [data.json]```

**输出为 Perl Data::Dumper 格式**

```json_pp -t dumper < [data.json]```

**同时使用多个格式化选项**

```json_pp -json_opt pretty,canonical,utf8 < [data.json]```

**校验 JSON**（输出重定向到 null）

```json_pp -t null < [data.json]```

# SYNOPSIS

**json_pp** [**-v**] [**-f** _from_format_] [**-t** _to_format_] [**-json_opt** _options_]

# PARAMETERS

**-f** _FORMAT_
> 输入格式：json（默认）或 eval（Perl 代码）。

**-t** _FORMAT_
> 输出格式：json（默认）、dumper（Data::Dumper）或 null。

**-json_opt** _OPTIONS_
> 以逗号分隔的 JSON 格式化选项：ascii、latin1、utf8、pretty、indent、space_before、space_after、relaxed、canonical、allow_nonref、allow_singlequote、allow_barekey、allow_bignum、loose、escape_slash、indent_length。

**-v**
> 详细模式（目前无实际作用）。

**-V**
> 打印版本并退出。

# DESCRIPTION

**json_pp** 是 JSON::PP 附带的命令行实用程序，可在输入和输出格式之间转换（其中之一是 JSON）。它从 stdin 读取并向 stdout 输出。默认行为是以格式化形式输出 JSON。

该工具提供基本的格式化和校验功能。装有 Perl 的系统上通常已预装。

# CAVEATS

多个 **-json_opt** 值必须在单个选项内以逗号分隔，不能写成多个标志。复杂的 JSON 操作建议改用 jq。

# HISTORY

json_pp 是 **Perl 的 JSON::PP 模块**的一部分，提供了一个简单的命令行 JSON 格式化工具。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [python](/man/python)(1), [jsonlint](/man/jsonlint)(1)
