#include <Arduino.h>


const int valSol = 16;
const int valProp = 17;
int Channel = 1;
int freq = 350;
int res = 10;
int state;


void pwm1(int valProp1,int Channel1,int freq1,int res1){
  pinMode(valProp1, OUTPUT);
  
  ledcSetup(Channel1, freq1, res1);
  ledcAttachPin(valProp1, Channel1);
}

void setup()
{
     //inicia comunicação serial
    Serial.begin(115200);
    pwm1(valProp, Channel,freq,res);
    pinMode(2, OUTPUT);
    pinMode(valSol, OUTPUT);
}

void serialMonitor()
{
    if(Serial.available() > 0)
    {
        char stateCase = Serial.read();
        switch(stateCase)
        {
            case '1':
            state = 1;
            Serial.println("Ligado");
            digitalWrite(2,1);
            break;
            case '0':
            state = 0;
            Serial.println("Desligado");
            digitalWrite(2,0);
            break;
        }
    }

}

void loop() 
{
    serialMonitor();    
}

void loadVar()
{

}