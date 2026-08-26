# TAGLINE

SPA JSON 到标准 JSON 的转换器

# TLDR

**将 PipeWire 配置文件转换**为标准 JSON

```spa-json-dump /usr/share/pipewire/pipewire.conf```

**转换 SPA JSON 文件**并用 jq 美化输出

```spa-json-dump [path/to/file.conf] | jq .```

**从 stdin 读取 SPA JSON** 并输出为标准 JSON

```cat [path/to/file.conf] | spa-json-dump```

# SYNOPSIS

**spa-json-dump** [_FILE_]

# DESCRIPTION

**spa-json-dump** 读取 SPA JSON 文件或标准输入，并将其输出为标准 JSON。SPA JSON 是 PipeWire 配置文件使用的一种轻量 JSON 变体。SPA JSON 解析器刻意保持宽松，能处理多种类 JSON 语法，包括不带引号的字符串和注释——这些在严格 JSON 中都是非法的。此工具通过将 SPA JSON 转换为符合标准的 JSON 来弥补这一差距，使其可以被 **jq** 或任何 JSON 解析器处理。

# CAVEATS

除了可选的文件参数外，该工具没有任何选项。如果输入不是有效的 SPA JSON，输出可能格式错误或为空，且不会给出明确的错误信息。仅对 PipeWire SPA JSON 文件有用；标准 JSON 文件会原样通过。

# HISTORY

**spa-json-dump** 作为 **PipeWire** 项目的一部分推出。PipeWire 是现代的 Linux 音视频服务器，已在许多发行版中取代 PulseAudio 和 JACK。PipeWire 使用自己的 SPA（Simple Plugin API）JSON 格式进行配置，创建此工具是为了让这些配置文件能够与标准 JSON 工具互操作。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-spa-tools```

```zypper: sudo zypper install pipewire-spa-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [jq](/man/jq)(1), [pw-dump](/man/pw-dump)(1)
