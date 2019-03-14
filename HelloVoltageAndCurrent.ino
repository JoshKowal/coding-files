/* This sketch measures the current and voltage across a motor. The
 * code uses conversion factors for the Attopilot 45A. If you wish
 * to use a different current and voltage sensor, you will need to
 * change the conversion factors.
 */

const int reads = 15;
const int volt = 0; //Connect volt pin on Attopilot to pin 0
const int curr = 1; //Connect current pin on Attopilot to pin 1
const int pwm = 9; //Connect signal pin on ESC to PWM pin 9
boolean running = false; //Can change this variable name; refers to if the motor is spinning
boolean high = false; //Condition to see if motor is on high throttle
boolean med = false; //Condition to see if motor is on medium throttle
#include <Servo.h> //Need this library to have the Arduino control throttle
#include <Wire.h>
Servo servo1; //Initialize a new Servo object

void setup(){
  pinMode(volt,INPUT);
  pinMode(curr,INPUT);
  Serial.begin(9600);
  Serial.println("Throttle Time Voltage Current");
  Wire.begin();
  /* These next lines establish communication between the ESC and
   * the Arduino. It also calibrates the throttle, which ranges from
   * 1000 (idle) to 2000 (max throttle). No need to change these lines.
   */
  servo1.attach(pwm);
  servo1.write(1000);
  delay(1000);
  servo1.write(2000);
  delay(1000);
  servo1.write(1000);
}

void loop(){
  //Only measure and print if the motor is running
  if (running){
    //Perform the reads and the math
    float voltage = 0.0;
    float current = 0.0;
    for (int j = 0; j < reads; j++){
      int v = analogRead(volt);
      int i = analogRead(curr);
      
      //You need to change these conversion factors for different sensors
      voltage += v / 49.45; //Equal to v * 5000 / 1024.0 / 242.3
      current += i / 14.94; //Equal to i * 5000 / 1024.0 / 73.2
    }
    //Find the averages and print them to the serial monitor
    if (high){
      Serial.print("High ");
    }
    if (med){
      Serial.print("Medium ");
    }
    Serial.print(millis());
    Serial.print(" ");
    Serial.print(voltage/reads);
    Serial.print(" ");
    Serial.println(current/reads);
  }
  //Check if Python tells Arduino to start/stop
  if (Serial.available() > 0){
    //If motor is on and byte is received, turn motor off
    if (running == true){
      int inbyte = int(Serial.read());
      if (inbyte > 0){
        running = false;
        servo1.write(1000);
      }
    }
  }
  if (Serial.available() > 0){
    if (running == false){
      //If motor is off and byte is received, turn motor on
      int inbyte2 = int(Serial.read());
      if (inbyte2 > 0){
        running = true;
        //If it was medium last time, turn on high throttle
        if (high == false){
          servo1.write(2000);
          high = true;
          med = false;
        }
        //If it was high last time, turn on medium throttle
        else{
          servo1.write(1500);
          high = false;
          med = true;
        }
      }
    }
  }
  delay(1000);
}
