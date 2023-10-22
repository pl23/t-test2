elif event.type == pygame.WINDOWRESIZED:
new_size = pygame.display.get_window_size()
new_size_x = new_size[0]
new_size_y = new_size[1]
new_size_x = clamp(new_size_x, 200, 1000)
new_size_y = clamp(new_size_y, 200, 1000)
new_size = (new_size_x, new_size_y)
screen = pygame.display.set_mode((new_size), pygame.RESIZABLE)
