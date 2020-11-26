from kivy.app import App
from kivy.lang import Builder
from encode import encode_module
from encode_pass import encode_pass
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("design.kv")
click = SoundLoader.load("click.wav")
sound = SoundLoader.load("iron.wav")
sound.loop = True
sound.play()


class ClassMethod(Screen):
    @property
    def click_sound(self):
        click.play()

    def switch_screen(self, screen_x):
        self.manager.transition = FadeTransition(duration=0.3)
        string = "self.manager.current = " + screen_x
        exec(string)

    @property
    def on_exit(self):
        quit()


class ScreenOne(ClassMethod):
    def global_declaration(self):
        # below can be used to keep track of a person's logs.
        global is_logged_in
        is_logged_in = False


class ScreenTwo(ClassMethod):
    def clear_fields(self):
        self.ids.login_username.text = ""
        self.ids.login_password.text = ""

    def login_submit(self):
        self.username = self.ids.login_username.text
        self.password = self.ids.login_password.text
        if self.username == "":
            self.username = "user"
        if self.password == "":
            self.password = "123"
        self.username = encode_module(self.username)
        self.password = encode_pass(self.password)
        global var01_user
        var01_user = self.username
        global var01_pin
        var01_pin = self.password


class ScreenThree(ClassMethod):
    def clear_fields(self):
        self.ids.signup_username.text = ""
        self.ids.signup_password.text = ""

    def signup_submit(self):
        global user_exists
        self.username = self.ids.signup_username.text
        self.password = self.ids.signup_password.text
        if self.username == "":
            self.username = "user"
        if self.password == "":
            self.password = "123"
        self.username = encode_module(self.username)
        self.password = encode_pass(self.password)
        try:
            self.open_file = open(self.password, "r")
            user_exists = True
        except:
            user_exists = False
            self.file1 = open(self.password, "w+")
            self.file1.write(self.username + "\n" + self.password + "\n")
            self.file1.close()


class ScreenFour(ClassMethod):
    pass


class ScreenFive(ClassMethod):
    def signup_success(self):
        if user_exists:
            self.ids.log_notif.text = "User already exists\nTry using a different pin"
        else:
            self.ids.log_notif.text = "Successfully Signed up!"


class ScreenSix(ClassMethod):
    def signup_success_text(self):
        try:
            self.file = open(var01_pin, "r")
        except:
            # the below line of code will create the file if not created.
            self.file = open("file.txt", "a+")
            self.file.close()
            self.file = open("file.txt", "r")
        self.verify = self.file.read().splitlines()
        if var01_user in self.verify:
            if var01_pin in self.verify:
                self.ids.log_notif_text.text = "Successfully Logged in!"
        else:
            self.ids.log_notif_text.text = "Wrong Username or pin."
        self.file.close()


class Manager(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MainApp().run()
