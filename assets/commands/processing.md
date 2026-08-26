# TAGLINE

面向视觉艺术的编程语言和 IDE

# TLDR

**启动 Processing IDE**

```processing```

**从命令行运行 sketch**

```processing-java --sketch=[path/to/sketch] --run```

**导出为应用程序**

```processing-java --sketch=[path] --export```

**只构建不运行**

```processing-java --sketch=[path] --build```

# SYNOPSIS

**processing** [_options_]

**processing-java** [_options_] **--sketch=**_path_

# PARAMETERS

**--run**
> 运行 sketch。

**--build**
> 只构建不运行。

**--export**
> 导出为应用程序。

**--present**
> 以演示模式运行。

**--platform** _os_
> 目标平台。

**--output** _dir_
> 输出目录。

# DESCRIPTION

**Processing** 是一门可视化编程语言，同时也是一个 IDE，用于在视觉艺术的语境中学习编程。它为创意编程简化了 Java。

# EXAMPLES

```bash
# Launch IDE
processing

# Run sketch
processing-java --sketch=/path/to/sketch --run

# Export for all platforms
processing-java --sketch=/path/to/sketch --export

# Build only
processing-java --sketch=/path/to/sketch --build
```

# SKETCH EXAMPLE

```java
void setup() {
  size(400, 400);
}

void draw() {
  background(255);
  ellipse(mouseX, mouseY, 50, 50);
}
```

# CAVEATS

需要 Java。以 IDE 为中心的工作流。sketch 默认保存在 ~/sketchbook。

# HISTORY

Processing 由 **Casey Reas** 和 **Ben Fry** 于 2001 年在 MIT 媒体实验室创建，用于在视觉语境中教授编程。

# INSTALL

```nix: nix profile install nixpkgs#processing```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[p5](/man/p5)(1), [java](/man/java)(1)
