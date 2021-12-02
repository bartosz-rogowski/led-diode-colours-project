#include <math.h>
#include <string.h>

int led_B = 11;
int led_G = 10;
int led_R = 9;

int sensorR = A2;
int sensorG = A1;
int sensorB = A0;

void (*func)();

//encodes values from message from the raspberry
int* get_values_from_message(char* message)
{
	char delim[] = ",";
	char *ptr = strtok(message, delim);

	int* values = calloc(4, sizeof(int));
	int i = 0;

	while(ptr)
	{
		values[i++] = atof(ptr);
		ptr = strtok(NULL, delim);
	}
	return values;
}

// the setup routine runs once when you press reset:
void setup() 
{   // initialize the digital pin as an output.
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

void readFromColourSensor() 
{
	while(1)
	{
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
		char* message_char;
		message.toCharArray(message_char, message.length())
		int* values = get_values_from_message(message_char);
		if(values[3] == 1)
		{
			free(values);
			break;
		}
		free(values);
	}
	// delay(1000); 
}

void readFromRaspberryPi() {
	while(1) 
	{
		String message = Serial.readStringUntil('\n');
		char* message_char;
		message.toCharArray(message_char, message.length())
		int* values = get_values_from_message(message_char);
	 	//analogwrite
		if(values[3] == 1)
		{
			free(values);
			break;
		}
		free(values);
	}
}

void loop() {
 if (Serial.available() > 0) {
		char data = Serial.read();
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
