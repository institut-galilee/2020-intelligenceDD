#include <Adafruit_GFX.h>   
#include <RGBmatrixPanel.h>

#define CLK 8  
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2
#define D   A5

RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, true);



int message = 0;
char msg[1];
char temp[14];
char car[11];
int i=0;
int lum=0;

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
    
    temp[i++]=char(Serial.read());
    
    
  }
  if(i==13){
    i=0;
    
    if(temp[4]!='a'){
        if(temp[12]=='n')
         matrix.setTextColor(matrix.Color333(0,7,0));
        else
          matrix.setTextColor(matrix.Color333(7,0,0));
        matrix.print(temp[0]);
        matrix.print(temp[1]);
        matrix.print(':');
        matrix.print(temp[2]);
        matrix.print(temp[3]);
        matrix.setCursor(1, 8);
        matrix.setTextColor(matrix.Color333(0,0,7));
        matrix.print(temp[4]);
        matrix.print(temp[5]);
        matrix.print(temp[6]);
        matrix.print(temp[7]);
        matrix.print(temp[8]);
        
        matrix.swapBuffers(false);
        delay(3000);
        matrix.fillScreen(0);
        
        matrix.setCursor(1, 0);
        if(temp[12]=='n')
         matrix.setTextColor(matrix.Color333(0,7,0));
        else
          matrix.setTextColor(matrix.Color333(7,0,0));
        matrix.print(temp[0]);
        matrix.print(temp[1]);
        matrix.print(':');
        matrix.print(temp[2]);
        matrix.print(temp[3]);
        matrix.setCursor(8, 8);
        matrix.setTextColor(matrix.Color333(0,0,7));
        
        matrix.print(temp[9]);
        matrix.print(temp[10]);
        matrix.print(temp[11]);
        
        matrix.swapBuffers(false);
        delay(1000);
        matrix.fillScreen(0);
        
        matrix.setCursor(1, 0);
        if(temp[12]=='n')
         matrix.setTextColor(matrix.Color333(0,7,0));
        else
          matrix.setTextColor(matrix.Color333(7,0,0));
        matrix.print(temp[0]);
        matrix.print(temp[1]);
        matrix.print(':');
        matrix.print(temp[2]);
        matrix.print(temp[3]);
        matrix.setCursor(4, 8);
        matrix.setTextColor(matrix.Color333(0,0,7));
        
        matrix.print('2');
        matrix.print('0');
        matrix.print('2');
        matrix.print('1');
        
        matrix.swapBuffers(false);
        delay(10);
    }
    else{
        if(temp[12]=='n')
         matrix.setTextColor(matrix.Color333(0,7,0));
        else
          matrix.setTextColor(matrix.Color333(7,0,0));
        matrix.print(temp[0]);
        matrix.print(temp[1]);
        matrix.print(':');
        matrix.print(temp[2]);
        matrix.print(temp[3]);
        matrix.setCursor(1, 8);
        matrix.setTextColor(matrix.Color333(0,0,7));
        matrix.print('T');
        matrix.print('=');
        matrix.print(temp[5]);
        matrix.print(temp[6]);
        matrix.print('c');
        
        matrix.swapBuffers(false);
        delay(3000);
        matrix.fillScreen(0);
        
        matrix.setCursor(1, 0);
        if(temp[12]=='n')
         matrix.setTextColor(matrix.Color333(0,7,0));
        else
          matrix.setTextColor(matrix.Color333(7,0,0));
        matrix.print(temp[0]);
        matrix.print(temp[1]);
        matrix.print(':');
        matrix.print(temp[2]);
        matrix.print(temp[3]);
        matrix.setCursor(1, 8);
        matrix.setTextColor(matrix.Color333(0,0,7));
        matrix.print('H');
        matrix.print('=');
        matrix.print(temp[8]);
        matrix.print(temp[9]);
        matrix.print('%');
        
        matrix.swapBuffers(false);
        delay(2000);
    }
  }
  
  
}
