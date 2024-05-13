#include <Arduino.h>

char serialData;
int freq = 10;
char freqNew = 0;
bool freqSetup = 0;

void setup()
{

    Serial.begin(9600);
    pinMode(2, OUTPUT);
    Serial.setTimeout(1);
}

void loop() 
{
  
    if (Serial.available() > 0)
    {

        serialData = Serial.read();

        if (serialData == '1')
        {
            /*freqNew = Serial.read();

            if(freqNew == '3')
            {
                while(freqSetup == 0)
                {
                    if(Serial.read() != '3')
                    {
                        freq = Serial.parseInt();
                        freqSetup = 1;
                    }
                }
            freqSetup = 0;
            }
            else
            {*/
            while(Serial.read() != '0')
            {
                digitalWrite(2, HIGH);
                delayMicroseconds(freq);
                digitalWrite(2, LOW);
                delayMicroseconds(freq);
            }
            }
    }
    else if (serialData == '0')
    {
      digitalWrite(2, LOW);
    }
}