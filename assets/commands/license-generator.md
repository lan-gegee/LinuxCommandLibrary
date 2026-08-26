# TAGLINE

从命令行生成 LICENSE 文件

# TLDR

**生成 MIT 许可证**

```license-generator MIT```

**列出支持的许可证**

```license-generator -l```

**设置作者和年份**

```license-generator MIT --author [name] --year [2024]```

**输出到 stdout**

```license-generator MIT --output /dev/stdout```

**多个许可证**（LICENSE-MIT 和 LICENSE-APACHE）

```license-generator MIT Apache```

# SYNOPSIS

**license-generator** [*options*] *LICENSE_TYPE*...

# DESCRIPTION

**license-generator** 从模板创建标准的开源 **LICENSE** 文件。使用 **cargo install license-generator** 安装。

支持的类型包括 AGPL、Apache、CC-BY、CC-BY-NC、CC-BY-NC-SA、CC-BY-SA、CC0、GPL、LGPL、MIT、MPL 和 Unlicense（用 **-l** 查看你的版本支持的完整列表）。

# PARAMETERS

*LICENSE_TYPE*

> 一个或多个许可证键名（例如 **MIT**、**Apache**）。指定多个类型会生成 **LICENSE-*** 文件。

**-l**, **--list**

> 列出可用的许可证。

**--author** *name*

> 作者字符串（默认：可用时取 git 用户名和邮箱）。

**--project** *name*

> 项目名称（某些许可证必需）。

**--year** *year*

> 版权年份。

**--output** *path*

> 输出路径（默认 **./LICENSE**）。

# CAVEATS

生成的文本只是一个起点；请确认许可证符合你项目的意图以及任何双许可需求。默认的作者检测依赖于 git config。

# INSTALL

```nix: nix profile install nixpkgs#license-generator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo-license](/man/cargo-license)(1), [licensecheck](/man/licensecheck)(1)

# RESOURCES

```[Source code](https://github.com/azu/license-generator)```

<!-- verified: 2026-07-19 -->
