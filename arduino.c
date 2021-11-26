#include<math.h>

int led_B = 11;
int led_G = 10;
int led_R = 9;

int sensorR = A2;
int sensorG = A1;
int sensorB = A0;

void (*func)();

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
  Serial.setTimeout(5000);
  pinMode(led_R, OUTPUT);  
  pinMode(led_G, OUTPUT);
  pinMode(led_B, OUTPUT);
//  delay(10000);
  Serial.println("To powinno byc tylko raz");
//  char data = Serial.read();
//    switch(data)
//    {
//      case '1':
//        readFromColourSensor();
//        break;
//
//      case '2':
//        Serial.println("getting back together");
//        break;
//    }
}

int toRGB(int bit10) {
  return bit10 / (pow(2, 10) - 1.) * 255;
}

void readFromColourSensor() {
    int inputR = toRGB(analogRead(sensorR));
    int inputG = toRGB(analogRead(sensorG));
    int inputB = toRGB(analogRead(sensorB));
    
    analogWrite(led_R, inputR);
    analogWrite(led_G, inputG);
    analogWrite(led_B, inputB);
    
    Serial.println(inputR);
    Serial.println(inputG);
    Serial.println(inputB);
    
    Serial.println();
    Serial.println();
//    delay(1000); 
}

void readFromRaspberryPi() {
  while(1) {
    // reading rgb and flag values
    //sending rgb to led
    //jezeli zakonczymy program w pythonie, to musimy zrobić finally w pythonie
    // i wyslac flage do arduino
    if (flag == 0)
       break;
  }
}

void loop() {
 if (Serial.available() > 0) {
    char data = Serial.read();
    int flag = 1;
    switch(data)
    {
      case '1':
        readFromRaspberryPi();
        break;

      case '2':
        readFromColourSensor();
        break;
    }
  }
}     
