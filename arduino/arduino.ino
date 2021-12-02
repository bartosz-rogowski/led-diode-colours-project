#include <math.h>
#include <string.h>

int led_B = 11;
int led_G = 10;
int led_R = 9;

int sensorR = A2;
int sensorG = A1;
int sensorB = A0;

//encodes values from message from the raspberry
int* get_values_from_message(char* message)
{
  char delim[] = ",";
  char *ptr = strtok(message, delim);

  int* values = (int*) calloc(4, sizeof(int));
  int i = 0;

  while(ptr)
  {
    values[i++] = atoi(ptr);
    ptr = strtok(NULL, delim);
  }
  return values;
}

// the setup routine runs once when you press reset:
void setup() 
{   // initialize the digital pin as an output.
  Serial.begin(9600);
//  Serial.setTimeout(5000);
  pinMode(led_R, OUTPUT);  
  pinMode(led_G, OUTPUT);
  pinMode(led_B, OUTPUT);
}

int toRGB(int bit10) {
  return bit10 / (pow(2, 10) - 1.) * 255;
}

void readFromColourSensor() 
{
  while(1)
  {
    if (Serial.available() > 0) {
      String message = Serial.readStringUntil('\n');
      const int message_char_length = message.length() + 1;
      char message_char[message_char_length];
      message.toCharArray(message_char, message_char_length);
      int* values = get_values_from_message(message_char);

      if(values[3] == 0) {
        int inputR = toRGB(analogRead(sensorR));
        int inputG = toRGB(analogRead(sensorG));
        int inputB = toRGB(analogRead(sensorB));
        
        analogWrite(led_R, inputR);
        analogWrite(led_G, inputG);
        analogWrite(led_B, inputB);
        
//        Serial.println(inputR);
//        Serial.println(inputG);
//        Serial.println(inputB);
//        Serial.println();
//        Serial.println();
        free(values);
      }
      else
      {
        analogWrite(led_R, 0);
        analogWrite(led_G, 0);
        analogWrite(led_B, 0);
        free(values);
        break;
      }
    }
  }
}

void readFromRaspberryPi() {
  while(1) 
  {
    if (Serial.available() > 0) {
      String message = Serial.readStringUntil('\n');
      Serial.println(message);
    
      const int message_char_length = message.length() + 1;
      char message_char[message_char_length];
      message.toCharArray(message_char, message_char_length);
      
      int* values = get_values_from_message(message_char); 
      analogWrite(led_R, values[0]);
      analogWrite(led_G, values[1]);
      analogWrite(led_B, values[2]);
  
//      Serial.println(values[0]);
//      Serial.println(values[1]);
//      Serial.println(values[2]);
//      Serial.println();
//      Serial.println();

      if(values[3] == 1)  
      {
        free(values);
        break;
      }
      free(values);
    }
  }
}

void loop() {
 Serial.println("");
 if (Serial.available() > 0) {
    char mode = Serial.read();
    switch(mode)
    {
      case '1':
        readFromRaspberryPi();
        break;

      case '2':
        readFromColourSensor();
        break;
    }
  }
  Serial.flush();
}     
