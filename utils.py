from config import pr, TARGET_FPS
pr.set_target_fps(TARGET_FPS)


class Utils():
    def __init__(self):
        self.mouse_coords = pr.Vector2()

    def update(self):
        self.mouse_coords = pr.get_mouse_position()

    def draw(self):
        pr.draw_fps(10, 10)
        pr.draw_text(f"X : {self.mouse_coords.x}",10, 30, 20, pr.RED)
        pr.draw_text(f"Y : {self.mouse_coords.y}",10, 50, 20, pr.RED)
        