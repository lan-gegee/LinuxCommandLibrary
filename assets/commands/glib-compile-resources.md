# TAGLINE

GLib 资源文件编译器

# TLDR

**将资源编译**为二进制包

```glib-compile-resources [resources.gresource.xml]```

**编译并指定输出**文件

```glib-compile-resources --target=[resources.gresource] [resources.gresource.xml]```

**生成 C 源代码**而非二进制

```glib-compile-resources --generate-source --target=[resources.c] [resources.gresource.xml]```

**生成 C 头文件**

```glib-compile-resources --generate-header --target=[resources.h] [resources.gresource.xml]```

**为资源文件指定源目录**

```glib-compile-resources --sourcedir=[path/to/resources] [resources.gresource.xml]```

**为构建系统输出依赖列表**

```glib-compile-resources --generate-dependencies [resources.gresource.xml]```

**设置 C 标识符前缀**

```glib-compile-resources --c-name=[myapp] --generate-source [resources.gresource.xml]```

# SYNOPSIS

**glib-compile-resources** [_OPTIONS_] _FILE_

# PARAMETERS

**--target**=_TARGET_
> 输出文件路径。默认为输入文件的基本名加上相应的扩展名。

**--sourcedir**=_DIR_
> XML 中引用的资源文件所在目录。

**--generate-source**
> 生成 C 源文件而非二进制资源包。

**--generate-header**
> 生成与生成的源码配套使用的 C 头文件。

**--generate-dependencies**
> 将引用文件的列表输出到 stdout。

**--c-name**=_PREFIX_
> 生成代码中 C 标识符的前缀。

**--manual-register**
> 生成手动注册/注销函数，而非自动初始化。

**--internal**
> 生成内部符号（不导出）。

# DESCRIPTION

**glib-compile-resources** 将应用程序资源（图片、UI 文件、CSS、图标、数据）编译为二进制包或 C 源码，以便嵌入 GLib/GTK 应用程序。资源在 XML 文件（通常以 .gresource.xml 为扩展名）中描述，其中列出要包含的文件及可选的预处理方式。

GResource 系统使应用程序能够通过虚拟文件系统路径（如 /org/myapp/data.txt）访问嵌入的资源，而无需依赖外部文件。这简化了部署并加快了加载速度。

# CAVEATS

XML 中的资源路径必须与相对于 sourcedir 的实际文件位置一致。使用 XML 预处理选项时可能需要 xmllint 工具。大型资源会显著增加二进制体积。

# HISTORY

glib-compile-resources 随 GLib 2.32 于 **2012 年 3 月**推出，是 GResource API 的一部分。它取代了在 GTK 应用程序中嵌入资源的临时做法，提供了一种与 GNOME 构建系统集成的标准化方案。

# INSTALL

```apt: sudo apt install libgio-2.0-dev-bin```

```apk: sudo apk add glib-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

