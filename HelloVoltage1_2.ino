/*This sketch is for testing voltages with 5 panels. It is easy to
 * modify this code to test with fewer, more, or different panels.
 */


const int reads = 15; //Number of times the Arduino reads voltages per measurement

/*Initialize the pins; the name of the variable corresponds to the
 * name of the panel being tested, and the integer correponds to
 * which Analog Input pin that panel will be attached to.
 */
const int a = 0;
const int b = 1;
const int c = 2;
const int d = 3;
const int e = 4;

void setup(){
  //Configure all pins above as inputs
  pinMode(a,INPUT);
  pinMode(b,INPUT);
  pinMode(c,INPUT);
  pinMode(d,INPUT);
  pinMode(e,INPUT);
  Serial.begin(9600);
  /*Modify this print statement depending on the number of panels 
   * and the name of the panels being tested.
   */
  Serial.println("Time AVol BVol CVol DVol EVol");
}

void loop(){
  float voltage_a = 0.0;
  float voltage_b = 0.0;
  float voltage_c = 0.0;
  float voltage_d = 0.0;
  float voltage_e = 0.0;
  //Perform the actual measurements below; will take average later
  for (int i = 0; i < reads; i++){
    int va = analogRead(a);
    int vb = analogRead(b);
    int vc = analogRead(c);
    int vd = analogRead(d);
    int ve = analogRead(e);
    //Conversion factor
    voltage_a += (float(va) * 5.0)/1024.0;
    voltage_b += (float(vb) * 5.0)/1024.0;
    voltage_c += (float(vc) * 5.0)/1024.0;
    voltage_d += (float(vd) * 5.0)/1024.0;
    voltage_e += (float(ve) * 5.0)/1024.0;
  }
  //This is formatting for the serial monitor to print the time
  //in milliseconds since the program started running
  unsigned long time = millis();
    Serial.print(0);
    Serial.print(0);
    Serial.print(0);
    Serial.print(time);
  }
  else if (time < 100){
    Serial.print(0);
    Serial.print(0);
    Serial.print(time);
  }
  else if (time < 1000){
    Serial.print(0);
    Serial.print(time);
  }
  else{
    Serial.print(time);
  }
  //Get the average voltage for this sample and print to serial monitor
  Serial.print(" ");
  Serial.print(voltage_a/reads);
  Serial.print(" ");
  Serial.print(voltage_b/reads);
  Serial.print(" ");
  Serial.print(voltage_c/reads);
  Serial.print(" ");
  Serial.print(voltage_d/reads);
  Serial.print(" ");
  Serial.print(voltage_e/reads);
  Serial.print("\n"); //Moves to next line
  delay(1000);
}
