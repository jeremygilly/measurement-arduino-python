#include <Statistic.h>
Statistic myStats;
//long double initialReading = 0;
int sourceSensePin = A0;    // select the input pin for the potentiometer
int drainSensePin = A1;
double sourceSense = 0;
double drainSense = 0;
double sensor = 0;
int numberOfReadings = 400;
unsigned int ADCValue;
double Vcc;
double result;
double averagedOutput;

double array[99];


long readVcc() {
  long result;
  // Read 1.1V reference against AVcc
  ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
  delay(2); // Wait for Vref to settle
  ADCSRA |= _BV(ADSC); // Convert
  while (bit_is_set(ADCSRA,ADSC));
  result = ADCL;
  result |= ADCH<<8;
  result = 1125300L / result; // Back-calculate AVcc in mV
  return result;
}

double reading() {
  Vcc = readVcc();
  
  sourceSense = analogRead(sourceSensePin);
  sourceSense = (sourceSense / 1024.0) * Vcc;
  
  drainSense = analogRead(drainSensePin);
  drainSense = (drainSense / 1024.0) * Vcc;

  sensor = sourceSense - drainSense;
  if (sensor == 0) {
    sensor = reading();
  }
//  Serial.println(sensor);
  
  return sensor;
}

double average (double * array, int len)
{
  long sum = 0L ;  // sum will be larger than an item, long for safety.
  for (int i = 0 ; i < len ; i++)
    sum += array[i];
  return  ((double) sum) / len ;  // average will be fractional, so float may be appropriate.
}

void setup() { 
  Serial.begin(9600);
  analogReference(DEFAULT); // use AREF for reference voltage
}

void loop() {
//  int start_time = millis();
  memset(array,0,sizeof(array));
  
  for (int i = 0; i < numberOfReadings; i++) {
    double sample_reading = reading();
      myStats.add(sample_reading);
      // Code takes ~245 ms to run (100 readings per output reading). 
      //Adding a delay of 1 ms increases run time to 345 ms.
      delay(0);
  }
  
  averagedOutput = myStats.average();
  Serial.println(averagedOutput,2);
//  int finish_time = millis();
//  int difference = finish_time - start_time;
//  Serial.println(difference);
  
}
