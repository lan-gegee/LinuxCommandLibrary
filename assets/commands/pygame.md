# TAGLINE

Python 游戏开发库

# TLDR

**安装 Pygame**

```pip install pygame```

**运行 Pygame 示例**

```python -m pygame.examples.aliens```

**检查安装**

```python -c "import pygame; print(pygame.ver)"```

# SYNOPSIS

**pygame** Python library for game development

# DESCRIPTION

**Pygame** 是构建在 SDL 之上的 Python 游戏开发库。它提供图形、声音、输入处理和游戏逻辑等模块，非常适合 2D 游戏和多媒体应用。

# BASIC EXAMPLE

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    pygame.display.flip()

pygame.quit()
```

# KEY MODULES

```python
pygame.display  # Window management
pygame.draw     # Shape drawing
pygame.image    # Load/save images
pygame.mixer    # Sound playback
pygame.font     # Text rendering
pygame.sprite   # Sprite groups
pygame.time     # Timing/FPS control
pygame.key      # Keyboard input
pygame.mouse    # Mouse input
```

# EXAMPLES

```bash
# List all examples
python -m pygame.examples

# Run specific example
python -m pygame.examples.chimp
python -m pygame.examples.aliens
```

# CAVEATS

专注于 2D。如需 3D 可考虑 PyOpenGL 或 Panda3D。基于 SDL，跨平台支持良好。

# HISTORY

Pygame 由 **Pete Shinners** 于 2000 年创建，作为 SDL 的 Python 封装，简化了游戏开发。

# SEE ALSO

[python](/man/python)(1)
