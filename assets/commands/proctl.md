# TAGLINE

管理项目许可证与语言配置

# TLDR

列出可用的**许可证**

```proctl -ll```

列出可用的**语言**

```proctl -lL```

交互式**挑选**许可证

```proctl -pl```

交互式**挑选**语言

```proctl -pL```

从项目中**移除**许可证

```proctl -r```

创建新的许可证**模板**

```proctl -t```

**删除**许可证模板

```proctl -R [@license_name]```

# SYNOPSIS

**proctl** [**-i**|**-ll**|**-lL**|**-c**|**-pl**|**-pL**|**-P** _license_|**-r**|**-sl** _query_|**-sL** _query_|**-T**|**-t**|**-R** _license_|**-C**|**-k**]

# PARAMETERS

**-i, -initialize**
> 为项目初始化 git 仓库

**-ll, -list-licenses**
> 列出所有可用的许可证模板

**-lL, -list-languages**
> 列出支持的编程语言

**-c, -current-license**
> 显示当前生效的项目许可证

**-pl, -pick-license**
> 通过 fzf 交互式选择许可证

**-pL, -pick-languages**
> 通过 fzf 交互式选择语言

**-P, -preview-license**
> 查看特定的许可证模板

**-r, -remove-license**
> 从当前项目移除许可证

**-sl, -search-license**
> 查找匹配查询模式的许可证

**-sL, -search-language**
> 查找匹配查询模式的语言

**-T, -template-help**
> 显示模板变量文档

**-t, -new-template**
> 创建新的许可证或语言模板

**-R, -delete-license**
> 从系统中移除一个或多个许可证模板

**-C, -new-config**
> 生成默认配置文件

**-k, -check-conflict**
> 检测相互冲突的许可证文件

**-h, -help**
> 显示帮助信息

# DESCRIPTION

**proctl** 管理项目的许可证和语言配置。它提供基于模板的许可证管理和交互式选择，让在项目中添加或切换许可证变得轻松。

该工具支持自定义许可证模板，并与 fzf 集成以模糊选择许可证和语言。配置存储在 **~/.config/license.conf** 中（首次启动或使用 **-new-config** 时自动生成）。

# CAVEATS

交互式选择菜单（**-pl**、**-pL**）可选依赖 fzf。许可证模板存储在用户配置中。自定义模板需手动创建。

# HISTORY

**proctl** 由 **HeCodes2Much**（CreativeCodeCat）创建，用于简化项目许可证管理，对需要处理多种许可要求的多项目开发者尤其有用。

# INSTALL

```aur: yay -S proctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[licensor](/man/licensor)(1), [fzf](/man/fzf)(1)
