from manim import *

SCALING = 2

class EULAV(Scene):
    def construct(self):
        # STICK FIGURE
        HEAD_SIZE = 0.2
        ARM_TO_TORSO_OFFSET = 0.4
        ARM_SIDE_LENGTH = 0.6
        ARM_HEIGHT = 0.5
        LEG_SIDE_LENGTH = 0.4
        LEG_HEIGHT = 0.8

        head = Circle(radius=HEAD_SIZE, color=WHITE)
        torso = Line(head.get_bottom(), head.get_bottom() + DOWN)
        ARM_BASE = torso.get_top() + DOWN * ARM_TO_TORSO_OFFSET
        right_arm = Line(ARM_BASE, ARM_BASE + RIGHT * ARM_SIDE_LENGTH + UP * ARM_HEIGHT)
        left_arm_1 = Line(ARM_BASE, ARM_BASE + (LEFT * ARM_SIDE_LENGTH + UP * ARM_HEIGHT)/2)
        left_arm_2 = Line(left_arm_1.get_end(), ARM_BASE + LEFT * ARM_SIDE_LENGTH + UP * ARM_HEIGHT)
        left_arm = VGroup(left_arm_1, left_arm_2)
        right_leg = Line(torso.get_bottom(), torso.get_bottom() + RIGHT * LEG_SIDE_LENGTH + DOWN * LEG_HEIGHT)
        left_leg = Line(torso.get_bottom(), torso.get_bottom() + LEFT * LEG_SIDE_LENGTH + DOWN * LEG_HEIGHT)
        stick_figure = VGroup(head, torso, right_arm, left_arm, right_leg, left_leg)
        stick_figure.scale(SCALING)

        # COMPUTER
        COMPUTER_WIDTH = 2
        COMPUTER_HEIGHT = 1.5
        COMPUTER_BASE_WIDTH = 0.8
        COMPUTER_BASE_HEIGHT = 0.2
        BASE_TO_COMPUTER_OFFSET = 0.1
        COMPUTER_TO_PERSON_HORIZONTAL_OFFSET = 1.5 * SCALING

        computer_screen = Rectangle(width=COMPUTER_WIDTH, height=COMPUTER_HEIGHT)
        computer_base = Rectangle(width=COMPUTER_BASE_WIDTH, height=COMPUTER_BASE_HEIGHT)
        computer_base.move_to(computer_screen.get_bottom(), UP*BASE_TO_COMPUTER_OFFSET)
        computer = VGroup(computer_screen, computer_base)
        computer.scale(SCALING)
        computer.move_to(stick_figure.get_right() + RIGHT * COMPUTER_TO_PERSON_HORIZONTAL_OFFSET)

        # BUTTONS
        BUTTON_WIDTH = 0.8
        BUTTON_HEIGHT = 0.3
        BUTTON_DOWN_OFFSET = 0.45 * SCALING
        BUTTON_SIDE_OFFSET = 0.45 * SCALING
        BUTTON_FONT_SIZE = 12
        BUTTON_CORNER_RADIUS = 0.1

        agree_button = RoundedRectangle(corner_radius=BUTTON_CORNER_RADIUS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREEN, fill_opacity=1)
        agree_button.move_to(computer_screen.get_center() + DOWN * BUTTON_DOWN_OFFSET + RIGHT * BUTTON_SIDE_OFFSET)
        agree_button_text = Text("I Agree", font_size=BUTTON_FONT_SIZE, color=BLACK)
        agree_button_text.move_to(agree_button.get_center())
        i_agree_button = VGroup(agree_button, agree_button_text)
        i_agree_button.scale(SCALING)
        decline_button = RoundedRectangle(corner_radius=BUTTON_CORNER_RADIUS, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=RED, fill_opacity=1)
        decline_button.move_to(computer_screen.get_center() + DOWN * BUTTON_DOWN_OFFSET + LEFT * BUTTON_SIDE_OFFSET)
        decline_button_text = Text("Decline", font_size=BUTTON_FONT_SIZE, color=BLACK)
        decline_button_text.move_to(decline_button.get_center())
        decline_button = VGroup(decline_button, decline_button_text)
        decline_button.scale(SCALING)
        buttons = VGroup(i_agree_button, decline_button)

        # EULA
        EULA_TOP_OF_SCREEN_OFFSET = 0.2 * SCALING
        LINE_SPACING = 0.1 * SCALING

        global eula_counter 
        eula_counter = 0

        def generate_eula():
            global eula_counter
            eula_counter += 1
            eula = Text(f"EULA {eula_counter}", font_size=20, color=WHITE)
            eula.move_to(computer_screen.get_top() + DOWN * EULA_TOP_OF_SCREEN_OFFSET)
            eula.scale(SCALING)
            return eula
        
        eula = generate_eula()
        eula_text_1 = Text("By agreeing to the EULA:", font_size=12, color=WHITE)
        eula_text_1.move_to(eula.get_bottom() + DOWN * LINE_SPACING * 1.5)
        eula_text_2 = Text("You agree to give us all your money", font_size=12, color=WHITE)
        eula_text_2.move_to(eula_text_1.get_bottom() + DOWN * LINE_SPACING)
        eula_text_3 = Text("You agree to give us your first born child", font_size=12, color=WHITE)
        eula_text_3.move_to(eula_text_2.get_bottom() + DOWN * LINE_SPACING)
        eula_text_4 = Text("You agree to give us your soul", font_size=12, color=WHITE)
        eula_text_4.move_to(eula_text_3.get_bottom() + DOWN * LINE_SPACING)

        eula_text = VGroup(eula_text_1, eula_text_2, eula_text_3, eula_text_4)

        # HELPER GROUPS
        computer_with_screen = VGroup(computer, buttons, eula, eula_text)
        scene = VGroup(stick_figure, computer_with_screen)

        # SCENE SETUP
        scene.move_to(ORIGIN)
        self.play(FadeIn(stick_figure))
        self.wait(0.2)
        self.play(FadeIn(computer_with_screen))

        # BUTTON CLICK
        ARM_CLICK_ROTATION = -PI/6
        ARM_DURATION = 0.5
        PULSE_SCALE_FACTOR = 1.1
        PULSE_DURATION = 0.05
        EULA_UPDATE_DURATION = 0.1
        ANIMATION_BASE_DURATION = 2 * (ARM_DURATION + PULSE_DURATION)

        arm_click_down = Rotate(
            right_arm,
            angle=ARM_CLICK_ROTATION,
            about_point=torso.get_top() + DOWN * ARM_TO_TORSO_OFFSET * SCALING,
            run_time=ARM_DURATION
        )
        arm_click_up = Rotate(
            right_arm,
            angle=-ARM_CLICK_ROTATION,
            about_point=torso.get_top() + DOWN * ARM_TO_TORSO_OFFSET * SCALING,
            run_time=ARM_DURATION
        )

        agree_button_scale_up_animation = ScaleInPlace(
            i_agree_button,
            scale_factor=PULSE_SCALE_FACTOR,
            run_time=PULSE_DURATION
        )
        agree_button_scale_down_animation = ScaleInPlace(
            i_agree_button,
            scale_factor=1/PULSE_SCALE_FACTOR,
            run_time=PULSE_DURATION
        )
    
        agree_click = Succession(
            arm_click_down,
            agree_button_scale_up_animation,
            agree_button_scale_down_animation,
            arm_click_up,
        )

        for i in range(9):
            SPEEDUP_FACTOR = 1+i/3
            self.play(agree_click, run_time=ANIMATION_BASE_DURATION/SPEEDUP_FACTOR)
            self.play(Transform(eula, generate_eula(), run_time=EULA_UPDATE_DURATION/SPEEDUP_FACTOR))

        # EULAV
        LOGO_START_SCALE = 0.4 * SCALING
        LOGO_FINAL_SCALE = 0.85 * SCALING
        LOGO_OPACITY = 0.2
        EULAV_APPEARACE_DURATION = 2

        shield_logo = ImageMobject("logo.png")
        shield_logo.scale(LOGO_START_SCALE)
        shield_logo.move_to(ORIGIN)
        shield_logo.generate_target()
        shield_logo.target.scale(LOGO_FINAL_SCALE)
        shield_logo.target.move_to(computer_with_screen.get_center())
        shield_logo.target.set_opacity(LOGO_OPACITY)

        self.play(FadeIn(shield_logo), run_time=EULAV_APPEARACE_DURATION)
        self.play(MoveToTarget(shield_logo))
        self.wait(0.5)

        ## HIGHLIGHT
        HIGHLIGHT_OPACITY = 0.3

        bg_2 = BackgroundRectangle(eula_text_2, fill_opacity=HIGHLIGHT_OPACITY, fill_color=RED)
        bg_3 = BackgroundRectangle(eula_text_3, fill_opacity=HIGHLIGHT_OPACITY, fill_color=PURPLE)
        bg_4 = BackgroundRectangle(eula_text_4, fill_opacity=HIGHLIGHT_OPACITY, fill_color=BLUE)
        bgs = VGroup(bg_2, bg_3, bg_4)
        self.play(FadeIn(bgs))

        ## USER REACTION
        USER_REACTION_DURATION = 0.75

        left_arm_2.generate_target()
        left_arm_2.target.rotate(-PI/2, about_point=left_arm_2.get_start())
        head.generate_target()
        head.target.color = RED
        head.target.scale(1.1)
        self.play(MoveToTarget(head), MoveToTarget(left_arm_2), run_time=USER_REACTION_DURATION)

        decline_button_scale_up_animation = ScaleInPlace(
            decline_button,
            scale_factor=PULSE_SCALE_FACTOR,
            run_time=PULSE_DURATION
        )
        decline_button_scale_down_animation = ScaleInPlace(
            decline_button,
            scale_factor=1/PULSE_SCALE_FACTOR,
            run_time=PULSE_DURATION
        )
    
        decline_click = Succession(
            arm_click_down,
            decline_button_scale_up_animation,
            decline_button_scale_down_animation,
            arm_click_up,
        )

        self.play(decline_click, run_time=ANIMATION_BASE_DURATION)
        self.wait(0.5)

        ## FINAL SCENE
        CLEAR_TIME = 1.5

        shield_logo.generate_target()
        shield_logo.target.move_to(ORIGIN)
        shield_logo.target.set_opacity(1)
        
        self.play(FadeOut(scene), FadeOut(bgs), MoveToTarget(shield_logo), run_time=CLEAR_TIME)
        brand = Text("EULAV", font_size=80, color=WHITE)
        brand.move_to(shield_logo.get_center())
        self.play(FadeIn(brand))
            

def main():
    config.quality = "high_quality" ## change to "fourk_quality" for 4k
    scene = EULAV()
    scene.render()

if __name__ == "__main__":
    main()
