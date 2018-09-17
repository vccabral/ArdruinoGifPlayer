


header = """
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

def get_frames_declaration(frames):

	frame_declarations = [
		frame_declarations.append("const PROGMEM uint8_t frames[] = {"+frame+"};")
		for frame in frames
	]
	return "\n".join(frame_declarations)


footer = """
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
  if (frame_count*strip.numPixels()<total_frames_count) {
    for(int i=0;i<strip.numPixels();i++){
      int start_index = frame_count*strip.numPixels() * 3;
//      int displayInt = pgm_read_word_near(0);
      int r = pgm_read_word_near(frames+start_index+i*3);
      int g = pgm_read_word_near(frames+start_index+i*3+1);
      int b = pgm_read_word_near(frames+start_index+i*3+2);
      if(test) {
        r = (rand() % static_cast<int>(10 + 1));
        g = (rand() % static_cast<int>(10 + 1));
        b = (rand() % static_cast<int>(10 + 1));
      }
      strip.setPixelColor(i, strip.Color(r,g,b));
//      strip.setPixelColor(i, strip.Color(,,);
    }
    delay(200);
    strip.show();
    frame_count = frame_count + 1;
  } else {
    frame_count = 0;
  }
}
"""

def get_program_text():
	return header + footer