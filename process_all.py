from PIL import Image
im = Image.open("giphy.gif")


def get_program(data_array, set_frames_code):
    HEADER = """
    #include <Adafruit_NeoPixel.h>
    #include <avr/pgmspace.h>
    #ifdef __AVR__
      #include <avr/power.h>
    #endif

    #define PIN 5

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(750, PIN, NEO_GRB + NEO_KHZ800);

    void setup() {
      #if defined (__AVR_ATtiny85__)
        if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
      #endif
      strip.begin();
      strip.show(); 
    }
    """

    print(HEADER)
    print(data_array)

    PREPROGRAM = """

    uint32_t frame_count = 0;
    long total_frames_count = 2250;
    int max_led_strength = 10;

    void loop() {
      while(true){
          Serial.println("again");
        setFrame();
      }
    }

    bool test = false;

    void setFrame(){
      int wait = 50;
    """

    return HEADER + data_array + PREPROGRAM + set_frames_code + "}"


def zig_zagged_line_to_plane(n):
    y = n // 30
    if (n // 30) % 2 == 0:
        return (y, n - y * 30)
    else:
        return (y, 29 - (n - y * 30))

data_array = ""
set_frames_code = ""
frame_count = 0
# To iterate through the entire gif
try:
    while 1:
        for i in range(1):
            im.seek(im.tell()+1)

        if frame_count > 32:
            print(get_program(data_array, set_frames_code))
        
        resized = im.resize((30,30)).convert('RGB')

        data_array = data_array + "const PROGMEM uint8_t frame"+str(frame_count)+"[] = {"

        for image_index in range(750):
            x, y = zig_zagged_line_to_plane(image_index)
            r, g, b = resized.getpixel((x, y))
            data_array = data_array + str(r//25) + "," + str(g//25) + "," + str(b//25)+","

        data_array = data_array[:-1] + "};\n"

        set_frames_code = set_frames_code + "for(int i=0;i<strip.numPixels();i++){int r = pgm_read_word_near(frame"+str(frame_count)+"+i*3);int g = pgm_read_word_near(frame"+str(frame_count)+"+i*3+1);int b = pgm_read_word_near(frame"+str(frame_count)+"+i*3+2);strip.setPixelColor(i, strip.Color(r,g,b));}strip.show();delay(wait);\n"


        frame_count = frame_count + 1

except EOFError:
    pass # end of sequence


print(get_program(data_array, set_frames_code))
