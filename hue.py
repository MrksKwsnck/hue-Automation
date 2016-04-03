from phue import *

class Hue:
    '''Wrapper for `phue`.'''
    
    BRI_MAX = 254
    BRI_MIN = 0
    BRI_STEP = 16
    HUE_MAX = 65535
    HUE_MIN = 0
    HUE_STEP = 4096
    
    def __init__(self):
        self.bridge = Bridge(None, None, 'python_hue.json')
        self.light_pointer = 0
    
    def current_light(self):
        return self.bridge.lights[self.light_pointer]
    
    def next_light(self):
        if self.light_pointer == len(self.bridge.lights) - 1:
            self.light_pointer = 0
        else:
            self.light_pointer += 1
        self.alert_current_light()
        return self.current_light()
    
    def prev_light(self):
        if self.light_pointer == 0:
            self.light_pointer = len(self.bridge.lights) - 1
        else:
            self.light_pointer -= 1
        self.alert_current_light()
        return self.current_light()
    
    def alert_current_light(self):
        self.current_light().alert = 'select'

    def lalert_current_light(self):
        self.current_light().alert = 'lselect'

    def toggle_colorloop(self):
        if self.current_light().effect == 'none':
            self.current_light().effect = 'colorloop'
        elif self.current_light().effect == 'colorloop':
            self.current_light().effect = 'none'

    def toggle_on(self):
        if self.current_light().on == False:
            self.current_light().on = True
        elif self.current_light().on == True:
            self.current_light().on = False

    def inc_bri(self):
        bri = self.current_light().brightness
        if bri + self.BRI_STEP > self.BRI_MAX:
            bri = self.BRI_MAX
        else:
            bri += self.BRI_STEP
        self.current_light().brightness = bri

    def dec_bri(self):
        bri = self.current_light().brightness
        if bri - self.BRI_STEP < self.BRI_MIN:
            bri = self.BRI_MIN
        else:
            bri -= self.BRI_STEP
        self.current_light().brightness = bri

    def shift_hue_right(self):
        hue = self.current_light().hue
        if hue + self.HUE_STEP > self.HUE_MAX:
            hue = (hue + self.HUE_STEP) - self.HUE_MAX
        else:
            hue += self.HUE_STEP
        self.current_light().hue = hue

    def shift_hue_left(self):
        hue = self.current_light().hue
        if hue - self.HUE_STEP < self.HUE_MIN:
            hue = (hue - self.HUE_STEP) + self.HUE_MAX
        else:
            hue -= self.HUE_STEP
        self.current_light().hue = hue
