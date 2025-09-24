from config import pr


class Button():
    def __init__(self, posX, posY, width, height, text, color_hovered=pr.YELLOW, color_normal=pr.RED, color_pressed=pr.GREEN):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.text = text
        self.bounds = pr.Rectangle(self.posX, self.posY, self.width, self.height)
        self.color_hovered = color_hovered
        self.color_normal = color_normal
        self.color_pressed = color_pressed
        self.is_hovered = False
        self.is_pressed = False
        self.was_clicked = False


    def update(self):
        self.mouse_coords = pr.get_mouse_position()

        self.is_hovered = pr.check_collision_point_rec(self.mouse_coords, self.bounds)
        self.was_clicked = False

        if self.is_hovered:
            if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
                self.is_pressed = True
            elif pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                self.was_clicked = True
            self.is_pressed = False
        else:
            self.is_pressed = False
    

    def draw(self):
        if self.is_pressed:
            color = self.color_pressed
        elif self.is_hovered:
            color = self.color_hovered
        else:
            color = self.color_normal
        
        pr.draw_rectangle(self.posX, self.posY, self.width, self.height, color)

        ### Centering Text inside the Button
        text_width = pr.measure_text(self.text, 20)
        text_x = self.bounds.x + (self.bounds.width - text_width) / 2
        text_y = self.bounds.y + (self.bounds.height - 20) / 2
        pr.draw_text(self.text, int(text_x), int(text_y), 20, pr.BLACK)

    def clicked(self):
        return self.was_clicked
    



class ToggleButton(Button):
    def __init__(self, posX,posY,
                width, height, 
                text, color_hovered=pr.YELLOW, 
                color_normal=pr.RED, color_pressed=pr.GREEN):
        super().__init__(posX, posY, width, height, text, color_hovered, color_normal, color_pressed)
        self.Toggled = False
    
    def update(self):
        super().update()
        if self.clicked():
            self.Toggled = not self.Toggled
    
    def draw(self):
        super().draw()

        if self.Toggled:
            base_color = self.color_pressed
        else:
            base_color = self.color_normal
        
        pr.draw_rectangle_rec(self.bounds, base_color)

        ### Centering Text
        text_width = pr.measure_text(self.text, 20)
        text_x = self.bounds.x + (self.bounds.width - text_width) / 2
        text_y = self.bounds.y + (self.bounds.height - 20) / 2
        pr.draw_text(self.text, int(text_x), int(text_y), 20, pr.BLACK)
    