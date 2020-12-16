/***************************************************
*
* For 32x16 RGB LED matrix.
*
* @author lg.gang
* @version  V1.0
* @date  2016-10-28
*
* GNU Lesser General Public License.
* See <http://www.gnu.org/licenses/> for details.
* All above must be included in any redistribution
* ****************************************************/

#include <Adafruit_GFX.h>   // Core graphics library
#include <RGBmatrixPanel.h> // Hardware-specific library

// Similar to F(), but for PROGMEM string pointers rather than literals
#define F2(progmem_ptr) (const __FlashStringHelper *)progmem_ptr

#define CLK 8  // MUST be on PORTB! (Use pin 11 on Mega)
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2
// Last parameter = 'true' enables double-buffering, for flicker-free,
// buttery smooth animation.  Note that NOTHING WILL SHOW ON THE DISPLAY
// until the first call to swapBuffers().  This is normal.
RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, true);
// Double-buffered mode consumes nearly all the RAM available on the
// Arduino Uno -- only a handful of free bytes remain.  Even the
// following string needs to go in PROGMEM:

const char str[] PROGMEM = "12 Decembre 2020";
int    textX   = matrix.width(),
       textMin = sizeof(str) * -12,
       hue     = 0;

int message = 0;
char msg[1];
char temp[11];
int i=0;
int j=0;

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.setTextWrap(false); 
 
}

void loop() {
  matrix.fillScreen(0);
  
  matrix.setCursor(1, 0);
  matrix.setTextSize(1);
 
  if (Serial.available())  {
    //Serial.println(message);
    message = Serial.read() - '0';
    itoa(message,msg,10);
    temp[i++]=msg[0];
    //Serial.print(msg);
    //Serial.println(Serial.readString());
    //if (message == 0) {
      //matrix.print(msg);
    /*}
    else {
      matrix.setTextColor(matrix.Color333(7,4,0));
      matrix.print(msg);
    }*/
    /*
    matrix.setTextColor(matrix.ColorHSV(7, 255, 255, true));
    matrix.setCursor(textX, 8);
    matrix.setTextSize(1);
    matrix.print(F2(Serial.read()));*/
    
    
  }
  if(i==5){
    i=0;
    matrix.setTextColor(matrix.Color333(7,0,0));
    matrix.print(temp[0]);
    matrix.print(temp[1]);
    matrix.print(':');
    matrix.print(temp[2]);
    matrix.print(temp[3]);
    /*matrix.setCursor(1, 8);
    matrix.print(temp[4]);
    matrix.print(temp[5]);
    matrix.print(temp[6]);
    for(j=0;j<9;j++)
    Serial.print(temp[j]);
    Serial.println(temp[9]);*/
    matrix.swapBuffers(false);
    delay(1);
  }
  //Serial.println("");
  
  
}
